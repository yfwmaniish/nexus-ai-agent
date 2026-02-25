'use client';

import { ResearchProgress } from '@/lib/types';
import { Loader2, CheckCircle2, Search, Brain, BarChart3, Database } from 'lucide-react';

export default function ProgressDisplay({ progress }: { progress: ResearchProgress }) {
    // Determine an icon based on the status phase
    const getIcon = () => {
        switch (progress.status) {
            case 'analyzing_query': return <Brain className="text-[#06B6D4]" size={24} />;
            case 'retrieving_data': return <Database className="text-[#10B981]" size={24} />;
            case 'researching': return <Search className="text-purple-400" size={24} />;
            case 'generating_report': return <BarChart3 className="text-orange-400" size={24} />;
            case 'complete': return <CheckCircle2 className="text-green-500" size={24} />;
            default: return <Loader2 className="text-slate-400 animate-spin" size={24} />;
        }
    };

    return (
        <div className="w-full max-w-3xl mx-auto mt-8 glass-panel p-8 flex flex-col items-center justify-center min-h-[300px] text-center">
            <div className="relative mb-6">
                <div className="absolute inset-0 bg-gradient-to-tr from-[#06B6D4] to-[#10B981] blur-xl opacity-30 rounded-full w-16 h-16 animate-pulse"></div>
                <div className="relative w-16 h-16 bg-[#0f172a] rounded-full border border-[#ffffff1a] flex items-center justify-center z-10">
                    {getIcon()}
                </div>
            </div>

            <h3 className="text-xl font-bold text-white mb-2">{progress.step_label}</h3>
            <p className="text-slate-400 max-w-md">{progress.step_detail}</p>

            <div className="w-full max-w-sm mt-8 bg-[#0f172a] rounded-full h-2 border border-[#ffffff1a] overflow-hidden">
                <div
                    className="bg-gradient-to-r from-[#06B6D4] to-[#10B981] h-full transition-all duration-500 ease-out"
                    style={{ width: `${progress.progress_pct}%` }}
                ></div>
            </div>
            <div className="mt-2 text-xs text-slate-500 font-mono">{progress.progress_pct}% Complete</div>
        </div>
    );
}
