'use client';

import { useState } from 'react';
import { Search, Zap, Microscope, Loader2 } from 'lucide-react';
import { ResearchMode } from '@/lib/types';

interface QueryInputProps {
    onSearch: (query: string, mode: ResearchMode) => void;
    isConnecting: boolean;
    isResearching: boolean;
}

export default function QueryInput({ onSearch, isConnecting, isResearching }: QueryInputProps) {
    const [query, setQuery] = useState('');
    const [mode, setMode] = useState<ResearchMode>('quick');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (!query.trim() || isConnecting || isResearching) return;
        onSearch(query, mode);
    };

    const isLoading = isConnecting || isResearching;

    return (
        <div className="w-full max-w-3xl mx-auto glass-panel p-2">
            <form onSubmit={handleSubmit} className="relative flex flex-col md:flex-row gap-2">
                <div className="relative flex-1">
                    <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                        <Search size={18} className="text-slate-400" />
                    </div>
                    <input
                        type="text"
                        className="w-full bg-transparent border-none text-white placeholder-slate-400 py-4 pl-12 pr-4 focus:ring-0 focus:outline-none"
                        placeholder="E.g., What are the main complaints about ANC headphones?"
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        disabled={isLoading}
                    />
                </div>

                <div className="flex items-center gap-2 px-2 pb-2 md:pb-0">
                    <div className="flex bg-[#0f172a80] rounded-lg p-1 border border-[#ffffff1a]">
                        <button
                            type="button"
                            onClick={() => setMode('quick')}
                            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md text-sm font-medium transition-all ${mode === 'quick'
                                    ? 'bg-[#ffffff1a] text-white shadow-sm'
                                    : 'text-slate-400 hover:text-white'
                                }`}
                        >
                            <Zap size={14} className={mode === 'quick' ? 'text-[#06B6D4]' : ''} />
                            Quick
                        </button>
                        <button
                            type="button"
                            onClick={() => setMode('deep')}
                            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md text-sm font-medium transition-all ${mode === 'deep'
                                    ? 'bg-[#ffffff1a] text-white shadow-sm'
                                    : 'text-slate-400 hover:text-white'
                                }`}
                        >
                            <Microscope size={14} className={mode === 'deep' ? 'text-[#10B981]' : ''} />
                            Deep
                        </button>
                    </div>

                    <button
                        type="submit"
                        disabled={!query.trim() || isLoading}
                        className="glass-button bg-gradient-to-r from-[#06B6D4] to-[#10B981] text-white px-6 py-2.5 rounded-lg font-medium flex items-center justify-center min-w-[100px] hover:opacity-90 disabled:opacity-50 border-none"
                    >
                        {isLoading ? <Loader2 size={18} className="animate-spin" /> : 'Analyze'}
                    </button>
                </div>
            </form>
        </div>
    );
}
