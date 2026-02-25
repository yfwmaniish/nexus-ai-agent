"""Mock competitor data — pricing comparisons and feature gaps."""

COMPETITORS: list[dict] = [
    # ── Electronics competitors ──
    {"our_sku": "ELEC-001", "competitor": "SonicBoom ANC Pro", "competitor_brand": "SonicBoom", "marketplace": "amazon", "price": 5999, "rating": 4.4, "features": ["ANC", "45hr battery", "Bluetooth 5.3", "USB-C", "Multipoint"], "missing_vs_us": [], "we_lack": ["Multipoint connection", "USB-C charging"], "notes": "Market leader, 22% more expensive"},
    {"our_sku": "ELEC-001", "competitor": "BassKing Over-Ear", "competitor_brand": "BassKing", "marketplace": "flipkart", "price": 3999, "rating": 4.0, "features": ["ANC", "30hr battery", "Bluetooth 5.0", "Foldable"], "missing_vs_us": ["Bluetooth 5.3"], "we_lack": [], "notes": "Budget competitor, weaker ANC"},
    {"our_sku": "ELEC-003", "competitor": "Amazon Echo 4th Gen", "competitor_brand": "Amazon", "marketplace": "amazon", "price": 4499, "rating": 4.6, "features": ["360° audio", "Alexa", "Smart hub", "Zigbee"], "missing_vs_us": [], "we_lack": ["Smart home hub", "Zigbee", "Massive ecosystem"], "notes": "Dominant ecosystem player"},
    {"our_sku": "ELEC-005", "competitor": "FitBand Galaxy Watch", "competitor_brand": "FitBand", "marketplace": "amazon", "price": 17999, "rating": 4.3, "features": ["AMOLED", "GPS", "SpO2", "LTE", "NFC payments"], "missing_vs_us": [], "we_lack": ["LTE connectivity", "NFC payments"], "notes": "20% premium, has cellular"},
    {"our_sku": "ELEC-005", "competitor": "TimeTech Pixel Watch", "competitor_brand": "TimeTech", "marketplace": "flipkart", "price": 16999, "rating": 4.2, "features": ["AMOLED", "GPS", "ECG", "Fall detection"], "missing_vs_us": [], "we_lack": ["ECG", "Fall detection"], "notes": "Health-focused competitor"},
    {"our_sku": "ELEC-008", "competitor": "AnkerNano 65W", "competitor_brand": "Anker", "marketplace": "amazon", "price": 2499, "rating": 4.8, "features": ["65W GaN", "3 ports", "PD3.0", "Compact", "Foldable plug"], "missing_vs_us": [], "we_lack": ["Foldable plug"], "notes": "Brand leader, 25% more expensive"},
    # ── Fashion competitors ──
    {"our_sku": "FASH-001", "competitor": "RetroKick Classic", "competitor_brand": "RetroKick", "marketplace": "amazon", "price": 4299, "rating": 4.5, "features": ["Suede upper", "Rubber sole", "Breathable", "Wide sizes available"], "missing_vs_us": [], "we_lack": ["Wide size options", "Suede material"], "notes": "Premium retro brand"},
    {"our_sku": "FASH-001", "competitor": "StepUp RetroMax", "competitor_brand": "StepUp", "marketplace": "flipkart", "price": 2799, "rating": 3.8, "features": ["Synthetic upper", "EVA sole", "10 colors"], "missing_vs_us": ["Leather upper"], "we_lack": ["Color variety"], "notes": "Budget option, lower quality"},
    {"our_sku": "FASH-005", "competitor": "TravelPro Duffel", "competitor_brand": "TravelPro", "marketplace": "amazon", "price": 5499, "rating": 4.6, "features": ["Canvas", "Laptop sleeve", "Trolley strap", "RFID pocket"], "missing_vs_us": [], "we_lack": ["Trolley strap", "RFID pocket"], "notes": "Premium travel brand"},
    # ── Home competitors ──
    {"our_sku": "HOME-003", "competitor": "RoboVac UltraClean", "competitor_brand": "RoboVac", "marketplace": "amazon", "price": 24999, "rating": 4.3, "features": ["LiDAR", "Mopping", "Auto-empty", "Self-cleaning mop", "AI obstacle"], "missing_vs_us": [], "we_lack": ["Self-cleaning mop", "AI obstacle avoidance"], "notes": "25% premium, smarter AI"},
    {"our_sku": "HOME-005", "competitor": "BreatheEasy Pro", "competitor_brand": "BreatheEasy", "marketplace": "amazon", "price": 15999, "rating": 4.5, "features": ["HEPA H14", "PM2.5", "CO2 sensor", "App control", "800sqft"], "missing_vs_us": [], "we_lack": ["CO2 sensor", "Larger coverage", "App control"], "notes": "Better sensors, larger area"},
    {"our_sku": "HOME-009", "competitor": "FryMaster Digital 5.5L", "competitor_brand": "FryMaster", "marketplace": "flipkart", "price": 4999, "rating": 4.4, "features": ["5.5L", "Digital display", "12 presets", "Preheat function"], "missing_vs_us": ["6L capacity"], "we_lack": ["Preheat function", "More presets"], "notes": "Cheaper, slightly smaller"},
    # ── Beauty competitors ──
    {"our_sku": "BEAU-001", "competitor": "DermaGlow C-Serum", "competitor_brand": "DermaGlow", "marketplace": "amazon", "price": 1299, "rating": 4.5, "features": ["15% Vitamin C", "Ferulic acid", "Vitamin E", "Glass dropper", "6mo shelf life"], "missing_vs_us": ["20% concentration"], "we_lack": ["Ferulic acid", "Longer shelf life"], "notes": "Lower C% but better stability"},
    {"our_sku": "BEAU-003", "competitor": "SunGuard Ultra Matte", "competitor_brand": "SunGuard", "marketplace": "flipkart", "price": 599, "rating": 4.3, "features": ["SPF 50", "Matte finish", "Sweat proof", "80ml"], "missing_vs_us": ["No white cast"], "we_lack": ["Sweat proof", "Matte finish"], "notes": "Cheaper, sweat-proof advantage"},
    # ── Sports competitors ──
    {"our_sku": "SPRT-005", "competitor": "SpeedElite Racer X", "competitor_brand": "SpeedElite", "marketplace": "amazon", "price": 11999, "rating": 4.5, "features": ["Carbon plate", "Pebax foam", "180g", "Wide option"], "missing_vs_us": [], "we_lack": ["Lighter weight", "Wide option"], "notes": "33% premium, race-proven"},
    {"our_sku": "SPRT-009", "competitor": "HydroFlask Standard", "competitor_brand": "HydroFlask", "marketplace": "amazon", "price": 2499, "rating": 4.7, "features": ["24hr cold", "12hr hot", "BPA free", "Wide mouth", "Lifetime warranty"], "missing_vs_us": [], "we_lack": ["Wide mouth", "Lifetime warranty"], "notes": "Almost 2x price, brand premium"},
]


def get_competitors_for_sku(sku: str) -> list[dict]:
    return [c for c in COMPETITORS if c["our_sku"] == sku]

def get_competitors_by_marketplace(marketplace: str) -> list[dict]:
    return [c for c in COMPETITORS if c["marketplace"] == marketplace.lower()]

def get_feature_gaps(sku: str) -> dict:
    comps = get_competitors_for_sku(sku)
    our_advantages = set()
    our_gaps = set()
    for c in comps:
        our_advantages.update(c.get("missing_vs_us", []))
        our_gaps.update(c.get("we_lack", []))
    return {"advantages": list(our_advantages), "gaps": list(our_gaps), "competitor_count": len(comps)}
