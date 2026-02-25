'use client';

import Sidebar from '@/components/Sidebar';
import QueryInput from '@/components/QueryInput';
import ProgressDisplay from '@/components/ProgressDisplay';
import ReportViewer from '@/components/ReportViewer';
import { useResearchStream } from '@/lib/websocket';

export default function Home() {
  const {
    startResearch,
    isConnecting,
    isResearching,
    progress,
    report,
    error
  } = useResearchStream();

  return (
    <div className="min-h-screen bg-[#0F172A] selection:bg-[#06B6D4]/30 selection:text-white flex">
      {/* Background Gradients */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none z-0">
        <div className="absolute -top-[20%] -left-[10%] w-[50%] h-[50%] rounded-full bg-[#06B6D4] blur-[150px] opacity-10 mix-blend-screen"></div>
        <div className="absolute top-[60%] -right-[10%] w-[40%] h-[50%] rounded-full bg-[#10B981] blur-[150px] opacity-10 mix-blend-screen"></div>
        <div className="absolute top-[20%] left-[60%] w-[30%] h-[30%] rounded-full bg-[#3B82F6] blur-[120px] opacity-5 mix-blend-screen"></div>
      </div>

      {/* Sidebar - hidden on mobile */}
      <Sidebar />

      {/* Main Content Area */}
      <main className="flex-1 md:ml-64 relative z-10 h-screen overflow-y-auto overflow-x-hidden scroll-smooth">

        {/* Top Header */}
        <header className="sticky top-0 z-20 backdrop-blur-md bg-[#0F172A]/80 border-b border-[#ffffff1a] px-6 py-4 flex justify-between items-center">
          <h1 className="text-lg font-medium text-white md:hidden">Nexus AI</h1>
          <div className="hidden md:flex flex-col">
            <h2 className="text-white font-medium">Research Workspace</h2>
            <p className="text-xs text-slate-400">Generate insights from connected data sources</p>
          </div>
          <div className="flex items-center gap-3">
            <span className="flex h-3 w-3 relative">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
            </span>
            <span className="text-xs font-mono text-slate-400">SYS.ONLINE</span>
          </div>
        </header>

        {/* Content Container */}
        <div className="px-4 md:px-8 pt-8 pb-32 max-w-7xl mx-auto flex flex-col items-center">

          {/* Welcome State (when no active research or report) */}
          {!progress && !report && (
            <div className="w-full max-w-3xl mt-12 mb-16 text-center animate-in fade-in slide-in-from-bottom-4 duration-700">
              <h1 className="text-4xl md:text-5xl font-bold text-white mb-6 tracking-tight">
                Ask Questions. <br className="md:hidden" /> <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#06B6D4] to-[#10B981]">Get Intelligence.</span>
              </h1>
              <p className="text-slate-400 text-lg md:text-xl max-w-2xl mx-auto font-light leading-relaxed mb-10">
                AI-powered research engine for e-commerce. Instantly analyze reviews, competitor pricing, and market demand across thousands of data points.
              </p>
            </div>
          )}

          {/* Error Banner */}
          {error && (
            <div className="w-full max-w-3xl glass-panel border-red-500/30 bg-red-500/10 p-4 mb-6 rounded-lg text-red-200 text-sm flex items-center gap-3">
              <div className="h-2 w-2 rounded-full bg-red-400"></div>
              {error}
            </div>
          )}

          {/* Search Bar - anchors to top if report exists, otherwise centered */}
          <div className={`w-full transition-all duration-700 ease-in-out ${(progress || report) ? 'mb-8 sticky top-[88px] z-30' : 'transform-none'
            }`}>
            <QueryInput
              onSearch={startResearch}
              isConnecting={isConnecting}
              isResearching={isResearching}
            />
          </div>

          {/* Active Research Progress */}
          {isResearching && progress && (
            <ProgressDisplay progress={progress} />
          )}

          {/* Final Report */}
          {report && !isResearching && (
            <div className="w-full mt-4">
              <div className="flex w-full justify-center mb-8">
                <div className="h-px bg-gradient-to-r from-transparent via-[#ffffff2a] to-transparent w-full max-w-md"></div>
              </div>
              <ReportViewer report={report} />
            </div>
          )}

        </div>
      </main>
    </div>
  );
}
