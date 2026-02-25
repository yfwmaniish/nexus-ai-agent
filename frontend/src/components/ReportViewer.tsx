'use client';

import { ResearchReport, ChartSpec } from '@/lib/types';
import {
    BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend
} from 'recharts';
import { Target, Lightbulb, AlertTriangle, ShieldCheck } from 'lucide-react';

export default function ReportViewer({ report }: { report: ResearchReport }) {
    if (!report) return null;

    return (
        <div className="w-full max-w-5xl mx-auto space-y-6 pb-20 animate-in fade-in slide-in-from-bottom-4 duration-500">

            {/* Meta Header */}
            <div className="flex flex-wrap items-center justify-between text-sm text-slate-400 mb-2">
                <div className="flex gap-4">
                    <span className="bg-[#0f172a] border border-[#ffffff1a] px-2 py-1 rounded">
                        ID: {report.id}
                    </span>
                    <span className="flex items-center gap-1">
                        <ShieldCheck size={14} className="text-green-400" />
                        Confidence: {(report.confidence_score * 100).toFixed(0)}%
                    </span>
                </div>
                <div className="flex gap-4">
                    <span>{report.duration_seconds}s latency</span>
                    <span>{report.tokens_used.toLocaleString()} tokens</span>
                </div>
            </div>

            {/* Executive Summary */}
            <div className="glass-panel p-6 relative overflow-hidden">
                <div className="absolute top-0 left-0 w-1 h-full bg-gradient-to-b from-[#06B6D4] to-[#10B981]"></div>
                <h2 className="text-xl font-semibold text-white mb-3 flex items-center gap-2">
                    <Target size={20} className="text-[#06B6D4]" />
                    Executive Summary
                </h2>
                <p className="text-slate-300 leading-relaxed text-lg">
                    {report.executive_summary}
                </p>
            </div>

            {/* Charts Grid */}
            {report.charts && report.charts.length > 0 && (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {report.charts.map((chart, idx) => (
                        <ChartRenderer key={idx} spec={chart} />
                    ))}
                </div>
            )}

            {/* Findings */}
            <div className="space-y-4">
                <h2 className="text-xl font-semibold text-white mt-8 mb-4">Key Findings</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {report.findings.map((f, i) => (
                        <div key={i} className="glass-panel p-5 hover:border-[#06B6D4] transition-colors border border-[#ffffff1a] group flex flex-col h-full">
                            <div className="flex justify-between items-start mb-3">
                                <h3 className="text-lg font-medium text-white group-hover:text-[#06B6D4] transition-colors line-clamp-2">
                                    {f.title}
                                </h3>
                                {f.sentiment && (
                                    <span className={`text-[10px] uppercase font-bold px-2 py-1 rounded-full border ${f.sentiment === 'positive' ? 'text-green-400 border-green-400/30 bg-green-400/10' :
                                            f.sentiment === 'negative' ? 'text-red-400 border-red-400/30 bg-red-400/10' :
                                                f.sentiment === 'mixed' ? 'text-yellow-400 border-yellow-400/30 bg-yellow-400/10' :
                                                    'text-slate-400 border-slate-400/30 bg-slate-400/10'
                                        }`}>
                                        {f.sentiment}
                                    </span>
                                )}
                            </div>
                            <p className="text-sm text-slate-300 mb-4 flex-grow">{f.detail}</p>

                            {f.evidence && f.evidence.length > 0 && (
                                <div className="mt-auto pt-3 border-t border-[#ffffff1a]">
                                    <p className="text-xs text-slate-500 font-medium mb-1">EVIDENCE</p>
                                    <ul className="list-disc pl-4 space-y-1">
                                        {f.evidence.map((ev, eIdx) => (
                                            <li key={eIdx} className="text-xs text-slate-400">{ev}</li>
                                        ))}
                                    </ul>
                                </div>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            {/* Recommendations & Notes */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6 pt-6">
                <div className="md:col-span-2 glass-panel p-6 bg-gradient-to-br from-[#0f172a] to-[#1e293b]">
                    <h2 className="text-xl font-semibold text-white mb-4 flex items-center gap-2">
                        <Lightbulb size={20} className="text-[#10B981]" />
                        Actionable Recommendations
                    </h2>
                    <ul className="space-y-3">
                        {report.recommendations.map((rec, idx) => (
                            <li key={idx} className="flex items-start gap-3">
                                <span className="flex-shrink-0 w-6 h-6 rounded-full bg-[#10B981]/20 text-[#10B981] flex items-center justify-center text-xs font-bold mt-0.5">
                                    {idx + 1}
                                </span>
                                <p className="text-slate-300">{rec}</p>
                            </li>
                        ))}
                    </ul>
                </div>

                {report.uncertainty_notes && report.uncertainty_notes.length > 0 && (
                    <div className="glass-panel p-6 border-l-[3px] border-l-orange-500">
                        <h2 className="text-lg font-semibold text-white mb-3 flex items-center gap-2">
                            <AlertTriangle size={18} className="text-orange-500" />
                            Uncertainties
                        </h2>
                        <ul className="space-y-2">
                            {report.uncertainty_notes.map((note, idx) => (
                                <li key={idx} className="text-sm text-slate-400 flex items-start gap-2">
                                    <span className="text-orange-500">•</span>
                                    <span>{note}</span>
                                </li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>

        </div>
    );
}

// ── Internal Chart Component ──────────────────────────────

function ChartRenderer({ spec }: { spec: ChartSpec }) {
    if (!spec.data || spec.data.length === 0) return null;

    return (
        <div className="glass-panel p-5 border border-[#ffffff1a]">
            <h3 className="text-sm font-semibold text-white mb-4 tracking-wide">{spec.title.toUpperCase()}</h3>
            <div className="h-[250px] w-full">
                <ResponsiveContainer width="100%" height="100%">
                    {spec.chart_type === 'line' ? (
                        <LineChart data={spec.data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
                            <XAxis dataKey={spec.x_key} stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} />
                            <YAxis stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} />
                            <Tooltip
                                contentStyle={{ backgroundColor: 'rgba(15,23,42,0.9)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px' }}
                                itemStyle={{ color: '#fff' }}
                            />
                            <Legend wrapperStyle={{ fontSize: '12px' }} />
                            {spec.y_keys.map((key, i) => (
                                <Line
                                    key={key}
                                    type="monotone"
                                    dataKey={key}
                                    stroke={spec.colors[i % spec.colors.length]}
                                    strokeWidth={2}
                                    dot={{ r: 3, fill: '#0f172a' }}
                                    activeDot={{ r: 5 }}
                                />
                            ))}
                        </LineChart>
                    ) : (
                        <BarChart data={spec.data} margin={{ top: 5, right: 20, bottom: 5, left: 0 }}>
                            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" vertical={false} />
                            <XAxis dataKey={spec.x_key} stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} />
                            <YAxis stroke="#64748b" fontSize={11} tickLine={false} axisLine={false} />
                            <Tooltip
                                cursor={{ fill: 'rgba(255,255,255,0.05)' }}
                                contentStyle={{ backgroundColor: 'rgba(15,23,42,0.9)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '8px' }}
                            />
                            <Legend wrapperStyle={{ fontSize: '12px' }} />
                            {spec.y_keys.map((key, i) => (
                                <Bar
                                    key={key}
                                    dataKey={key}
                                    fill={spec.colors[i % spec.colors.length]}
                                    radius={[4, 4, 0, 0]}
                                    maxBarSize={50}
                                />
                            ))}
                        </BarChart>
                    )}
                </ResponsiveContainer>
            </div>
        </div>
    );
}
