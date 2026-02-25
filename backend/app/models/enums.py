"""Domain enumerations for the research agent pipeline."""

from enum import Enum


class ResearchMode(str, Enum):
    QUICK = "quick"
    DEEP = "deep"


class QueryType(str, Enum):
    SENTIMENT = "sentiment"
    PRICING = "pricing"
    COMPETITOR = "competitor"
    PERFORMANCE = "performance"
    DEMAND = "demand"
    FEATURE_GAP = "feature_gap"
    GENERAL = "general"


class ResearchStatus(str, Enum):
    PENDING = "pending"
    ANALYZING_QUERY = "analyzing_query"
    RETRIEVING_DATA = "retrieving_data"
    RESEARCHING = "researching"
    GENERATING_REPORT = "generating_report"
    COMPLETE = "complete"
    ERROR = "error"


class Marketplace(str, Enum):
    AMAZON = "amazon"
    FLIPKART = "flipkart"
    SHOPIFY = "shopify"
    D2C = "d2c"


class ProductCategory(str, Enum):
    ELECTRONICS = "electronics"
    FASHION = "fashion"
    HOME = "home"
    BEAUTY = "beauty"
    SPORTS = "sports"
