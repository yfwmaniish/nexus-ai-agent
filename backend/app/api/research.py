"""Research API endpoints — the main entry point for research queries."""

from __future__ import annotations

import asyncio
import json
import time
import uuid

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import BaseModel

from app.agents.query_analyzer import analyze_query
from app.agents.data_retriever import retrieve_data
from app.agents.research_engine import run_quick, run_deep
from app.agents.report_generator import build_report
from app.models.enums import ResearchMode, ResearchStatus
from app.models.schemas import ResearchProgress, ResearchReport, ResearchRequest
from app.services.memory_service import get_memory_service

router = APIRouter(prefix="/api/research", tags=["research"])

# ── In-memory store (hackathon) ──────────────────────────
_reports: dict[str, ResearchReport] = {}
_prior_context: dict[str, dict] = {}  # research_id → analysis (for follow-ups)


@router.post("", response_model=ResearchReport)
async def start_research(req: ResearchRequest) -> ResearchReport:
    """Execute a research query (quick or deep) synchronously."""
    memory = get_memory_service()
    memory.record_query(req.query)
    memory_ctx = memory.get_context_prompt()

    # Step 1 — Analyze query
    prior = _prior_context.get(req.follow_up_of, {}) if req.follow_up_of else {}
    prior_str = json.dumps(prior, default=str) if prior else ""
    analysis = await analyze_query(req.query, prior_str)

    # Step 2 — Retrieve data
    data = retrieve_data(analysis)

    # Step 3 — Run research
    start = time.time()
    if req.mode == ResearchMode.QUICK:
        result = await run_quick(req.query, analysis, data, memory_ctx)
    else:
        result = await run_deep(req.query, analysis, data, memory_ctx)

    # Step 4 — Build report
    report = build_report(req.query, req.mode, analysis, result)
    report.duration_seconds = round(time.time() - start, 2)

    _reports[report.id] = report
    _prior_context[report.id] = analysis

    # Learn from usage
    qt = analysis.get("query_type")
    if qt:
        memory.learn_preference("last_query_type", qt)

    return report


@router.get("/history", response_model=list[dict])
async def get_history():
    """Return brief metadata for all past research sessions."""
    return [
        {
            "id": r.id,
            "query": r.query,
            "mode": r.mode,
            "status": r.status,
            "confidence_score": r.confidence_score,
            "created_at": r.created_at,
            "duration_seconds": r.duration_seconds,
        }
        for r in sorted(_reports.values(), key=lambda x: x.created_at, reverse=True)
    ]


@router.get("/{research_id}", response_model=ResearchReport)
async def get_research(research_id: str):
    """Get a specific research report by ID."""
    report = _reports.get(research_id)
    if not report:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Research not found")
    return report


# ── WebSocket for streaming research ─────────────────────

@router.websocket("/ws/{session_id}")
async def research_stream(ws: WebSocket, session_id: str):
    """Stream research progress and final report over WebSocket."""
    await ws.accept()

    try:
        # Wait for research request from client
        raw = await ws.receive_text()
        req_data = json.loads(raw)
        req = ResearchRequest(**req_data)

        memory = get_memory_service()
        memory.record_query(req.query)
        memory_ctx = memory.get_context_prompt()

        # Progress callback
        async def send_progress(label: str, detail: str, pct: int):
            prog = ResearchProgress(
                research_id=session_id,
                status=ResearchStatus.RESEARCHING,
                step_label=label,
                step_detail=detail,
                progress_pct=pct,
            )
            await ws.send_text(json.dumps({"type": "progress", "data": prog.model_dump()}))

        # Step 1 — Analyze
        await send_progress("Analyzing query", "Understanding your business question...", 10)
        prior = _prior_context.get(req.follow_up_of, {}) if req.follow_up_of else {}
        analysis = await analyze_query(req.query, json.dumps(prior, default=str) if prior else "")

        # Step 2 — Retrieve
        await send_progress("Retrieving data", f"Found relevant data for {analysis.get('query_type', 'general')} analysis...", 25)
        data = retrieve_data(analysis)
        stats = data.get("summary_stats", {})
        await send_progress(
            "Data loaded",
            f"{stats.get('product_count', 0)} products, {stats.get('review_count', 0)} reviews, {stats.get('competitor_count', 0)} competitors",
            35,
        )

        # Step 3 — Research
        start = time.time()

        def sync_progress(label, detail, pct):
            asyncio.get_event_loop().create_task(send_progress(label, detail, pct))

        if req.mode == ResearchMode.QUICK:
            await send_progress("Analyzing", "Running quick analysis...", 50)
            result = await run_quick(req.query, analysis, data, memory_ctx)
        else:
            result = await run_deep(req.query, analysis, data, memory_ctx, on_progress=sync_progress)

        # Step 4 — Build report
        await send_progress("Generating report", "Structuring findings and charts...", 90)
        report = build_report(req.query, req.mode, analysis, result)
        report.duration_seconds = round(time.time() - start, 2)

        _reports[report.id] = report
        _prior_context[report.id] = analysis

        # Send final report
        await send_progress("Complete", "Research complete!", 100)
        await ws.send_text(json.dumps({"type": "report", "data": report.model_dump()}))

    except WebSocketDisconnect:
        pass
    except Exception as e:
        try:
            await ws.send_text(json.dumps({"type": "error", "message": str(e)}))
        except Exception:
            pass
