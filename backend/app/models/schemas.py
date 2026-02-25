"""Pydantic models for request/response validation across the API."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from .enums import Marketplace, ProductCategory, QueryType, ResearchMode, ResearchStatus


# ── Request Models ─────────────────────────────────────────


class ResearchRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=2000)
    mode: ResearchMode = ResearchMode.QUICK
    follow_up_of: str | None = Field(None, description="ID of prior research for follow-ups")


class MemoryUpdate(BaseModel):
    preferred_kpis: list[str] | None = None
    preferred_marketplaces: list[Marketplace] | None = None
    preferred_categories: list[ProductCategory] | None = None
    custom_context: str | None = None


# ── Response Models ────────────────────────────────────────


class ResearchProgress(BaseModel):
    """Streamed over WebSocket during research."""
    research_id: str
    status: ResearchStatus
    step_label: str = ""
    step_detail: str = ""
    progress_pct: int = 0
    timestamp: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class Finding(BaseModel):
    title: str
    detail: str
    evidence: list[str] = []
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)
    sentiment: str | None = None  # positive / negative / neutral


class ChartSpec(BaseModel):
    """Generic spec the frontend can render with Recharts."""
    chart_type: str  # bar, line, donut, gauge, grouped_bar
    title: str
    data: list[dict[str, Any]]
    x_key: str = ""
    y_keys: list[str] = []
    colors: list[str] = []


class ResearchReport(BaseModel):
    id: str = Field(default_factory=lambda: uuid.uuid4().hex[:12])
    query: str
    mode: ResearchMode
    query_type: QueryType = QueryType.GENERAL
    status: ResearchStatus = ResearchStatus.PENDING

    # ── Results ──
    executive_summary: str = ""
    findings: list[Finding] = []
    recommendations: list[str] = []
    charts: list[ChartSpec] = []
    confidence_score: float = 0.0
    uncertainty_notes: list[str] = []

    # ── Meta ──
    tokens_used: int = 0
    cost_usd: float = 0.0
    duration_seconds: float = 0.0
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class MemoryState(BaseModel):
    preferred_kpis: list[str] = ["GMV", "CAC", "LTV", "Margin"]
    preferred_marketplaces: list[Marketplace] = [Marketplace.AMAZON, Marketplace.FLIPKART]
    preferred_categories: list[ProductCategory] = [ProductCategory.ELECTRONICS]
    custom_context: str = ""
    past_queries: list[str] = []
    learned_preferences: dict[str, Any] = {}
