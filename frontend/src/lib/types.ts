export type ResearchMode = 'quick' | 'deep';

export type QueryType =
    | 'sentiment'
    | 'pricing'
    | 'competitor'
    | 'performance'
    | 'demand'
    | 'feature_gap'
    | 'general';

export type ResearchStatus =
    | 'pending'
    | 'analyzing_query'
    | 'retrieving_data'
    | 'researching'
    | 'generating_report'
    | 'complete'
    | 'error';

export interface Finding {
    title: string;
    detail: string;
    evidence: string[];
    confidence: number;
    sentiment?: 'positive' | 'negative' | 'neutral' | 'mixed';
}

export interface ChartSpec {
    chart_type: 'bar' | 'line' | 'donut' | 'gauge' | 'grouped_bar';
    title: string;
    data: any[];
    x_key: string;
    y_keys: string[];
    colors: string[];
}

export interface ResearchReport {
    id: string;
    query: string;
    mode: ResearchMode;
    query_type: QueryType;
    status: ResearchStatus;
    executive_summary: string;
    findings: Finding[];
    recommendations: string[];
    charts: ChartSpec[];
    confidence_score: number;
    uncertainty_notes: string[];
    tokens_used: number;
    cost_usd: number;
    duration_seconds: number;
    created_at: string;
}

export interface ResearchProgress {
    research_id: string;
    status: ResearchStatus;
    step_label: string;
    step_detail: string;
    progress_pct: number;
}

export interface MemoryState {
    preferred_kpis: string[];
    preferred_marketplaces: string[];
    preferred_categories: string[];
    custom_context: string;
    past_queries: string[];
    learned_preferences: Record<string, any>;
}
