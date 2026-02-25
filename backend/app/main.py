"""FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.api import research, memory, reports
from app.services.llm_service import get_llm_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup / shutdown lifecycle."""
    yield
    # Cleanup
    llm = get_llm_service()
    await llm.close()


app = FastAPI(
    title="E-Commerce Intelligence Agent",
    description="Deep research agent for e-commerce business insights",
    version="1.0.0",
    lifespan=lifespan,
)

# ── CORS ─────────────────────────────────────────────────
settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routes ───────────────────────────────────────────────
app.include_router(research.router)
app.include_router(memory.router)
app.include_router(reports.router)


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "model": settings.GEMINI_MODEL,
        "api_key_set": bool(settings.OPENROUTER_API_KEY),
    }
