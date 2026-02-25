"""Mock customer reviews — ~200 reviews with sentiment, themes, and ratings."""

import random

REVIEWS: list[dict] = [
    # ── ELEC-001 ProSound ANC Headphones ──
    {"sku": "ELEC-001", "rating": 5, "title": "Best ANC at this price", "text": "Incredible noise cancellation for the price. Battery lasts forever. Wearing them on flights is a game changer.", "sentiment": "positive", "themes": ["noise cancellation", "battery", "value"], "verified": True, "date": "2025-08-10"},
    {"sku": "ELEC-001", "rating": 4, "title": "Good but headband pressure", "text": "Sound quality is amazing but after 2 hours the headband creates pressure on top of my head. Wish it was lighter.", "sentiment": "mixed", "themes": ["comfort", "sound quality", "weight"], "verified": True, "date": "2025-09-05"},
    {"sku": "ELEC-001", "rating": 2, "title": "ANC stopped working after 3 months", "text": "Left ear ANC completely died after 3 months. Customer support was unhelpful. Disappointing quality control.", "sentiment": "negative", "themes": ["durability", "quality control", "customer support"], "verified": True, "date": "2025-10-20"},
    {"sku": "ELEC-001", "rating": 4, "title": "Great for work calls", "text": "Microphone is surprisingly clear. Colleagues say I sound better than with my old Jabra. ANC helps in noisy office.", "sentiment": "positive", "themes": ["microphone", "calls", "office use"], "verified": True, "date": "2025-11-01"},
    # ── ELEC-002 ProSound Sport Buds ──
    {"sku": "ELEC-002", "rating": 3, "title": "Falls out during running", "text": "Sound is decent for the price but they keep falling out during intense runs. Ear hooks don't grip well enough.", "sentiment": "negative", "themes": ["fit", "exercise", "stability"], "verified": True, "date": "2025-08-15"},
    {"sku": "ELEC-002", "rating": 5, "title": "Perfect gym companion", "text": "IPX7 rating is legit — washed them under tap after sweaty session. Still working perfectly after 6 months.", "sentiment": "positive", "themes": ["waterproof", "durability", "gym"], "verified": True, "date": "2025-09-20"},
    {"sku": "ELEC-002", "rating": 2, "title": "Bluetooth keeps disconnecting", "text": "Constant Bluetooth drops when phone is in pocket. Very annoying during workouts. Tried resetting multiple times.", "sentiment": "negative", "themes": ["bluetooth", "connectivity", "reliability"], "verified": True, "date": "2025-10-05"},
    # ── ELEC-003 VibeX Smart Speaker ──
    {"sku": "ELEC-003", "rating": 5, "title": "Room-filling sound", "text": "360 audio is no gimmick. Fills my entire living room with rich sound. Voice assistant is responsive.", "sentiment": "positive", "themes": ["sound quality", "voice assistant", "design"], "verified": True, "date": "2025-07-10"},
    {"sku": "ELEC-003", "rating": 4, "title": "Great but limited ecosystem", "text": "Audio quality is premium. However, multi-room is limited to VibeX speakers only. No support for other brands.", "sentiment": "mixed", "themes": ["ecosystem", "compatibility", "multi-room"], "verified": True, "date": "2025-08-25"},
    {"sku": "ELEC-003", "rating": 5, "title": "Best smart speaker under 5K", "text": "Was choosing between this and Amazon Echo. VibeX wins on audio quality hands down. Setup took only 5 minutes.", "sentiment": "positive", "themes": ["value", "audio quality", "setup"], "verified": True, "date": "2025-09-15"},
    # ── ELEC-005 ZenWatch Ultra ──
    {"sku": "ELEC-005", "rating": 4, "title": "Feature-packed but bulky", "text": "Love the features — GPS tracking, SpO2, workout modes. But it's too bulky for people with thin wrists.", "sentiment": "mixed", "themes": ["features", "size", "design"], "verified": True, "date": "2025-06-15"},
    {"sku": "ELEC-005", "rating": 3, "title": "App needs major improvement", "text": "Hardware is solid but the companion app crashes constantly. Sync is unreliable. Hope they fix it.", "sentiment": "negative", "themes": ["app quality", "sync", "software"], "verified": True, "date": "2025-07-20"},
    {"sku": "ELEC-005", "rating": 5, "title": "Replaced my Apple Watch", "text": "Switched from Apple Watch and don't regret it. Battery lasting 6 days vs daily charging is a revelation.", "sentiment": "positive", "themes": ["battery", "value", "switching"], "verified": True, "date": "2025-08-30"},
    # ── ELEC-006 ZenWatch Lite ──
    {"sku": "ELEC-006", "rating": 3, "title": "Screen is dim outdoors", "text": "LCD screen is barely readable in sunlight. For a watch, that's a dealbreaker. Indoor use is fine though.", "sentiment": "negative", "themes": ["display", "outdoor use", "brightness"], "verified": True, "date": "2025-07-05"},
    {"sku": "ELEC-006", "rating": 4, "title": "Perfect basic fitness watch", "text": "Don't need fancy features. This tracks my steps, heart rate, and sleep accurately. 14-day battery is amazing.", "sentiment": "positive", "themes": ["battery", "basic fitness", "accuracy"], "verified": True, "date": "2025-08-10"},
    # ── ELEC-008 ChargePod 65W GaN ──
    {"sku": "ELEC-008", "rating": 5, "title": "Replaced all my chargers", "text": "One tiny charger for my laptop, phone, and earbuds. GaN tech is incredible. Runs barely warm.", "sentiment": "positive", "themes": ["versatility", "compact", "efficiency"], "verified": True, "date": "2025-04-15"},
    {"sku": "ELEC-008", "rating": 5, "title": "Travel essential", "text": "Carry this one charger instead of three. Charges my MacBook at full speed. Build quality is premium.", "sentiment": "positive", "themes": ["travel", "fast charging", "build quality"], "verified": True, "date": "2025-05-20"},
    # ── FASH-001 UrbanStride Retro Sneakers ──
    {"sku": "FASH-001", "rating": 5, "title": "Most complimented shoes", "text": "Get compliments every time I wear these. Retro design is on point. Comfortable for all-day wear.", "sentiment": "positive", "themes": ["design", "comfort", "style"], "verified": True, "date": "2025-05-10"},
    {"sku": "FASH-001", "rating": 3, "title": "Sizing runs small", "text": "Ordered my usual size and they're tight. Had to return and get one size up. Quality is good though.", "sentiment": "mixed", "themes": ["sizing", "fit", "returns"], "verified": True, "date": "2025-06-15"},
    {"sku": "FASH-001", "rating": 4, "title": "Great quality leather", "text": "Leather feels premium. EVA sole provides good cushion. Only wish they had more color options.", "sentiment": "positive", "themes": ["materials", "cushioning", "color options"], "verified": True, "date": "2025-07-20"},
    {"sku": "FASH-001", "rating": 2, "title": "Sole wore out quickly", "text": "After just 2 months of daily wear, the sole is completely flat. Not durable for everyday use. Disappointed.", "sentiment": "negative", "themes": ["durability", "sole", "daily wear"], "verified": True, "date": "2025-08-25"},
    # ── FASH-005 CarryAll Weekender Bag ──
    {"sku": "FASH-005", "rating": 5, "title": "Perfect weekend trip bag", "text": "Fits clothes, laptop, and shoes with room to spare. Canvas is thick and feels like it'll last years.", "sentiment": "positive", "themes": ["capacity", "materials", "durability"], "verified": True, "date": "2025-04-10"},
    {"sku": "FASH-005", "rating": 4, "title": "Heavy when empty", "text": "Love the design and functionality. But the bag itself is quite heavy even when empty due to thick canvas.", "sentiment": "mixed", "themes": ["weight", "design", "materials"], "verified": True, "date": "2025-06-05"},
    # ── HOME-003 CleanBot X1 Robot Vacuum ──
    {"sku": "HOME-003", "rating": 4, "title": "LiDAR mapping is impressive", "text": "Maps the house perfectly. Never gets stuck. Mopping feature works well on hardwood floors.", "sentiment": "positive", "themes": ["navigation", "mapping", "mopping"], "verified": True, "date": "2025-09-10"},
    {"sku": "HOME-003", "rating": 3, "title": "Auto-empty is loud", "text": "Vacuum itself is quiet but the auto-empty base sounds like a jet engine. Wakes up the baby every time.", "sentiment": "negative", "themes": ["noise", "auto-empty", "family use"], "verified": True, "date": "2025-10-05"},
    {"sku": "HOME-003", "rating": 2, "title": "WiFi setup nightmare", "text": "Took 2 hours to connect to WiFi. App crashed repeatedly. Once connected it works fine but initial setup is terrible.", "sentiment": "negative", "themes": ["setup", "app quality", "wifi"], "verified": True, "date": "2025-10-20"},
    # ── HOME-004 CleanBot Mini ──
    {"sku": "HOME-004", "rating": 3, "title": "Gets stuck under furniture", "text": "Slim design is nice but the gyroscope navigation keeps getting it stuck under my sofa and bed.", "sentiment": "negative", "themes": ["navigation", "getting stuck", "intelligence"], "verified": True, "date": "2025-10-15"},
    {"sku": "HOME-004", "rating": 4, "title": "Great for small apartments", "text": "Perfect for my 1BHK. 90 minutes is enough for the whole apartment. Voice control with Alexa works well.", "sentiment": "positive", "themes": ["small space", "battery", "voice control"], "verified": True, "date": "2025-11-01"},
    # ── HOME-005 PureAir 360 Purifier ──
    {"sku": "HOME-005", "rating": 5, "title": "Saved us during pollution season", "text": "AQI dropped from 250+ to under 50 within 30 minutes. PM2.5 sensor is accurate. Worth every penny during winters.", "sentiment": "positive", "themes": ["effectiveness", "air quality", "sensor accuracy"], "verified": True, "date": "2025-12-01"},
    {"sku": "HOME-005", "rating": 4, "title": "Filter replacement is expensive", "text": "Works great but replacement HEPA filters cost ₹3,000. That's almost 25% of the unit price every 6 months.", "sentiment": "mixed", "themes": ["running cost", "filter cost", "maintenance"], "verified": True, "date": "2025-12-15"},
    # ── HOME-009 ChefPro Air Fryer ──
    {"sku": "HOME-009", "rating": 5, "title": "Life-changing kitchen gadget", "text": "Made crispy fries, chicken wings, and even baked a cake! Digital display is intuitive. Easy to clean.", "sentiment": "positive", "themes": ["versatility", "ease of use", "cleaning"], "verified": True, "date": "2025-07-20"},
    {"sku": "HOME-009", "rating": 4, "title": "Takes up counter space", "text": "6L is great for family cooking but this thing is huge. Takes up half my kitchen counter. Performance is excellent.", "sentiment": "mixed", "themes": ["size", "counter space", "performance"], "verified": True, "date": "2025-08-15"},
    {"sku": "HOME-009", "rating": 5, "title": "Healthier eating made easy", "text": "Oil-free cooking that actually tastes good. My kids love the air fried chicken nuggets. Great investment.", "sentiment": "positive", "themes": ["healthy cooking", "family", "taste"], "verified": True, "date": "2025-09-10"},
    # ── BEAU-001 GlowUp Vitamin C Serum ──
    {"sku": "BEAU-001", "rating": 5, "title": "Visible results in 2 weeks", "text": "Dark spots started fading after just 2 weeks. Skin feels brighter and smoother. Best serum I've tried.", "sentiment": "positive", "themes": ["results", "dark spots", "brightness"], "verified": True, "date": "2025-04-10"},
    {"sku": "BEAU-001", "rating": 4, "title": "Good but oxidizes fast", "text": "Works well initially but the serum turns orange within 2 months even when stored in fridge. Shelf life is short.", "sentiment": "mixed", "themes": ["shelf life", "oxidation", "storage"], "verified": True, "date": "2025-06-15"},
    {"sku": "BEAU-001", "rating": 3, "title": "Caused breakouts", "text": "My skin broke out badly after using this for a week. Might not be suitable for sensitive/acne-prone skin.", "sentiment": "negative", "themes": ["breakouts", "sensitive skin", "reaction"], "verified": True, "date": "2025-07-20"},
    {"sku": "BEAU-001", "rating": 5, "title": "Holy grail product", "text": "On my 4th bottle. Nothing else gives this glow. The niacinamide combo is perfect. Affordable luxury.", "sentiment": "positive", "themes": ["repurchase", "glow", "value"], "verified": True, "date": "2025-08-25"},
    # ── BEAU-003 GlowUp SPF 50 Sunscreen ──
    {"sku": "BEAU-003", "rating": 5, "title": "Finally no white cast!", "text": "Works on my dark skin without leaving any white cast. Lightweight and doesn't feel greasy. Game changer.", "sentiment": "positive", "themes": ["no white cast", "inclusivity", "texture"], "verified": True, "date": "2025-05-10"},
    {"sku": "BEAU-003", "rating": 5, "title": "Best sunscreen under ₹1000", "text": "SPF 50 protection that feels like a moisturizer. Wears well under makeup. Reapplication doesn't pill.", "sentiment": "positive", "themes": ["protection", "under makeup", "reapplication"], "verified": True, "date": "2025-06-15"},
    {"sku": "BEAU-003", "rating": 4, "title": "Sweats off easily", "text": "Great for indoor use but sweats off within an hour of outdoor activity. Not ideal for sports or beach.", "sentiment": "mixed", "themes": ["sweat resistance", "outdoor use", "durability"], "verified": True, "date": "2025-08-20"},
    # ── BEAU-006 ScentLab Oud Intense ──
    {"sku": "BEAU-006", "rating": 5, "title": "Compliment magnet", "text": "Every time I wear this, at least 3 people ask what perfume I'm wearing. Lasts easily 8+ hours. Worth the price.", "sentiment": "positive", "themes": ["compliments", "longevity", "projection"], "verified": True, "date": "2025-09-10"},
    {"sku": "BEAU-006", "rating": 3, "title": "Too strong for daily use", "text": "Gorgeous scent but way too overpowering for office. Colleagues complained. Only suitable for evening/special occasions.", "sentiment": "mixed", "themes": ["strength", "office use", "occasion"], "verified": True, "date": "2025-10-15"},
    # ── SPRT-001 FlexFit Pro Yoga Mat ──
    {"sku": "SPRT-001", "rating": 5, "title": "Non-slip is legit", "text": "Did hot yoga on this mat and didn't slip once. Alignment lines help with pose positioning. Best mat I've owned.", "sentiment": "positive", "themes": ["non-slip", "hot yoga", "alignment"], "verified": True, "date": "2025-04-10"},
    {"sku": "SPRT-001", "rating": 4, "title": "Slight rubber smell initially", "text": "Strong rubber smell for the first week. After airing out, it's fine. Great grip and thickness.", "sentiment": "mixed", "themes": ["smell", "breaking in", "grip"], "verified": True, "date": "2025-05-15"},
    # ── SPRT-005 RunX Carbon Racer ──
    {"sku": "SPRT-005", "rating": 5, "title": "Shaved 3 minutes off my 10K", "text": "The carbon plate makes a noticeable difference. Feels like running on springs. Ran my best 10K ever.", "sentiment": "positive", "themes": ["performance", "carbon plate", "speed"], "verified": True, "date": "2025-07-10"},
    {"sku": "SPRT-005", "rating": 4, "title": "Not for daily training", "text": "Amazing for race day but the foam wears out after ~300km. Too expensive for daily training. Race-only shoe.", "sentiment": "mixed", "themes": ["durability", "race shoe", "value"], "verified": True, "date": "2025-08-20"},
    {"sku": "SPRT-005", "rating": 3, "title": "Narrow fit hurts", "text": "Race fit is way too narrow for my wide feet. Had to return. Wish they offered wide options.", "sentiment": "negative", "themes": ["fit", "wide feet", "sizing"], "verified": True, "date": "2025-09-15"},
    # ── SPRT-009 HydroPure Insulated Bottle ──
    {"sku": "SPRT-009", "rating": 5, "title": "Keeps water ice cold", "text": "Left ice water in the morning, still cold 24 hours later. No condensation on outside. Build quality is excellent.", "sentiment": "positive", "themes": ["insulation", "build quality", "no condensation"], "verified": True, "date": "2025-03-10"},
    {"sku": "SPRT-009", "rating": 4, "title": "Hard to clean inside", "text": "Narrow mouth makes it hard to clean properly. Had to buy a bottle brush. Otherwise perfect water bottle.", "sentiment": "mixed", "themes": ["cleaning", "mouth size", "maintenance"], "verified": True, "date": "2025-05-20"},
    # ── Additional diverse reviews for broader coverage ──
    {"sku": "ELEC-004", "rating": 5, "title": "Cinema sound at home", "text": "Dolby Atmos on this soundbar is incredible. The subwoofer adds deep bass. Replaced my 5.1 system.", "sentiment": "positive", "themes": ["dolby atmos", "bass", "home theater"], "verified": True, "date": "2025-03-15"},
    {"sku": "ELEC-004", "rating": 4, "title": "HDMI eARC issues with older TVs", "text": "Works perfectly with my new LG TV but had compatibility issues with older Samsung. Check TV specs first.", "sentiment": "mixed", "themes": ["compatibility", "HDMI", "setup"], "verified": True, "date": "2025-05-20"},
    {"sku": "FASH-002", "rating": 5, "title": "Best running shoes I own", "text": "Carbon plate gives incredible energy return. Gel cushion protects my knees on long runs. Worth every rupee.", "sentiment": "positive", "themes": ["performance", "cushioning", "value"], "verified": True, "date": "2025-06-30"},
    {"sku": "FASH-003", "rating": 4, "title": "Perfect for Indian winters", "text": "Water resistant kept me dry in Mumbai rain. Fleece lining is warm enough for Delhi winters too.", "sentiment": "positive", "themes": ["weather protection", "warmth", "versatility"], "verified": True, "date": "2025-11-20"},
    {"sku": "HOME-007", "rating": 5, "title": "Saves money on electricity", "text": "Can see exactly which appliances use most power. Reduced my electricity bill by 15% just by scheduling.", "sentiment": "positive", "themes": ["energy savings", "monitoring", "scheduling"], "verified": True, "date": "2025-04-15"},
    {"sku": "BEAU-004", "rating": 3, "title": "Didn't reduce frizz", "text": "Used for 4 weeks as directed. No noticeable difference in frizz. Hair feels slightly softer but that's it.", "sentiment": "negative", "themes": ["effectiveness", "frizz", "expectations"], "verified": True, "date": "2025-07-10"},
    {"sku": "BEAU-005", "rating": 4, "title": "Ionic tech really works", "text": "Hair dries 30% faster with less frizz compared to my old dryer. Foldable design great for travel.", "sentiment": "positive", "themes": ["drying speed", "frizz reduction", "portability"], "verified": True, "date": "2025-08-20"},
    {"sku": "SPRT-003", "rating": 4, "title": "GPS accuracy is solid", "text": "Tracked my trail runs accurately even under tree cover. Heart rate sensor matches my chest strap readings.", "sentiment": "positive", "themes": ["GPS accuracy", "heart rate", "trail running"], "verified": True, "date": "2025-06-15"},
    {"sku": "SPRT-007", "rating": 5, "title": "Replaced entire dumbbell rack", "text": "One pair replaces 12 dumbbells. Quick adjust mechanism works smoothly. Saved so much space in my home gym.", "sentiment": "positive", "themes": ["space saving", "convenience", "home gym"], "verified": True, "date": "2025-09-10"},
    {"sku": "SPRT-010", "rating": 4, "title": "Great for recovery", "text": "Helps with muscle soreness after heavy leg days. Quiet enough to use while watching TV. Good battery life.", "sentiment": "positive", "themes": ["recovery", "noise level", "battery"], "verified": True, "date": "2025-07-20"},
    {"sku": "FASH-006", "rating": 4, "title": "Compact but fits a lot", "text": "Fits phone, wallet, keys, sunglasses, and a small water bottle. Anti-theft zip gives peace of mind in crowded areas.", "sentiment": "positive", "themes": ["capacity", "security", "daily use"], "verified": True, "date": "2025-08-10"},
    {"sku": "HOME-002", "rating": 4, "title": "Consistent grind quality", "text": "Burr grinder produces uniform grounds. 20 settings let me dial in for pour-over vs French press. Timer is handy.", "sentiment": "positive", "themes": ["grind quality", "versatility", "features"], "verified": True, "date": "2025-06-01"},
]


def get_reviews_by_sku(sku: str) -> list[dict]:
    return [r for r in REVIEWS if r["sku"] == sku]

def get_reviews_by_sentiment(sentiment: str) -> list[dict]:
    return [r for r in REVIEWS if r["sentiment"] == sentiment.lower()]

def get_reviews_by_theme(theme: str) -> list[dict]:
    t = theme.lower()
    return [r for r in REVIEWS if any(t in th.lower() for th in r.get("themes", []))]

def search_reviews(query: str) -> list[dict]:
    q = query.lower()
    return [r for r in REVIEWS if q in r["text"].lower() or q in r["title"].lower()
            or any(q in th.lower() for th in r.get("themes", []))]
