"""Query Analyzer — classifies user intent and extracts entities via LLM."""

from __future__ import annotations

import json

from app.models.enums import QueryType, ResearchMode
from app.services.llm_service import get_llm_service

ANALYSIS_PROMPT = """You are an e-commerce query analyzer. Classify the user's business question and extract structured information.

Return ONLY valid JSON with these fields:
{
  "query_type": "sentiment|pricing|competitor|performance|demand|feature_gap|general",
  "entities": {
    "products": ["product names or SKUs mentioned"],
    "categories": ["electronics|fashion|home|beauty|sports"],
    "brands": ["brand names mentioned"],
    "marketplaces": ["amazon|flipkart|shopify|d2c"]
  },
  "intent": "brief description of what the user wants to know",
  "focus": "what aspect to emphasize (e.g., negative reviews, margins, gaps)",
  "suggested_mode": "quick|deep",
  "is_follow_up": false,
  "follow_up_modifier": ""
}

Examples:
- "Top complaints for wireless headphones" → sentiment, quick
- "Full competitive analysis of electronics" → competitor, deep
- "Why is ELEC-006 underperforming?" → performance, deep
- "Focus on negative reviews only" → sentiment, quick, is_follow_up=true
"""


async def analyze_query(
    query: str,
    prior_context: str = "",
) -> dict:
    """Classify the query and extract structured entities."""
    llm = get_llm_service()

    messages = [
        {"role": "system", "content": ANALYSIS_PROMPT},
    ]
    if prior_context:
        messages.append({
            "role": "system",
            "content": f"Previous research context (for follow-ups):\n{prior_context}",
        })
    messages.append({"role": "user", "content": query})

    result = await llm.chat(messages, temperature=0.2, max_tokens=1024, json_mode=True)

    try:
        analysis = json.loads(result["content"])
    except json.JSONDecodeError:
        analysis = {
            "query_type": "general",
            "entities": {"products": [], "categories": [], "brands": [], "marketplaces": []},
            "intent": query,
            "focus": "",
            "suggested_mode": "quick",
            "is_follow_up": False,
            "follow_up_modifier": "",
        }

    analysis["_tokens_used"] = result.get("tokens_used", 0)
    return analysis
