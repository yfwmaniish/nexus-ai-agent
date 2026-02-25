import { useState, useCallback, useRef, useEffect } from 'react';
import { ResearchProgress, ResearchReport, ResearchMode } from './types';

const WS_BASE = 'ws://localhost:8000/api/research/ws';

export function useResearchStream() {
    const [isConnecting, setIsConnecting] = useState(false);
    const [progress, setProgress] = useState<ResearchProgress | null>(null);
    const [report, setReport] = useState<ResearchReport | null>(null);
    const [error, setError] = useState<string | null>(null);
    const wsRef = useRef<WebSocket | null>(null);

    const startResearch = useCallback((query: string, mode: ResearchMode = 'quick') => {
        setIsConnecting(true);
        setProgress(null);
        setReport(null);
        setError(null);

        // Generate a temporary session ID for this request
        const sessionId = Math.random().toString(36).substring(2, 12);
        const ws = new WebSocket(`${WS_BASE}/${sessionId}`);
        wsRef.current = ws;

        ws.onopen = () => {
            setIsConnecting(false);
            // Send the request payload as soon as connected
            ws.send(JSON.stringify({ query, mode }));
            setProgress({
                research_id: sessionId,
                status: 'pending',
                step_label: 'Connecting',
                step_detail: 'Establishing secure link to research engine...',
                progress_pct: 0
            });
        };

        ws.onmessage = (event) => {
            try {
                const payload = JSON.parse(event.data);
                if (payload.type === 'progress') {
                    setProgress(payload.data as ResearchProgress);
                } else if (payload.type === 'report') {
                    setReport(payload.data as ResearchReport);
                    ws.close();
                } else if (payload.type === 'error') {
                    setError(payload.message || 'Unknown stream error');
                    ws.close();
                }
            } catch (err) {
                console.error('Failed to parse WebSocket message:', event.data);
            }
        };

        ws.onerror = () => {
            setError('Connection failed. Is the backend running?');
            setIsConnecting(false);
        };

        ws.onclose = () => {
            setIsConnecting(false);
        };
    }, []);

    // Cleanup on unmount
    useEffect(() => {
        return () => {
            if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
                wsRef.current.close();
            }
        };
    }, []);

    return {
        startResearch,
        isConnecting,
        isResearching: !!progress && !report && !error,
        progress,
        report,
        error,
        reset: () => {
            setProgress(null);
            setReport(null);
            setError(null);
        }
    };
}
