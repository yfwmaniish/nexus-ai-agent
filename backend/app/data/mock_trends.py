"""Mock market trends — monthly metrics for demand, pricing, and search volume."""

TRENDS: list[dict] = [
    # ── Electronics trends ──
    {"category": "electronics", "subcategory": "headphones", "month": "2025-01", "search_volume": 145000, "demand_index": 72, "avg_price": 4200, "price_trend": "stable", "seasonal_note": "Post-holiday dip"},
    {"category": "electronics", "subcategory": "headphones", "month": "2025-02", "search_volume": 132000, "demand_index": 68, "avg_price": 4100, "price_trend": "declining", "seasonal_note": "Low season"},
    {"category": "electronics", "subcategory": "headphones", "month": "2025-03", "search_volume": 138000, "demand_index": 70, "avg_price": 4150, "price_trend": "stable", "seasonal_note": "Exam season, students buying"},
    {"category": "electronics", "subcategory": "headphones", "month": "2025-04", "search_volume": 155000, "demand_index": 75, "avg_price": 4300, "price_trend": "rising", "seasonal_note": "New launches drive interest"},
    {"category": "electronics", "subcategory": "headphones", "month": "2025-05", "search_volume": 148000, "demand_index": 73, "avg_price": 4250, "price_trend": "stable", "seasonal_note": "Summer sales begin"},
    {"category": "electronics", "subcategory": "headphones", "month": "2025-06", "search_volume": 162000, "demand_index": 78, "avg_price": 3900, "price_trend": "declining", "seasonal_note": "Summer sale discounts"},
    {"category": "electronics", "subcategory": "smartwatches", "month": "2025-01", "search_volume": 98000, "demand_index": 65, "avg_price": 8500, "price_trend": "stable", "seasonal_note": "New Year fitness resolutions"},
    {"category": "electronics", "subcategory": "smartwatches", "month": "2025-02", "search_volume": 112000, "demand_index": 72, "avg_price": 8200, "price_trend": "declining", "seasonal_note": "Valentine's gifting"},
    {"category": "electronics", "subcategory": "smartwatches", "month": "2025-03", "search_volume": 95000, "demand_index": 62, "avg_price": 8000, "price_trend": "declining", "seasonal_note": "Off-season"},
    {"category": "electronics", "subcategory": "smartwatches", "month": "2025-04", "search_volume": 105000, "demand_index": 68, "avg_price": 8300, "price_trend": "rising", "seasonal_note": "Summer fitness prep"},
    # ── Fashion trends ──
    {"category": "fashion", "subcategory": "sneakers", "month": "2025-01", "search_volume": 210000, "demand_index": 80, "avg_price": 3800, "price_trend": "stable", "seasonal_note": "New year, new shoes trend"},
    {"category": "fashion", "subcategory": "sneakers", "month": "2025-02", "search_volume": 195000, "demand_index": 76, "avg_price": 3750, "price_trend": "stable", "seasonal_note": "Steady demand"},
    {"category": "fashion", "subcategory": "sneakers", "month": "2025-03", "search_volume": 225000, "demand_index": 85, "avg_price": 3900, "price_trend": "rising", "seasonal_note": "Spring collections launch"},
    {"category": "fashion", "subcategory": "sneakers", "month": "2025-04", "search_volume": 240000, "demand_index": 88, "avg_price": 4100, "price_trend": "rising", "seasonal_note": "Peak season begins"},
    {"category": "fashion", "subcategory": "bags", "month": "2025-01", "search_volume": 85000, "demand_index": 60, "avg_price": 2800, "price_trend": "stable", "seasonal_note": "Travel season starts"},
    {"category": "fashion", "subcategory": "bags", "month": "2025-02", "search_volume": 92000, "demand_index": 65, "avg_price": 2750, "price_trend": "stable", "seasonal_note": "Weekend trip demand"},
    {"category": "fashion", "subcategory": "bags", "month": "2025-03", "search_volume": 110000, "demand_index": 72, "avg_price": 2900, "price_trend": "rising", "seasonal_note": "Spring travel peak"},
    # ── Home trends ──
    {"category": "home", "subcategory": "air_purifiers", "month": "2025-09", "search_volume": 75000, "demand_index": 55, "avg_price": 11000, "price_trend": "stable", "seasonal_note": "Pre-pollution season awareness"},
    {"category": "home", "subcategory": "air_purifiers", "month": "2025-10", "search_volume": 185000, "demand_index": 92, "avg_price": 12500, "price_trend": "rising", "seasonal_note": "Delhi pollution spike"},
    {"category": "home", "subcategory": "air_purifiers", "month": "2025-11", "search_volume": 320000, "demand_index": 98, "avg_price": 14000, "price_trend": "rising", "seasonal_note": "Peak pollution — highest demand"},
    {"category": "home", "subcategory": "air_purifiers", "month": "2025-12", "search_volume": 220000, "demand_index": 85, "avg_price": 13000, "price_trend": "declining", "seasonal_note": "Post-peak, holiday sales"},
    {"category": "home", "subcategory": "kitchen_appliances", "month": "2025-01", "search_volume": 165000, "demand_index": 75, "avg_price": 5500, "price_trend": "stable", "seasonal_note": "New year kitchen goals"},
    {"category": "home", "subcategory": "kitchen_appliances", "month": "2025-10", "search_volume": 280000, "demand_index": 95, "avg_price": 5200, "price_trend": "declining", "seasonal_note": "Festive sale (Diwali)"},
    # ── Beauty trends ──
    {"category": "beauty", "subcategory": "skincare", "month": "2025-01", "search_volume": 340000, "demand_index": 82, "avg_price": 950, "price_trend": "stable", "seasonal_note": "New year skincare routines"},
    {"category": "beauty", "subcategory": "skincare", "month": "2025-02", "search_volume": 310000, "demand_index": 78, "avg_price": 920, "price_trend": "stable", "seasonal_note": "Winter skincare continues"},
    {"category": "beauty", "subcategory": "skincare", "month": "2025-03", "search_volume": 365000, "demand_index": 86, "avg_price": 980, "price_trend": "rising", "seasonal_note": "Summer prep — sunscreen spike"},
    {"category": "beauty", "subcategory": "skincare", "month": "2025-04", "search_volume": 390000, "demand_index": 90, "avg_price": 1000, "price_trend": "rising", "seasonal_note": "Peak sunscreen + serum season"},
    {"category": "beauty", "subcategory": "fragrances", "month": "2025-02", "search_volume": 120000, "demand_index": 78, "avg_price": 2200, "price_trend": "rising", "seasonal_note": "Valentine's gifting peak"},
    {"category": "beauty", "subcategory": "fragrances", "month": "2025-10", "search_volume": 145000, "demand_index": 85, "avg_price": 2400, "price_trend": "rising", "seasonal_note": "Festive gifting season"},
    # ── Sports trends ──
    {"category": "sports", "subcategory": "fitness_equipment", "month": "2025-01", "search_volume": 280000, "demand_index": 95, "avg_price": 3500, "price_trend": "rising", "seasonal_note": "New year resolutions — peak"},
    {"category": "sports", "subcategory": "fitness_equipment", "month": "2025-02", "search_volume": 220000, "demand_index": 80, "avg_price": 3400, "price_trend": "declining", "seasonal_note": "Resolution dropoff"},
    {"category": "sports", "subcategory": "fitness_equipment", "month": "2025-03", "search_volume": 180000, "demand_index": 70, "avg_price": 3300, "price_trend": "declining", "seasonal_note": "Steady decline"},
    {"category": "sports", "subcategory": "running_shoes", "month": "2025-01", "search_volume": 155000, "demand_index": 78, "avg_price": 6500, "price_trend": "stable", "seasonal_note": "Marathon season prep"},
    {"category": "sports", "subcategory": "running_shoes", "month": "2025-02", "search_volume": 170000, "demand_index": 82, "avg_price": 6800, "price_trend": "rising", "seasonal_note": "Spring marathon registrations"},
    {"category": "sports", "subcategory": "running_shoes", "month": "2025-10", "search_volume": 195000, "demand_index": 88, "avg_price": 6200, "price_trend": "declining", "seasonal_note": "Festive discounts on running gear"},
]


def get_trends_by_category(category: str) -> list[dict]:
    return [t for t in TRENDS if t["category"] == category.lower()]

def get_trends_by_subcategory(subcategory: str) -> list[dict]:
    return [t for t in TRENDS if t["subcategory"] == subcategory.lower()]

def get_high_demand_categories(threshold: int = 80) -> list[dict]:
    return [t for t in TRENDS if t["demand_index"] >= threshold]

def get_price_trends(category: str) -> list[dict]:
    return sorted(
        [t for t in TRENDS if t["category"] == category.lower()],
        key=lambda x: x["month"]
    )
