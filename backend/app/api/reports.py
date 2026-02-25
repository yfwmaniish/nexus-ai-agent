"""Reports API — list and retrieve generated reports."""

from fastapi import APIRouter, HTTPException

from app.models.schemas import ResearchReport

router = APIRouter(prefix="/api/reports", tags=["reports"])

# Import the shared store from research router
from app.api.research import _reports


@router.get("", response_model=list[dict])
async def list_reports():
    """List all reports with summary metadata."""
    return [
        {
            "id": r.id,
            "query": r.query,
            "mode": r.mode,
            "query_type": r.query_type,
            "executive_summary": r.executive_summary[:200],
            "confidence_score": r.confidence_score,
            "findings_count": len(r.findings),
            "created_at": r.created_at,
            "duration_seconds": r.duration_seconds,
        }
        for r in sorted(_reports.values(), key=lambda x: x.created_at, reverse=True)
    ]


@router.get("/{report_id}", response_model=ResearchReport)
async def get_report(report_id: str):
    report = _reports.get(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return report
