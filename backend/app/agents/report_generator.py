"""Report Generator — transforms raw research into a structured ResearchReport."""

from __future__ import annotations

import uuid
from datetime import datetime

from app.models.enums import QueryType, ResearchMode, ResearchStatus
from app.models.schemas import ChartSpec, Finding, ResearchReport


def build_report(
    query: str,
    mode: ResearchMode,
    analysis: dict,
    research_result: dict,
) -> ResearchReport:
    """Assemble a ResearchReport from the raw LLM research output."""

    query_type = QueryType.GENERAL
    raw_qt = analysis.get("query_type", "general")
    try:
        query_type = QueryType(raw_qt)
    except ValueError:
        pass

    # ── Parse findings ───────────────────────────────────
    findings: list[Finding] = []
    for f in research_result.get("findings", []):
        findings.append(Finding(
            title=f.get("title", "Untitled"),
            detail=f.get("detail", ""),
            evidence=f.get("evidence", []),
            confidence=min(max(f.get("confidence", 0.7), 0.0), 1.0),
            sentiment=f.get("sentiment"),
        ))

    # ── Parse charts ─────────────────────────────────────
    charts: list[ChartSpec] = []
    for c in research_result.get("charts", []):
        charts.append(ChartSpec(
            chart_type=c.get("chart_type", "bar"),
            title=c.get("title", ""),
            data=c.get("data", []),
            x_key=c.get("x_key", "label"),
            y_keys=c.get("y_keys", ["value"]),
            colors=c.get("colors", ["#06B6D4", "#10B981", "#F43F5E"]),
        ))

    return ResearchReport(
        id=uuid.uuid4().hex[:12],
        query=query,
        mode=mode,
        query_type=query_type,
        status=ResearchStatus.COMPLETE,
        executive_summary=research_result.get("executive_summary", ""),
        findings=findings,
        recommendations=research_result.get("recommendations", []),
        charts=charts,
        confidence_score=min(max(research_result.get("confidence_score", 0.7), 0.0), 1.0),
        uncertainty_notes=research_result.get("uncertainty_notes", []),
        tokens_used=research_result.get("_tokens_used", 0),
        cost_usd=_estimate_cost(research_result.get("_tokens_used", 0)),
        duration_seconds=research_result.get("_duration", 0),
        created_at=datetime.utcnow().isoformat(),
    )


def _estimate_cost(tokens: int) -> float:
    """Rough cost estimate for Gemini Flash via OpenRouter ($0.10/1M input)."""
    return round(tokens * 0.0000001, 6)
