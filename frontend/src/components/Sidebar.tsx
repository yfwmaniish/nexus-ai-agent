'use client';

import {
    LayoutDashboard,
    History,
    Settings,
    Database,
    TerminalSquare
} from 'lucide-react';

export default function Sidebar() {
    return (
        <aside className="fixed left-0 top-0 h-screen w-64 glass-panel border-l-0 border-y-0 border-r border-[#ffffff1a] hidden md:flex flex-col z-10">
            <div className="p-6">
                <div className="flex items-center gap-3">
                    <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-[#06B6D4] to-[#10B981] flex items-center justify-center text-white font-bold">
                        <TerminalSquare size={18} />
                    </div>
                    <h1 className="text-xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400">
                        Nexus AI
                    </h1>
                </div>
                <p className="text-xs text-slate-400 mt-2 font-medium tracking-wide">E-COMMERCE INTELLIGENCE</p>
            </div>

            <nav className="flex-1 px-4 py-4 space-y-1">
                <a href="#" className="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-[#ffffff1a] text-white font-medium transition-colors">
                    <LayoutDashboard size={18} className="text-[#06B6D4]" />
                    Research Terminal
                </a>
                {/* 
                <a href="#" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-[#ffffff0a] font-medium transition-colors">
                    <History size={18} />
                    History
                </a>
                <a href="#" className="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-[#ffffff0a] font-medium transition-colors">
                    <Database size={18} />
                    Data Sources
                </a> 
                */}
            </nav>

            <div className="p-4 border-t border-[#ffffff1a]">
                <button className="flex items-center gap-3 px-3 py-2.5 w-full rounded-lg text-slate-400 hover:text-white hover:bg-[#ffffff0a] font-medium transition-colors text-left">
                    <Settings size={18} />
                    Preferences
                </button>
            </div>
        </aside>
    );
}
