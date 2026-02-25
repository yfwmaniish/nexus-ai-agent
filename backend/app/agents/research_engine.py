"""Research Engine — core LLM reasoning for quick and deep modes."""

from __future__ import annotations

import json
from typing import AsyncGenerator, Callable

from app.models.enums import ResearchMode
from app.services.llm_service import get_llm_service
from app.services.memory_service import get_memory_service

QUICK_SYSTEM = """You are an expert e-commerce business analyst. Provide a concise, actionable analysis.

RULES:
1. Be specific — reference actual product names, SKUs, prices, and ratings from the data
2. Quantify findings (percentages, counts, comparisons)
3. Include confidence level (0-1) for each major finding
4. Flag uncertainties clearly
5. Keep response focused and under 800 words

Return ONLY valid JSON:
{
  "executive_summary": "2-3 sentence overview",
  "findings": [
    {
      "title": "Finding title",
      "detail": "Detailed explanation with data references",
      "evidence": ["data point 1", "data point 2"],
      "confidence": 0.85,
      "sentiment": "positive|negative|neutral|mixed"
    }
  ],
  "recommendations": ["actionable recommendation 1", "recommendation 2"],
  "charts": [
    {
      "chart_type": "bar|line|donut|gauge|grouped_bar",
      "title": "Chart title",
      "data": [{"label": "X", "value": 10}],
      "x_key": "label",
      "y_keys": ["value"],
      "colors": ["#06B6D4", "#10B981", "#F43F5E"]
    }
  ],
  "confidence_score": 0.82,
  "uncertainty_notes": ["any caveats or data limitations"]
}"""

DEEP_SYSTEM = """You are a senior e-commerce strategist performing deep analysis. Follow this methodology:

PHASE 1 — OBSERVE: What does the data show? Key patterns, outliers, correlations.
PHASE 2 — HYPOTHESIZE: Why are these patterns occurring? Root causes, market dynamics.
PHASE 3 — VALIDATE: Which hypotheses are supported by evidence? Cross-reference data points.
PHASE 4 — SYNTHESIZE: What are the actionable insights? Strategic recommendations.

RULES:
1. Reference specific products, SKUs, prices, ratings, and review quotes
2. Compare against competitors with actual numbers
3. Identify trends and seasonal patterns
4. Quantify every claim (percentages, deltas, ratios)
5. Provide multiple chart specifications for data visualization
6. Be thorough — this should feel like a consultant's report
7. Include confidence scores and uncertainty notes
8. Aim for 1200-1800 words of analysis

Return ONLY valid JSON with the same structure as quick mode but more comprehensive findings (5-8 findings, 3-5 charts, 4-6 recommendations)."""


def _build_data_context(data: dict) -> str:
    """Serialize retrieved data into a context string for the LLM."""
    parts: list[str] = []

    if data.get("products"):
        parts.append("=== PRODUCT DATA ===")
        for p in data["products"][:15]:
            parts.append(
                f"SKU:{p['sku']} | {p['name']} | ₹{p['price']} (MRP ₹{p['mrp']}) | "
                f"Rating:{p['rating']} ({p['reviews_count']} reviews) | "
                f"Sales:{p['sales_volume']} | Margin:{p['margin_pct']}% | "
                f"Brand:{p['brand']} | Markets:{','.join(p['marketplace'])}"
            )

    if data.get("reviews"):
        parts.append("\n=== CUSTOMER REVIEWS ===")
        for r in data["reviews"][:20]:
            parts.append(
                f"[{r['sku']}] ★{r['rating']} ({r['sentiment']}) \"{r['title']}\" — "
                f"{r['text'][:200]} | Themes: {','.join(r.get('themes', []))}"
            )

    if data.get("competitors"):
        parts.append("\n=== COMPETITOR DATA ===")
        for c in data["competitors"][:10]:
            parts.append(
                f"vs {c['competitor']} ({c['competitor_brand']}) on {c['marketplace']} | "
                f"₹{c['price']} | Rating:{c['rating']} | "
                f"They lack: {','.join(c.get('missing_vs_us', []) or ['nothing'])} | "
                f"We lack: {','.join(c.get('we_lack', []) or ['nothing'])} | {c.get('notes', '')}"
            )

    if data.get("trends"):
        parts.append("\n=== MARKET TRENDS ===")
        for t in data["trends"][:15]:
            parts.append(
                f"{t['category']}/{t['subcategory']} [{t['month']}] | "
                f"Search:{t['search_volume']:,} | Demand:{t['demand_index']} | "
                f"AvgPrice:₹{t['avg_price']} ({t['price_trend']}) | {t['seasonal_note']}"
            )

    if data.get("summary_stats"):
        s = data["summary_stats"]
        parts.append(f"\n=== SUMMARY STATS ===\n{json.dumps(s, indent=2)}")

    return "\n".join(parts)


async def run_quick(
    query: str,
    analysis: dict,
    data: dict,
    memory_context: str = "",
) -> dict:
    """Quick mode — single LLM call, structured response."""
    llm = get_llm_service()
    data_ctx = _build_data_context(data)

    messages = [
        {"role": "system", "content": QUICK_SYSTEM},
    ]
    if memory_context:
        messages.append({"role": "system", "content": f"User preferences:\n{memory_context}"})

    messages.append({
        "role": "user",
        "content": f"Query: {query}\n\nAnalysis: {json.dumps(analysis, default=str)}\n\n{data_ctx}",
    })

    result = await llm.chat(messages, temperature=0.4, max_tokens=4096, json_mode=True)

    try:
        parsed = json.loads(result["content"])
    except json.JSONDecodeError:
        parsed = {
            "executive_summary": result["content"][:500],
            "findings": [],
            "recommendations": [],
            "charts": [],
            "confidence_score": 0.5,
            "uncertainty_notes": ["Failed to parse structured response"],
        }

    parsed["_tokens_used"] = result.get("tokens_used", 0)
    parsed["_duration"] = result.get("duration_seconds", 0)
    return parsed


async def run_deep(
    query: str,
    analysis: dict,
    data: dict,
    memory_context: str = "",
    on_progress: Callable[[str, str, int], None] | None = None,
) -> dict:
    """Deep mode — multi-step analysis with progress callbacks."""
    llm = get_llm_service()
    data_ctx = _build_data_context(data)

    steps = [
        ("Observing patterns", "Analyzing raw data for patterns, outliers, and key metrics..."),
        ("Forming hypotheses", "Identifying root causes and market dynamics..."),
        ("Validating findings", "Cross-referencing data points and confirming hypotheses..."),
        ("Synthesizing insights", "Generating actionable recommendations and visualizations..."),
    ]

    if on_progress:
        for i, (label, detail) in enumerate(steps[:3]):
            pct = (i + 1) * 20
            on_progress(label, detail, pct)

    messages = [
        {"role": "system", "content": DEEP_SYSTEM},
    ]
    if memory_context:
        messages.append({"role": "system", "content": f"User preferences:\n{memory_context}"})

    messages.append({
        "role": "user",
        "content": (
            f"Perform a deep analysis.\n\n"
            f"Query: {query}\n\n"
            f"Query Analysis: {json.dumps(analysis, default=str)}\n\n"
            f"{data_ctx}"
        ),
    })

    if on_progress:
        on_progress("Generating report", "LLM is synthesizing the full analysis...", 70)

    result = await llm.chat(messages, temperature=0.5, max_tokens=8192, json_mode=True)

    if on_progress:
        on_progress("Finalizing", "Structuring report and charts...", 95)

    try:
        parsed = json.loads(result["content"])
    except json.JSONDecodeError:
        parsed = {
            "executive_summary": result["content"][:800],
            "findings": [],
            "recommendations": [],
            "charts": [],
            "confidence_score": 0.5,
            "uncertainty_notes": ["Failed to parse structured response"],
        }

    parsed["_tokens_used"] = result.get("tokens_used", 0)
    parsed["_duration"] = result.get("duration_seconds", 0)
    return parsed
