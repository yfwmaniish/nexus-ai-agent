import { MemoryState, ResearchReport, ResearchMode } from './types';

const API_BASE = 'http://localhost:8000/api';

export class ApiClient {
    static async getPreferences(): Promise<MemoryState> {
        const res = await fetch(`${API_BASE}/memory/preferences`);
        if (!res.ok) throw new Error('Failed to fetch preferences');
        return res.json();
    }

    static async updatePreferences(data: Partial<MemoryState>): Promise<MemoryState> {
        const res = await fetch(`${API_BASE}/memory/preferences`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
        });
        if (!res.ok) throw new Error('Failed to update preferences');
        return res.json();
    }

    static async getHistory(): Promise<Partial<ResearchReport>[]> {
        const res = await fetch(`${API_BASE}/research/history`);
        if (!res.ok) throw new Error('Failed to fetch history');
        return res.json();
    }

    static async getReport(id: string): Promise<ResearchReport> {
        const res = await fetch(`${API_BASE}/research/${id}`);
        if (!res.ok) throw new Error('Failed to fetch report');
        return res.json();
    }

    // Non-streaming fallback
    static async startResearchSync(query: string, mode: ResearchMode = 'quick'): Promise<ResearchReport> {
        const res = await fetch(`${API_BASE}/research`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query, mode }),
        });
        if (!res.ok) throw new Error('Research failed');
        return res.json();
    }
}
