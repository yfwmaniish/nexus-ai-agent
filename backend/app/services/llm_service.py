"""OpenRouter LLM service — wraps Gemini calls via the OpenRouter API."""

from __future__ import annotations

import json
import time
from typing import AsyncGenerator

import httpx

from app.config import get_settings


class LLMService:
    """Thin async wrapper around the OpenRouter chat-completions endpoint."""

    def __init__(self) -> None:
        s = get_settings()
        self.base_url = s.OPENROUTER_BASE_URL
        self.api_key = s.OPENROUTER_API_KEY
        self.model = s.GEMINI_MODEL
        self._client = httpx.AsyncClient(timeout=120.0)

    # ── Non-streaming call ───────────────────────────────

    async def chat(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        json_mode: bool = False,
    ) -> dict:
        """Send a chat completion and return the full response."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000",
            "X-Title": "E-Commerce Intelligence Agent",
        }

        body: dict = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        if json_mode:
            body["response_format"] = {"type": "json_object"}

        start = time.time()
        resp = await self._client.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=body,
        )
        resp.raise_for_status()
        data = resp.json()
        elapsed = time.time() - start

        content = data["choices"][0]["message"]["content"]
        usage = data.get("usage", {})

        return {
            "content": content,
            "tokens_used": usage.get("total_tokens", 0),
            "prompt_tokens": usage.get("prompt_tokens", 0),
            "completion_tokens": usage.get("completion_tokens", 0),
            "duration_seconds": round(elapsed, 2),
            "model": self.model,
        }

    # ── Streaming call ───────────────────────────────────

    async def chat_stream(
        self,
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> AsyncGenerator[str, None]:
        """Stream chat completion tokens as they arrive."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000",
            "X-Title": "E-Commerce Intelligence Agent",
        }
        body = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": True,
        }

        async with self._client.stream(
            "POST",
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=body,
        ) as resp:
            resp.raise_for_status()
            async for line in resp.aiter_lines():
                if not line.startswith("data: "):
                    continue
                payload = line[6:]
                if payload.strip() == "[DONE]":
                    break
                try:
                    chunk = json.loads(payload)
                    delta = chunk["choices"][0].get("delta", {})
                    token = delta.get("content", "")
                    if token:
                        yield token
                except (json.JSONDecodeError, KeyError, IndexError):
                    continue

    async def close(self) -> None:
        await self._client.aclose()


# ── Module-level singleton ───────────────────────────────

_instance: LLMService | None = None


def get_llm_service() -> LLMService:
    global _instance
    if _instance is None:
        _instance = LLMService()
    return _instance
