"""Domain-aware memory manager — persists user preferences and learned context."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from app.config import get_settings
from app.models.schemas import MemoryState


class MemoryService:
    """Manages user preferences, past queries, and learned patterns.

    Persists to a local JSON file for hackathon simplicity.
    """

    def __init__(self) -> None:
        storage = Path(get_settings().DATA_DIR)
        storage.mkdir(parents=True, exist_ok=True)
        self._file = storage / "memory.json"
        self._state = self._load()

    # ── Public API ───────────────────────────────────────

    def get_state(self) -> MemoryState:
        return self._state

    def update(
        self,
        preferred_kpis: list[str] | None = None,
        preferred_marketplaces: list[str] | None = None,
        preferred_categories: list[str] | None = None,
        custom_context: str | None = None,
    ) -> MemoryState:
        if preferred_kpis is not None:
            self._state.preferred_kpis = preferred_kpis
        if preferred_marketplaces is not None:
            self._state.preferred_marketplaces = preferred_marketplaces  # type: ignore[assignment]
        if preferred_categories is not None:
            self._state.preferred_categories = preferred_categories  # type: ignore[assignment]
        if custom_context is not None:
            self._state.custom_context = custom_context
        self._persist()
        return self._state

    def record_query(self, query: str) -> None:
        self._state.past_queries.append(query)
        # Keep last 50 queries
        self._state.past_queries = self._state.past_queries[-50:]
        self._persist()

    def learn_preference(self, key: str, value: Any) -> None:
        self._state.learned_preferences[key] = value
        self._persist()

    def get_context_prompt(self) -> str:
        """Build a context string the LLM can use to personalize responses."""
        s = self._state
        parts: list[str] = []
        if s.preferred_kpis:
            parts.append(f"Preferred KPIs: {', '.join(s.preferred_kpis)}")
        if s.preferred_marketplaces:
            parts.append(f"Preferred marketplaces: {', '.join(str(m) for m in s.preferred_marketplaces)}")
        if s.preferred_categories:
            parts.append(f"Focus categories: {', '.join(str(c) for c in s.preferred_categories)}")
        if s.custom_context:
            parts.append(f"Additional context: {s.custom_context}")
        if s.past_queries:
            recent = s.past_queries[-5:]
            parts.append(f"Recent queries: {'; '.join(recent)}")
        if s.learned_preferences:
            lp = ", ".join(f"{k}={v}" for k, v in s.learned_preferences.items())
            parts.append(f"Learned preferences: {lp}")
        return "\n".join(parts) if parts else "No prior context."

    # ── Persistence ──────────────────────────────────────

    def _load(self) -> MemoryState:
        if self._file.exists():
            try:
                raw = json.loads(self._file.read_text(encoding="utf-8"))
                return MemoryState(**raw)
            except (json.JSONDecodeError, Exception):
                pass
        return MemoryState()

    def _persist(self) -> None:
        self._file.write_text(
            self._state.model_dump_json(indent=2),
            encoding="utf-8",
        )


# ── Singleton ────────────────────────────────────────────

_instance: MemoryService | None = None


def get_memory_service() -> MemoryService:
    global _instance
    if _instance is None:
        _instance = MemoryService()
    return _instance
