"""Data Retriever — fetches relevant mock data based on query analysis."""

from __future__ import annotations

from app.data.mock_products import get_all_products, get_products_by_category, get_products_by_brand, search_products, get_product_by_sku
from app.data.mock_reviews import get_reviews_by_sku, get_reviews_by_sentiment, search_reviews, REVIEWS
from app.data.mock_competitors import get_competitors_for_sku, get_feature_gaps, COMPETITORS
from app.data.mock_trends import get_trends_by_category, get_trends_by_subcategory, get_high_demand_categories, TRENDS


def retrieve_data(analysis: dict) -> dict:
    """Gather all relevant data based on the query analysis.

    Uses the adapter pattern — swap MockDataSource for a real API later.
    """
    entities = analysis.get("entities", {})
    query_type = analysis.get("query_type", "general")

    result: dict = {
        "products": [],
        "reviews": [],
        "competitors": [],
        "trends": [],
        "summary_stats": {},
    }

    # ── Resolve products ─────────────────────────────────
    product_names = entities.get("products", [])
    categories = entities.get("categories", [])
    brands = entities.get("brands", [])

    found_products: list[dict] = []
    found_skus: set[str] = set()

    # By explicit SKU or name
    for name in product_names:
        if name.upper().startswith(("ELEC-", "FASH-", "HOME-", "BEAU-", "SPRT-")):
            p = get_product_by_sku(name.upper())
            if p and p["sku"] not in found_skus:
                found_products.append(p)
                found_skus.add(p["sku"])
        else:
            matches = search_products(name)
            for p in matches:
                if p["sku"] not in found_skus:
                    found_products.append(p)
                    found_skus.add(p["sku"])

    # By category
    for cat in categories:
        for p in get_products_by_category(cat):
            if p["sku"] not in found_skus:
                found_products.append(p)
                found_skus.add(p["sku"])

    # By brand
    for brand in brands:
        for p in get_products_by_brand(brand):
            if p["sku"] not in found_skus:
                found_products.append(p)
                found_skus.add(p["sku"])

    # Fallback: if nothing found, include top products by sales
    if not found_products:
        all_p = get_all_products()
        found_products = sorted(all_p, key=lambda x: x.get("sales_volume", 0), reverse=True)[:15]

    result["products"] = found_products[:20]  # Cap for context window

    # ── Resolve reviews ──────────────────────────────────
    focus = analysis.get("focus", "").lower()
    for p in result["products"]:
        sku_reviews = get_reviews_by_sku(p["sku"])
        if "negative" in focus:
            sku_reviews = [r for r in sku_reviews if r.get("sentiment") == "negative"]
        elif "positive" in focus:
            sku_reviews = [r for r in sku_reviews if r.get("sentiment") == "positive"]
        result["reviews"].extend(sku_reviews)

    # If query is about sentiment broadly, also search by text
    if query_type == "sentiment":
        intent = analysis.get("intent", "")
        text_matches = search_reviews(intent)
        existing_ids = {(r["sku"], r["title"]) for r in result["reviews"]}
        for r in text_matches:
            if (r["sku"], r["title"]) not in existing_ids:
                result["reviews"].append(r)

    result["reviews"] = result["reviews"][:30]

    # ── Resolve competitors ──────────────────────────────
    if query_type in ("competitor", "pricing", "feature_gap", "performance", "general"):
        for p in result["products"]:
            comps = get_competitors_for_sku(p["sku"])
            result["competitors"].extend(comps)

    result["competitors"] = result["competitors"][:15]

    # ── Resolve trends ───────────────────────────────────
    if query_type in ("demand", "performance", "general"):
        for cat in categories:
            result["trends"].extend(get_trends_by_category(cat))
        if not result["trends"]:
            result["trends"] = get_high_demand_categories(75)

    result["trends"] = result["trends"][:20]

    # ── Summary stats ────────────────────────────────────
    if result["products"]:
        prices = [p["price"] for p in result["products"]]
        ratings = [p["rating"] for p in result["products"]]
        margins = [p["margin_pct"] for p in result["products"]]
        result["summary_stats"] = {
            "product_count": len(result["products"]),
            "review_count": len(result["reviews"]),
            "competitor_count": len(result["competitors"]),
            "avg_price": round(sum(prices) / len(prices)),
            "avg_rating": round(sum(ratings) / len(ratings), 2),
            "avg_margin": round(sum(margins) / len(margins), 1),
            "total_sales_volume": sum(p.get("sales_volume", 0) for p in result["products"]),
        }

    return result
