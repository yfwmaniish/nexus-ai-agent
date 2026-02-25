"""Memory API endpoints — user preferences and domain-aware context."""

from fastapi import APIRouter

from app.models.schemas import MemoryState, MemoryUpdate
from app.services.memory_service import get_memory_service

router = APIRouter(prefix="/api/memory", tags=["memory"])


@router.get("/preferences", response_model=MemoryState)
async def get_preferences():
    return get_memory_service().get_state()


@router.put("/preferences", response_model=MemoryState)
async def update_preferences(update: MemoryUpdate):
    mem = get_memory_service()
    return mem.update(
        preferred_kpis=update.preferred_kpis,
        preferred_marketplaces=[m.value if hasattr(m, "value") else m for m in update.preferred_marketplaces] if update.preferred_marketplaces else None,
        preferred_categories=[c.value if hasattr(c, "value") else c for c in update.preferred_categories] if update.preferred_categories else None,
        custom_context=update.custom_context,
    )


@router.get("/context")
async def get_context():
    """Return the context prompt string the agent uses for personalization."""
    return {"context": get_memory_service().get_context_prompt()}
