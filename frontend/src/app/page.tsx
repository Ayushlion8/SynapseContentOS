"use client"

import { useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import { mockChannels, mockTrends, mockAgents, mockFeedbackSignals, mockDashboardStats } from "@/lib/mock-data"
import { formatNumber, getScoreColor, getGlowClass } from "@/lib/utils"
import {
  Activity, Zap, TrendingUp, Eye, Brain, Cpu, Radio, BarChart3,
  Layers, GitBranch, Play, AlertTriangle, CheckCircle2, ArrowUpRight,
  ArrowDownRight, Sparkles, Clock, Target, Flame, Shield, MessageSquare,
  Volume2, Clapperboard, Image, Calendar, Database, Globe, Bot,
  ChevronRight, Wifi, RadioTower, Search, Lightbulb
} from "lucide-react"

const AGENT_ICONS: Record<string, React.ReactNode> = {
  trend_hunter: <Search size={14} />,
  competitor_intel: <Eye size={14} />,
  hook_generator: <Zap size={14} />,
  script_writer: <MessageSquare size={14} />,
  viral_analyzer: <Flame size={14} />,
  voiceover: <Volume2 size={14} />,
  scene_planner: <Clapperboard size={14} />,
  video_generator: <Play size={14} />,
  thumbnail_optimizer: <Image size={14} />,
  caption_generator: <MessageSquare size={14} />,
  posting_scheduler: <Calendar size={14} />,
  analytics_feedback: <Brain size={14} />,
  content_memory: <Database size={14} />,
  brand_consistency: <Shield size={14} />,
}

const PIPELINE_STAGES = [
  { name: "Trend Discovery", agents: ["trend_hunter", "competitor_intel", "content_memory"], color: "cyan" },
  { name: "Content Strategy", agents: ["analytics_feedback", "viral_analyzer"], color: "purple" },
  { name: "Creative Generation", agents: ["hook_generator", "script_writer"], color: "blue" },
  { name: "Production", agents: ["scene_planner", "voiceover", "brand_consistency"], color: "emerald" },
  { name: "Video Assembly", agents: ["video_generator", "thumbnail_optimizer"], color: "amber" },
  { name: "Publishing", agents: ["caption_generator", "posting_scheduler"], color: "rose" },
]

const STAGE_COLORS: Record<string, string> = {
  cyan: "from-cyan-500/20 to-cyan-600/5 border-cyan-500/30",
  purple: "from-purple-500/20 to-purple-600/5 border-purple-500/30",
  blue: "from-blue-500/20 to-blue-600/5 border-blue-500/30",
  emerald: "from-emerald-500/20 to-emerald-600/5 border-emerald-500/30",
  amber: "from-amber-500/20 to-amber-600/5 border-amber-500/30",
  rose: "from-rose-500/20 to-rose-600/5 border-rose-500/30",
}

const STAGE_BORDER: Record<string, string> = {
  cyan: "border-cyan-500/30", purple: "border-purple-500/30", blue: "border-blue-500/30",
  emerald: "border-emerald-500/30", amber: "border-amber-500/30", rose: "border-rose-500/30",
}

const STAGE_TEXT: Record<string, string> = {
  cyan: "text-cyan-400", purple: "text-purple-400", blue: "text-blue-400",
  emerald: "text-emerald-400", amber: "text-amber-400", rose: "text-rose-400",
}

const STAGE_DOT: Record<string, string> = {
  cyan: "bg-cyan-400", purple: "bg-purple-400", blue: "bg-blue-400",
  emerald: "bg-emerald-400", amber: "bg-amber-400", rose: "bg-rose-400",
}

export default function CommandCenter() {
  const [activeSection, setActiveSection] = useState("overview")

  return (
    <div className="flex h-screen overflow-hidden">
      {/* Sidebar */}
      <Sidebar activeSection={activeSection} onSelect={setActiveSection} />

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto p-4 space-y-4">
        <AnimatePresence mode="wait">
          {activeSection === "overview" && <OverviewSection key="overview" />}
          {activeSection === "channels" && <ChannelsSection key="channels" />}
          {activeSection === "agents" && <AgentsSection key="agents" />}
          {activeSection === "pipeline" && <PipelineSection key="pipeline" />}
          {activeSection === "trends" && <TrendsSection key="trends" />}
          {activeSection === "knowledge" && <KnowledgeSection key="knowledge" />}
          {activeSection === "feedback" && <FeedbackSection key="feedback" />}
        </AnimatePresence>
      </main>
    </div>
  )
}

function Sidebar({ activeSection, onSelect }: { activeSection: string; onSelect: (s: string) => void }) {
  const items = [
    { id: "overview", label: "Command Center", icon: <Cpu size={18} /> },
    { id: "channels", label: "Channels", icon: <Layers size={18} /> },
    { id: "agents", label: "AI Agents", icon: <Bot size={18} /> },
    { id: "pipeline", label: "Pipeline", icon: <GitBranch size={18} /> },
    { id: "trends", label: "Trend Intel", icon: <RadioTower size={18} /> },
    { id: "knowledge", label: "Knowledge Graph", icon: <Globe size={18} /> },
    { id: "feedback", label: "Self-Improve", icon: <Brain size={18} /> },
  ]

  return (
    <aside className="w-56 border-r border-[#1a2a44] bg-[#060e1a] flex flex-col shrink-0">
      <div className="p-4 border-b border-[#1a2a44]">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-cyan-500 to-blue-600 flex items-center justify-center text-white font-bold text-sm">
            M
          </div>
          <div>
            <div className="text-sm font-bold text-white tracking-wide">MATIKS</div>
            <div className="text-[10px] text-cyan-400/70 font-mono uppercase tracking-widest">Content OS</div>
          </div>
        </div>
      </div>

      <nav className="flex-1 p-2 space-y-0.5">
        {items.map(item => (
          <button
            key={item.id}
            onClick={() => onSelect(item.id)}
            className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm transition-all ${
              activeSection === item.id
                ? "bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 shadow-[0_0_15px_rgba(6,182,212,0.1)]"
                : "text-slate-400 hover:bg-slate-800/30 hover:text-slate-200"
            }`}
          >
            {item.icon}
            <span className="font-medium">{item.label}</span>
          </button>
        ))}
      </nav>

      <div className="p-4 border-t border-[#1a2a44] space-y-3">
        <SystemStatus />
        <div className="text-[10px] text-slate-600 font-mono">
          v1.0.0 • 14 agents active
        </div>
      </div>
    </aside>
  )
}

function SystemStatus() {
  return (
    <div className="bg-[#0a1628] rounded-lg p-3 border border-[#1a2a44]">
      <div className="flex items-center gap-2 mb-2">
        <span className="status-dot status-dot-active" />
        <span className="text-[10px] font-mono text-emerald-400 uppercase tracking-wider">System Operational</span>
      </div>
      <div className="space-y-1">
        <div className="flex justify-between text-[10px]">
          <span className="text-slate-500">CPU</span>
          <span className="text-slate-400 font-mono">23%</span>
        </div>
        <div className="w-full h-1 bg-slate-800 rounded-full overflow-hidden">
          <div className="h-full bg-cyan-500/60 rounded-full" style={{ width: "23%" }} />
        </div>
        <div className="flex justify-between text-[10px]">
          <span className="text-slate-500">Queue</span>
          <span className="text-slate-400 font-mono">3/20</span>
        </div>
        <div className="w-full h-1 bg-slate-800 rounded-full overflow-hidden">
          <div className="h-full bg-purple-500/60 rounded-full" style={{ width: "15%" }} />
        </div>
      </div>
    </div>
  )
}

function OverviewSection() {
  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
      <Header title="Operator Command Center" subtitle="Real-time AI content infrastructure monitoring" />

      {/* Top Stats */}
      <div className="grid grid-cols-6 gap-3">
        <StatCard label="Channels" value={mockDashboardStats.active_channels} sub={`of ${mockDashboardStats.total_channels}`} icon={<Layers size={16} />} color="cyan" />
        <StatCard label="Avg Engagement" value={`${mockDashboardStats.avg_engagement_rate}%`} sub="+12% vs last week" icon={<TrendingUp size={16} />} color="emerald" />
        <StatCard label="Viral Score" value={mockDashboardStats.avg_viral_score.toFixed(2)} sub="across all channels" icon={<Flame size={16} />} color="amber" />
        <StatCard label="Reels/Day" value={mockDashboardStats.total_target_reels_daily} sub="target output" icon={<Play size={16} />} color="blue" />
        <StatCard label="Health Score" value={mockDashboardStats.avg_health_score.toFixed(1)} sub="avg channel health" icon={<Activity size={16} />} color="purple" />
        <StatCard label="Active Niches" value={mockDashboardStats.niches_active} sub="content verticals" icon={<Target size={16} />} color="rose" />
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-12 gap-3">
        {/* Channel Overview - left */}
        <div className="col-span-4 space-y-3">
          <Panel title="Channel Fleet" icon={<Layers size={14} />}>
            <div className="space-y-2 max-h-[320px] overflow-y-auto pr-1">
              {mockChannels.slice(0, 8).map(ch => (
                <ChannelCard key={ch.id} channel={ch} compact />
              ))}
            </div>
          </Panel>
        </div>

        {/* Agent Pipeline - center */}
        <div className="col-span-5 space-y-3">
          <Panel title="Reel Generation Pipeline" icon={<GitBranch size={14} />} subtitle="6-stage autonomous pipeline">
            <div className="space-y-2">
              {PIPELINE_STAGES.map((stage, i) => (
                <PipelineStageRow key={i} stage={stage} index={i} />
              ))}
            </div>
          </Panel>

          <Panel title="AI Agent Activity" icon={<Bot size={14} />} subtitle="14 specialized agents">
            <div className="grid grid-cols-2 gap-1.5 max-h-[180px] overflow-y-auto">
              {mockAgents.slice(0, 8).map(agent => (
                <AgentPill key={agent.type} agent={agent} />
              ))}
            </div>
          </Panel>
        </div>

        {/* Feedback + Trends - right */}
        <div className="col-span-3 space-y-3">
          <Panel title="Self-Improvement Engine" icon={<Brain size={14} />} subtitle="Live feedback signals" accent="emerald">
            <div className="space-y-2 max-h-[200px] overflow-y-auto pr-1">
              {mockFeedbackSignals.map(sig => (
                <FeedbackSignalCard key={sig.id} signal={sig} />
              ))}
            </div>
          </Panel>

          <Panel title="Trend Radar" icon={<Radio size={14} />} subtitle="Active trend intelligence">
            <div className="space-y-2 max-h-[200px] overflow-y-auto pr-1">
              {mockTrends.slice(0, 5).map(trend => (
                <TrendPill key={trend.id} trend={trend} />
              ))}
            </div>
          </Panel>
        </div>
      </div>

      {/* Bottom Row */}
      <div className="grid grid-cols-12 gap-3">
        <div className="col-span-8">
          <Panel title="Retention Curve Analysis" icon={<BarChart3 size={14} />}>
            <RetentionChart />
          </Panel>
        </div>
        <div className="col-span-4">
          <Panel title="Recent AI Adjustments" icon={<Lightbulb size={14} />} accent="amber">
            <div className="space-y-2 max-h-[200px] overflow-y-auto">
              {mockFeedbackSignals.map(sig => (
                <AdjustmentCard key={sig.id} signal={sig} />
              ))}
            </div>
          </Panel>
        </div>
      </div>
    </motion.div>
  )
}

function ChannelsSection() {
  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
      <Header title="Multi-Channel Management" subtitle="12 channels across 5 niches — AI-managed at scale" />

      <div className="grid grid-cols-3 gap-3">
        {mockChannels.map(ch => (
          <ChannelCard key={ch.id} channel={ch} />
        ))}
      </div>
    </motion.div>
  )
}

function AgentsSection() {
  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
      <Header title="AI Agent Orchestration" subtitle="14 specialized agents in autonomous multi-agent coordination" />

      {/* Agent Map */}
      <div className="grid grid-cols-7 gap-2">
        {PIPELINE_STAGES.map((stage, si) => (
          <div key={si} className="col-span-1">
            <div className={`bg-gradient-to-b ${STAGE_COLORS[stage.color]} rounded-lg p-2 border ${STAGE_BORDER[stage.color]}`}>
              <div className={`text-[9px] font-mono uppercase tracking-wider ${STAGE_TEXT[stage.color]} mb-2`}>
                Stage {si + 1}
              </div>
              <div className="text-[10px] font-medium text-slate-200 mb-2">{stage.name}</div>
              <div className="space-y-1.5">
                {stage.agents.map(agentType => {
                  const agent = mockAgents.find(a => a.type === agentType)
                  if (!agent) return null
                  return (
                    <div key={agentType} className={`bg-[#050a14]/60 rounded-md p-2 border ${STAGE_BORDER[stage.color]}`}>
                      <div className="flex items-center gap-1.5 mb-1">
                        <span className={`${STAGE_TEXT[stage.color]}`}>{AGENT_ICONS[agentType]}</span>
                        <span className="text-[10px] font-mono text-slate-300">{agentType}</span>
                      </div>
                      <div className="text-[9px] text-slate-500 leading-tight">{agent.description.slice(0, 60)}...</div>
                      <div className="flex items-center gap-2 mt-1.5">
                        <span className="text-[9px] font-mono text-emerald-400">{agent.success_rate * 100}%</span>
                        <span className="text-[9px] text-slate-600">|</span>
                        <span className="text-[9px] font-mono text-slate-400">{agent.runs_today}/day</span>
                      </div>
                    </div>
                  )
                })}
              </div>
              {si < PIPELINE_STAGES.length - 1 && (
                <div className="flex justify-center mt-2">
                  <ChevronRight size={12} className={`${STAGE_TEXT[stage.color]} opacity-50`} />
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Agent Details Grid */}
      <div className="grid grid-cols-4 gap-3 mt-4">
        {mockAgents.map(agent => (
          <div key={agent.type} className="card-dark p-4 hover:scale-[1.01] transition-transform">
            <div className="flex items-center gap-2 mb-2">
              <div className="w-8 h-8 rounded-lg bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400">
                {AGENT_ICONS[agent.type]}
              </div>
              <div>
                <div className="text-xs font-mono text-slate-200">{agent.type}</div>
                <div className="flex items-center gap-1">
                  <span className="status-dot status-dot-active" />
                  <span className="text-[9px] text-slate-500">Active</span>
                </div>
              </div>
            </div>
            <div className="text-[10px] text-slate-400 mb-3 leading-relaxed">{agent.description}</div>
            <div className="grid grid-cols-2 gap-2">
              <div className="bg-[#050a14] rounded p-1.5">
                <div className="text-[9px] text-slate-500">Success</div>
                <div className="text-xs font-mono text-emerald-400">{(agent.success_rate * 100).toFixed(0)}%</div>
              </div>
              <div className="bg-[#050a14] rounded p-1.5">
                <div className="text-[9px] text-slate-500">Runs Today</div>
                <div className="text-xs font-mono text-cyan-400">{agent.runs_today}</div>
              </div>
            </div>
            <div className="mt-2 flex flex-wrap gap-1">
              {agent.outputs.map(o => (
                <span key={o} className="text-[8px] font-mono bg-cyan-500/10 text-cyan-400 px-1.5 py-0.5 rounded">
                  {o}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </motion.div>
  )
}

function PipelineSection() {
  const [activePipeline, setActivePipeline] = useState(true)

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
      <Header title="Autonomous Reel Pipeline" subtitle="End-to-end AI content generation — Trend to Publish" />

      <div className="flex items-center gap-4 mb-4">
        <button
          onClick={() => setActivePipeline(!activePipeline)}
          className="px-4 py-2 bg-cyan-500/20 border border-cyan-500/30 text-cyan-400 rounded-lg text-sm font-medium hover:bg-cyan-500/30 transition-all flex items-center gap-2"
        >
          <Play size={14} /> Trigger Pipeline
        </button>
        <div className="text-xs text-slate-500">Pipeline runs: 247 today | Avg duration: 4.2 min | Success: 93.1%</div>
      </div>

      {/* Pipeline Flow Visualization */}
      <div className="relative">
        <div className="flex items-stretch gap-1">
          {PIPELINE_STAGES.map((stage, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: i * 0.15 }}
              className="flex-1"
            >
              <div className={`bg-gradient-to-b ${STAGE_COLORS[stage.color]} rounded-xl p-4 border ${STAGE_BORDER[stage.color]} h-full`}>
                <div className="text-center mb-3">
                  <div className={`inline-flex w-6 h-6 rounded-full ${STAGE_DOT[stage.color]} text-[#050a14] text-xs font-bold items-center justify-center mb-1`}>
                    {i + 1}
                  </div>
                  <div className="text-xs font-semibold text-slate-200">{stage.name}</div>
                </div>

                <div className="space-y-2">
                  {stage.agents.map(at => (
                    <div key={at} className="bg-[#050a14]/50 rounded-lg p-2 border border-white/5">
                      <div className="flex items-center gap-1.5">
                        <span className={STAGE_TEXT[stage.color]}>{AGENT_ICONS[at]}</span>
                        <span className="text-[10px] font-mono text-slate-300">{at}</span>
                      </div>
                      {activePipeline && (
                        <motion.div
                          initial={{ width: "0%" }}
                          animate={{ width: "100%" }}
                          transition={{ delay: i * 0.8, duration: 1.5, repeat: Infinity, repeatType: "reverse" }}
                          className={`h-0.5 ${STAGE_DOT[stage.color]} rounded mt-1 opacity-50`}
                        />
                      )}
                    </div>
                  ))}
                </div>
              </div>

              {i < PIPELINE_STAGES.length - 1 && (
                <div className="flex items-center justify-center -mt-4 relative z-10">
                  <div className={`w-6 h-0.5 ${STAGE_DOT[stage.color]} opacity-40`} />
                  <ChevronRight size={10} className={STAGE_TEXT[stage.color]} />
                </div>
              )}
            </motion.div>
          ))}
        </div>
      </div>

      {/* Generated Content Preview */}
      <div className="grid grid-cols-3 gap-3 mt-4">
        <Panel title="Script Preview" icon={<MessageSquare size={14} />}>
          <div className="text-[10px] text-slate-400 leading-relaxed font-mono">
            <span className="text-cyan-400">[HOOK]</span> Everyone is wrong about fitness transformations<br /><br />
            <span className="text-purple-400">[BODY]</span> Most people spend 2 hours on what this does in 15 minutes. The secret? Compound engagement...<br /><br />
            <span className="text-emerald-400">[CTA]</span> Save this and try it tomorrow morning →
          </div>
        </Panel>
        <Panel title="Scene Breakdown" icon={<Clapperboard size={14} />}>
          <div className="space-y-1.5">
            {[
              { t: "0-2s", type: "HOOK", desc: "Bold text overlay" },
              { t: "2-8s", type: "PROBLEM", desc: "Common mistake demo" },
              { t: "8-18s", type: "SOLUTION", desc: "Correct approach reveal" },
              { t: "18-25s", type: "PROOF", desc: "Results + social proof" },
              { t: "25-30s", type: "CTA", desc: "Save + follow prompt" },
            ].map((s, i) => (
              <div key={i} className="flex items-center gap-2 bg-[#050a14]/50 rounded p-1.5">
                <span className="text-[9px] font-mono text-slate-500 w-10">{s.t}</span>
                <span className="text-[9px] font-mono text-cyan-400">{s.type}</span>
                <span className="text-[9px] text-slate-400">{s.desc}</span>
              </div>
            ))}
          </div>
        </Panel>
        <Panel title="Voiceover Config" icon={<Volume2 size={14} />}>
          <div className="space-y-1.5">
            {[
              { k: "Voice", v: "Adam — Confident Male" },
              { k: "Speed", v: "1.1x (fast)" },
              { k: "Stability", v: "0.65" },
              { k: "Clarity", v: "0.85" },
              { k: "Style", v: "0.7 (expressive)" },
              { k: "Emotion", v: "energetic" },
            ].map((item, i) => (
              <div key={i} className="flex justify-between bg-[#050a14]/50 rounded p-1.5">
                <span className="text-[9px] text-slate-500">{item.k}</span>
                <span className="text-[9px] font-mono text-cyan-400">{item.v}</span>
              </div>
            ))}
          </div>
        </Panel>
      </div>
    </motion.div>
  )
}

function TrendsSection() {
  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
      <Header title="Trend Intelligence Engine" subtitle="Real-time trend discovery, scoring, and opportunity mapping" />

      {/* Trend Stats */}
      <div className="grid grid-cols-4 gap-3">
        <StatCard label="Trends Tracked" value="847" sub="across 5 platforms" icon={<Radio size={16} />} color="cyan" />
        <StatCard label="Emerging" value="23" sub="detected in last 24h" icon={<Sparkles size={16} />} color="purple" />
        <StatCard label="Viral Now" value="8" sub="actively spreading" icon={<Flame size={16} />} color="amber" />
        <StatCard label="Avg Opportunity" value="0.81" sub="across all niches" icon={<Target size={16} />} color="emerald" />
      </div>

      {/* Trend Cards */}
      <div className="grid grid-cols-2 gap-3">
        {mockTrends.map(trend => (
          <div key={trend.id} className="card-dark p-4 hover:scale-[1.005] transition-transform">
            <div className="flex items-start justify-between mb-3">
              <div>
                <div className="flex items-center gap-2">
                  <span className={`text-xs font-semibold ${trend.status === "viral" ? "text-amber-400" : trend.status === "hot" ? "text-rose-400" : trend.status === "emerging" ? "text-purple-400" : "text-cyan-400"}`}>
                    {trend.name}
                  </span>
                  <span className={`text-[8px] uppercase font-mono px-1.5 py-0.5 rounded ${
                    trend.status === "viral" ? "bg-amber-500/20 text-amber-400" :
                    trend.status === "hot" ? "bg-rose-500/20 text-rose-400" :
                    trend.status === "emerging" ? "bg-purple-500/20 text-purple-400" :
                    "bg-cyan-500/20 text-cyan-400"
                  }`}>
                    {trend.status}
                  </span>
                </div>
                <div className="text-[10px] text-slate-500 mt-0.5">
                  {trend.niche} • {trend.source} • {trend.type}
                </div>
              </div>
            </div>

            {/* Score Bars */}
            <div className="grid grid-cols-4 gap-2 mb-3">
              {[
                { label: "Confidence", value: trend.confidence, color: "bg-cyan-500" },
                { label: "Opportunity", value: trend.opportunity, color: "bg-emerald-500" },
                { label: "Saturation", value: trend.saturation, color: "bg-amber-500" },
                { label: "Velocity", value: trend.velocity, color: "bg-purple-500" },
              ].map(s => (
                <div key={s.label}>
                  <div className="text-[8px] text-slate-500 mb-0.5">{s.label}</div>
                  <div className="w-full h-1 bg-slate-800 rounded-full overflow-hidden">
                    <div className={`h-full ${s.color} rounded-full`} style={{ width: `${s.value * 100}%` }} />
                  </div>
                  <div className="text-[9px] font-mono text-slate-400 mt-0.5">{(s.value * 100).toFixed(0)}%</div>
                </div>
              ))}
            </div>

            {/* Hooks */}
            <div className="space-y-1">
              <div className="text-[9px] text-slate-500 uppercase tracking-wider">Top Hooks</div>
              {trend.viral_hooks.map((hook, i) => (
                <div key={i} className="text-[10px] text-slate-300 bg-[#050a14]/50 rounded px-2 py-1">
                  &ldquo;{hook}&rdquo;
                </div>
              ))}
            </div>

            {/* Growth */}
            <div className="flex items-center gap-3 mt-2 pt-2 border-t border-[#1a2a44]">
              <div className="flex items-center gap-1">
                <ArrowUpRight size={10} className="text-emerald-400" />
                <span className="text-[9px] font-mono text-emerald-400">+{trend.growth_24h}% 24h</span>
              </div>
              <div className="flex items-center gap-1">
                <ArrowUpRight size={10} className="text-cyan-400" />
                <span className="text-[9px] font-mono text-cyan-400">+{trend.growth_7d}% 7d</span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </motion.div>
  )
}

function KnowledgeSection() {
  const nodes = [
    { id: "n1", type: "hook", label: "Contrarian Hook", x: 80, y: 60, cluster: "alpha" },
    { id: "n2", type: "hook", label: "Question Hook", x: 200, y: 40, cluster: "alpha" },
    { id: "n3", type: "hook", label: "Shocking Stat", x: 320, y: 80, cluster: "alpha" },
    { id: "n4", type: "format", label: "Step-by-Step", x: 60, y: 160, cluster: "beta" },
    { id: "n5", type: "format", label: "Countdown", x: 180, y: 180, cluster: "beta" },
    { id: "n6", type: "format", label: "Before/After", x: 300, y: 150, cluster: "beta" },
    { id: "n7", type: "emotion", label: "Curiosity", x: 440, y: 60, cluster: "gamma" },
    { id: "n8", type: "emotion", label: "Fear", x: 500, y: 140, cluster: "gamma" },
    { id: "n9", type: "emotion", label: "Aspiration", x: 460, y: 220, cluster: "gamma" },
    { id: "n10", type: "audience", label: "Gen Z Male", x: 600, y: 80, cluster: "delta" },
    { id: "n11", type: "audience", label: "Mill. Female", x: 620, y: 180, cluster: "delta" },
    { id: "n12", type: "trend", label: "AI Tools", x: 140, y: 280, cluster: "epsilon" },
    { id: "n13", type: "trend", label: "Fitness Transform", x: 280, y: 290, cluster: "epsilon" },
    { id: "n14", type: "niche", label: "Fitness", x: 720, y: 60, cluster: "alpha" },
    { id: "n15", type: "niche", label: "Tech", x: 740, y: 160, cluster: "beta" },
    { id: "n16", type: "niche", label: "Motivation", x: 720, y: 260, cluster: "gamma" },
    { id: "n17", type: "content", label: "Reel #247", x: 400, y: 300, cluster: "alpha" },
    { id: "n18", type: "content", label: "Reel #248", x: 540, y: 310, cluster: "beta" },
  ]

  const edges = [
    { source: "n1", target: "n4" }, { source: "n1", target: "n7" },
    { source: "n2", target: "n5" }, { source: "n3", target: "n8" },
    { source: "n4", target: "n12" }, { source: "n5", target: "n13" },
    { source: "n7", target: "n10" }, { source: "n9", target: "n11" },
    { source: "n10", target: "n14" }, { source: "n11", target: "n15" },
    { source: "n12", target: "n15" }, { source: "n13", target: "n14" },
    { source: "n17", target: "n1" }, { source: "n17", target: "n4" },
    { source: "n18", target: "n3" }, { source: "n18", target: "n6" },
    { source: "n1", target: "n2" }, { source: "n4", target: "n5" },
    { source: "n8", target: "n16" }, { source: "n9", target: "n16" },
  ]

  const typeColors: Record<string, string> = {
    hook: "#06b6d4", format: "#8b5cf6", emotion: "#f43f5e",
    audience: "#f59e0b", trend: "#10b981", niche: "#3b82f6", content: "#ec4899",
  }

  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
      <Header title="Content Knowledge Graph" subtitle="Neural visualization of content relationships, viral clusters, and hook families" />

      {/* Graph Visualization */}
      <div className="card-dark p-4 relative overflow-hidden">
        <div className="flex items-center gap-4 mb-4">
          <div className="text-xs font-semibold text-slate-200">Content Relationship Network</div>
          <div className="flex gap-3">
            {Object.entries(typeColors).map(([type, color]) => (
              <div key={type} className="flex items-center gap-1">
                <div className="w-2 h-2 rounded-full" style={{ backgroundColor: color }} />
                <span className="text-[9px] text-slate-400 capitalize">{type}</span>
              </div>
            ))}
          </div>
        </div>

        <svg viewBox="0 0 800 350" className="w-full h-[400px]">
          {/* Edges */}
          {edges.map((edge, i) => {
            const s = nodes.find(n => n.id === edge.source)
            const t = nodes.find(n => n.id === edge.target)
            if (!s || !t) return null
            return (
              <line
                key={i}
                x1={s.x} y1={s.y} x2={t.x} y2={t.y}
                stroke="rgba(6,182,212,0.15)"
                strokeWidth="1"
                strokeDasharray="4,4"
              />
            )
          })}

          {/* Nodes */}
          {nodes.map(node => (
            <g key={node.id}>
              <circle cx={node.x} cy={node.y} r="18" fill={`${typeColors[node.type]}15`} stroke={typeColors[node.type]} strokeWidth="1" />
              <circle cx={node.x} cy={node.y} r="4" fill={typeColors[node.type]} className="animate-pulse-glow" />
              <text x={node.x} y={node.y + 28} textAnchor="middle" className="text-[8px] fill-slate-400">{node.label}</text>
            </g>
          ))}
        </svg>

        {/* Animated pulse effect */}
        <div className="absolute inset-0 pointer-events-none">
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[300px] h-[300px] rounded-full border border-cyan-500/5 animate-spin-slow" />
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[200px] h-[200px] rounded-full border border-purple-500/5 animate-spin-slow" style={{ animationDirection: "reverse" }} />
        </div>
      </div>

      {/* Cluster Cards */}
      <div className="grid grid-cols-5 gap-3">
        {[
          { id: "alpha", name: "Viral Hook Cluster", count: 12, perf: 0.82, type: "hook", color: "cyan" },
          { id: "beta", name: "Format Cluster", count: 8, perf: 0.71, type: "format", color: "purple" },
          { id: "gamma", name: "Emotion Cluster", count: 10, perf: 0.78, type: "emotion", color: "rose" },
          { id: "delta", name: "Audience Cluster", count: 6, perf: 0.65, type: "audience", color: "amber" },
          { id: "epsilon", name: "Trend Cluster", count: 9, perf: 0.74, type: "trend", color: "emerald" },
        ].map(cluster => (
          <div key={cluster.id} className="card-dark p-3">
            <div className={`text-[9px] font-mono uppercase tracking-wider ${STAGE_TEXT[cluster.color]} mb-1`}>{cluster.id} cluster</div>
            <div className="text-xs font-medium text-slate-200 mb-2">{cluster.name}</div>
            <div className="flex items-center justify-between">
              <span className="text-[10px] text-slate-500">{cluster.count} nodes</span>
              <span className={`text-xs font-mono ${getScoreColor(cluster.perf)}`}>{(cluster.perf * 100).toFixed(0)}%</span>
            </div>
          </div>
        ))}
      </div>
    </motion.div>
  )
}

function FeedbackSection() {
  return (
    <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
      <Header title="Self-Improving Content Intelligence" subtitle="The AI learns from every metric and automatically optimizes all agent behavior" />

      {/* Core Engine Status */}
      <div className="card-dark p-4 glow-border-emerald">
        <div className="flex items-center gap-3 mb-3">
          <div className="w-10 h-10 rounded-lg bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center">
            <Brain size={20} className="text-emerald-400 animate-pulse" />
          </div>
          <div>
            <div className="text-sm font-semibold text-emerald-400">Feedback Loop Engine — ACTIVE</div>
            <div className="text-[10px] text-slate-400">Continuously analyzing 847 content data points across 12 channels</div>
          </div>
          <div className="ml-auto flex items-center gap-2">
            <span className="status-dot status-dot-active" />
            <span className="text-[10px] font-mono text-emerald-400">Auto-adjusting</span>
          </div>
        </div>
      </div>

      {/* Feedback Signals */}
      <div className="grid grid-cols-1 gap-3">
        {mockFeedbackSignals.map((sig, i) => (
          <motion.div
            key={sig.id}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: i * 0.1 }}
            className="card-dark p-4"
          >
            <div className="flex items-start gap-4">
              {/* Signal Type */}
              <div className={`w-10 h-10 rounded-lg flex items-center justify-center shrink-0 ${
                sig.type === "retention_drop" ? "bg-red-500/10 border border-red-500/20" :
                sig.type === "engagement_spike" ? "bg-emerald-500/10 border border-emerald-500/20" :
                sig.type === "completion_improvement" ? "bg-cyan-500/10 border border-cyan-500/20" :
                sig.type === "audience_shift" ? "bg-purple-500/10 border border-purple-500/20" :
                "bg-amber-500/10 border border-amber-500/20"
              }`}>
                {sig.type === "retention_drop" ? <ArrowDownRight size={18} className="text-red-400" /> :
                 sig.type === "engagement_spike" ? <ArrowUpRight size={18} className="text-emerald-400" /> :
                 sig.type === "completion_improvement" ? <ArrowUpRight size={18} className="text-cyan-400" /> :
                 <Activity size={18} className="text-amber-400" />}
              </div>

              {/* Signal Details */}
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-xs font-semibold text-slate-200">{sig.diagnosis}</span>
                  {sig.is_significant && (
                    <span className="text-[8px] bg-amber-500/20 text-amber-400 px-1.5 py-0.5 rounded font-mono">SIGNIFICANT</span>
                  )}
                  {sig.action_required && (
                    <span className="text-[8px] bg-emerald-500/20 text-emerald-400 px-1.5 py-0.5 rounded font-mono">AUTO-FIXING</span>
                  )}
                </div>

                <div className="flex items-center gap-4 mb-2">
                  <div className="text-[10px] text-slate-500">Metric: <span className="text-slate-300 font-mono">{sig.metric}</span></div>
                  <div className="text-[10px] text-slate-500">Delta: <span className={(typeof sig.delta === "number" && sig.delta > 0) ? "text-emerald-400 font-mono" : "text-red-400 font-mono"}>{(typeof sig.delta === "number" && sig.delta > 0) ? "+" : ""}{typeof sig.delta === "number" ? sig.delta.toFixed(2) : sig.delta}</span></div>
                </div>

                {/* Adjustment */}
                <div className="bg-[#050a14] rounded-lg p-3 border border-[#1a2a44]">
                  <div className="text-[9px] text-emerald-400 uppercase tracking-wider font-mono mb-1">AI Strategy Adjustment</div>
                  <div className="text-[10px] text-slate-300">
                    Agent <span className="font-mono text-cyan-400">{sig.adjustment.agent}</span> → parameter{" "}
                    <span className="font-mono text-purple-400">{sig.adjustment.parameter}</span>:{" "}
                    <span className="font-mono text-red-400 line-through">{sig.adjustment.current_value}</span>{" "}
                    <span className="font-mono text-emerald-400">{sig.adjustment.new_value}</span>
                  </div>
                  <div className="text-[10px] text-slate-500 mt-1 italic">{sig.adjustment.reason}</div>
                </div>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {/* Why the AI Changed Strategy */}
      <div className="card-dark p-4">
        <div className="text-xs font-semibold text-amber-400 mb-3">Why the AI Changed Strategy — Summary</div>
        <div className="text-[10px] text-slate-400 leading-relaxed">
          Self-improvement engine detected 5 significant feedback signals. Auto-applying 5 strategy adjustments across 5 agents.
          Key changes: stronger hooks (shorter openings), opinionated script tone, faster scene pacing, storytelling narrative shift,
          and posting time optimization. Expected impact: <span className="text-emerald-400">+15-25% engagement improvement</span> over next 7 days.
        </div>
      </div>
    </motion.div>
  )
}

// ─── Sub-Components ─────────────────────────────────────────────────────────

function Header({ title, subtitle }: { title: string; subtitle: string }) {
  return (
    <div className="flex items-center justify-between">
      <div>
        <h1 className="text-lg font-bold text-white tracking-tight">{title}</h1>
        <p className="text-[11px] text-slate-500">{subtitle}</p>
      </div>
      <div className="flex items-center gap-2">
        <span className="status-dot status-dot-active" />
        <span className="text-[10px] font-mono text-slate-500">Live</span>
      </div>
    </div>
  )
}

function Panel({ title, icon, subtitle, accent, children }: { title: string; icon?: React.ReactNode; subtitle?: string; accent?: string; children: React.ReactNode }) {
  const borderClass = accent === "emerald" ? "glow-border-emerald" : accent === "amber" ? "glow-border-purple" : "glow-border"
  return (
    <div className={`card-dark p-3 ${borderClass}`}>
      <div className="flex items-center justify-between mb-2">
        <div className="flex items-center gap-1.5">
          {icon && <span className="text-cyan-400">{icon}</span>}
          <span className="text-[11px] font-semibold text-slate-200">{title}</span>
        </div>
        {subtitle && <span className="text-[9px] text-slate-600">{subtitle}</span>}
      </div>
      {children}
    </div>
  )
}

function StatCard({ label, value, sub, icon, color }: { label: string; value: string | number; sub: string; icon: React.ReactNode; color: string }) {
  const colorMap: Record<string, string> = {
    cyan: "from-cyan-500/10 to-cyan-600/5 border-cyan-500/20 text-cyan-400",
    emerald: "from-emerald-500/10 to-emerald-600/5 border-emerald-500/20 text-emerald-400",
    amber: "from-amber-500/10 to-amber-600/5 border-amber-500/20 text-amber-400",
    blue: "from-blue-500/10 to-blue-600/5 border-blue-500/20 text-blue-400",
    purple: "from-purple-500/10 to-purple-600/5 border-purple-500/20 text-purple-400",
    rose: "from-rose-500/10 to-rose-600/5 border-rose-500/20 text-rose-400",
  }
  const c = colorMap[color] || colorMap.cyan
  const textColor = c.split(" ").pop()

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`bg-gradient-to-br ${c} rounded-xl p-3 border`}
    >
      <div className="flex items-center justify-between mb-1">
        <span className="text-[10px] text-slate-500">{label}</span>
        <span className={textColor}>{icon}</span>
      </div>
      <div className={`text-xl font-bold font-mono ${textColor}`}>{value}</div>
      <div className="text-[9px] text-slate-500 mt-0.5">{sub}</div>
    </motion.div>
  )
}

function ChannelCard({ channel, compact = false }: { channel: typeof mockChannels[0]; compact?: boolean }) {
  if (compact) {
    return (
      <div className="flex items-center gap-2 bg-[#050a14]/50 rounded-lg p-2 border border-[#1a2a44] hover:border-cyan-500/20 transition-colors">
        <span className="text-lg">{channel.emoji}</span>
        <div className="flex-1 min-w-0">
          <div className="text-[10px] font-semibold text-slate-200 truncate">{channel.name}</div>
          <div className="text-[9px] text-slate-500">{channel.niche} • {formatNumber(channel.followers)}</div>
        </div>
        <div className="text-right">
          <div className={`text-[10px] font-mono ${getScoreColor(channel.viral_probability_score)}`}>
            {(channel.viral_probability_score * 100).toFixed(0)}%
          </div>
          <div className="text-[8px] text-slate-600">viral</div>
        </div>
      </div>
    )
  }

  return (
    <div className={`card-dark p-4 ${getGlowClass(channel.channel_health_score / 100)}`}>
      <div className="flex items-center gap-3 mb-3">
        <span className="text-2xl">{channel.emoji}</span>
        <div className="flex-1">
          <div className="text-sm font-semibold text-white">{channel.name}</div>
          <div className="text-[10px] text-slate-500 font-mono">{channel.handle}</div>
        </div>
        <span className={`text-[9px] uppercase font-mono px-2 py-0.5 rounded ${
          channel.status === "active" ? "bg-emerald-500/20 text-emerald-400" :
          channel.status === "growing" ? "bg-cyan-500/20 text-cyan-400" :
          "bg-slate-500/20 text-slate-400"
        }`}>
          {channel.status}
        </span>
      </div>

      <div className="grid grid-cols-3 gap-2 mb-3">
        <div className="bg-[#050a14] rounded p-2">
          <div className="text-[8px] text-slate-500">Followers</div>
          <div className="text-xs font-mono text-slate-200">{formatNumber(channel.followers)}</div>
        </div>
        <div className="bg-[#050a14] rounded p-2">
          <div className="text-[8px] text-slate-500">Eng Rate</div>
          <div className="text-xs font-mono text-emerald-400">{channel.avg_engagement_rate}%</div>
        </div>
        <div className="bg-[#050a14] rounded p-2">
          <div className="text-[8px] text-slate-500">Reels/Day</div>
          <div className="text-xs font-mono text-cyan-400">{channel.target_reels_per_day}</div>
        </div>
      </div>

      {/* Score Bars */}
      <div className="space-y-1.5">
        {[
          { label: "Viral Prob", value: channel.viral_probability_score, color: "bg-amber-500" },
          { label: "Health", value: channel.channel_health_score / 100, color: "bg-emerald-500" },
          { label: "Momentum", value: channel.momentum_score, color: "bg-cyan-500" },
        ].map(s => (
          <div key={s.label} className="flex items-center gap-2">
            <span className="text-[9px] text-slate-500 w-16">{s.label}</span>
            <div className="flex-1 h-1.5 bg-slate-800 rounded-full overflow-hidden">
              <div className={`h-full ${s.color} rounded-full transition-all`} style={{ width: `${s.value * 100}%` }} />
            </div>
            <span className={`text-[9px] font-mono ${getScoreColor(s.value)}`}>{(s.value * 100).toFixed(0)}%</span>
          </div>
        ))}
      </div>

      {/* AI Strategy */}
      <div className="mt-3 pt-2 border-t border-[#1a2a44]">
        <div className="text-[9px] text-slate-600 uppercase tracking-wider mb-1">AI Strategy</div>
        <div className="flex flex-wrap gap-1">
          <span className="text-[8px] bg-cyan-500/10 text-cyan-400 px-1.5 py-0.5 rounded font-mono">{channel.ai_strategy.hook_style}</span>
          <span className="text-[8px] bg-purple-500/10 text-purple-400 px-1.5 py-0.5 rounded font-mono">{channel.ai_strategy.pacing}</span>
          <span className="text-[8px] bg-emerald-500/10 text-emerald-400 px-1.5 py-0.5 rounded font-mono">{channel.ai_strategy.cta_type}</span>
        </div>
      </div>
    </div>
  )
}

function PipelineStageRow({ stage, index }: { stage: typeof PIPELINE_STAGES[0]; index: number }) {
  return (
    <div className="flex items-center gap-2">
      <div className={`w-6 h-6 rounded-md ${STAGE_DOT[stage.color]} flex items-center justify-center text-[#050a14] text-[10px] font-bold shrink-0`}>
        {index + 1}
      </div>
      <div className={`flex-1 bg-gradient-to-r ${STAGE_COLORS[stage.color]} rounded-lg p-2.5 border ${STAGE_BORDER[stage.color]}`}>
        <div className="flex items-center justify-between">
          <span className={`text-[11px] font-semibold ${STAGE_TEXT[stage.color]}`}>{stage.name}</span>
          <div className="flex gap-1">
            {stage.agents.map(at => (
              <span key={at} className="text-[9px] font-mono bg-[#050a14]/50 text-slate-400 px-1.5 py-0.5 rounded">
                {at.replace(/_/g, " ")}
              </span>
            ))}
          </div>
        </div>
        <div className="flex items-center gap-2 mt-1">
          <div className="flex-1 h-0.5 bg-slate-800/50 rounded-full overflow-hidden">
            <motion.div
              initial={{ width: "0%" }}
              animate={{ width: "100%" }}
              transition={{ delay: index * 0.5, duration: 2, repeat: Infinity, repeatType: "reverse" }}
              className={`h-full ${STAGE_DOT[stage.color]} rounded-full opacity-60`}
            />
          </div>
          <CheckCircle2 size={10} className="text-emerald-400" />
        </div>
      </div>
    </div>
  )
}

function AgentPill({ agent }: { agent: typeof mockAgents[0] }) {
  return (
    <div className="flex items-center gap-1.5 bg-[#050a14]/50 rounded px-2 py-1.5 border border-[#1a2a44]">
      <span className="text-cyan-400">{AGENT_ICONS[agent.type]}</span>
      <span className="text-[9px] font-mono text-slate-300 truncate">{agent.type.replace(/_/g, " ")}</span>
      <span className="status-dot status-dot-active ml-auto shrink-0" />
    </div>
  )
}

function FeedbackSignalCard({ signal }: { signal: typeof mockFeedbackSignals[0] }) {
  return (
    <div className="bg-[#050a14]/50 rounded-lg p-2 border border-[#1a2a44]">
      <div className="flex items-center gap-1.5 mb-1">
        {signal.type === "retention_drop" ? <ArrowDownRight size={10} className="text-red-400" /> :
         signal.type === "engagement_spike" ? <ArrowUpRight size={10} className="text-emerald-400" /> :
         <Activity size={10} className="text-cyan-400" />}
        <span className="text-[9px] font-medium text-slate-300">{signal.metric.replace(/_/g, " ")}</span>
        <span className={`text-[9px] font-mono ml-auto ${(typeof signal.delta === "number" && signal.delta > 0) ? "text-emerald-400" : "text-red-400"}`}>
          {(typeof signal.delta === "number" && signal.delta > 0) ? "+" : ""}{typeof signal.delta === "number" ? signal.delta.toFixed(2) : signal.delta}
        </span>
      </div>
      <div className="text-[9px] text-slate-500 leading-tight">{signal.diagnosis.slice(0, 60)}...</div>
      {signal.action_required && (
        <div className="mt-1 text-[8px] text-emerald-400 font-mono">
          → {signal.adjustment.agent}: {signal.adjustment.current_value} → {signal.adjustment.new_value}
        </div>
      )}
    </div>
  )
}

function TrendPill({ trend }: { trend: typeof mockTrends[0] }) {
  return (
    <div className="bg-[#050a14]/50 rounded-lg p-2 border border-[#1a2a44]">
      <div className="flex items-center justify-between mb-0.5">
        <span className="text-[10px] text-slate-200 font-medium">{trend.name}</span>
        <span className={`text-[8px] uppercase font-mono px-1 py-0.5 rounded ${
          trend.status === "viral" ? "bg-amber-500/20 text-amber-400" :
          trend.status === "hot" ? "bg-rose-500/20 text-rose-400" :
          trend.status === "emerging" ? "bg-purple-500/20 text-purple-400" :
          "bg-cyan-500/20 text-cyan-400"
        }`}>
          {trend.status}
        </span>
      </div>
      <div className="flex items-center gap-2">
        <div className="flex-1 h-0.5 bg-slate-800 rounded-full overflow-hidden">
          <div className="h-full bg-cyan-500 rounded-full" style={{ width: `${trend.opportunity * 100}%` }} />
        </div>
        <span className="text-[8px] font-mono text-slate-400">{(trend.opportunity * 100).toFixed(0)}%</span>
      </div>
    </div>
  )
}

function AdjustmentCard({ signal }: { signal: typeof mockFeedbackSignals[0] }) {
  return (
    <div className="bg-[#050a14]/50 rounded p-2 border border-[#1a2a44]">
      <div className="flex items-center gap-1.5 mb-1">
        <span className="text-[9px] font-mono text-cyan-400">{signal.adjustment.agent}</span>
        <ArrowUpRight size={8} className="text-emerald-400" />
        <span className="text-[9px] font-mono text-emerald-400">{signal.adjustment.new_value}</span>
      </div>
      <div className="text-[8px] text-slate-500">{signal.adjustment.reason.slice(0, 70)}...</div>
    </div>
  )
}

function RetentionChart() {
  const retentionData = [
    { second: "0s", retention: 100 },
    { second: "2s", retention: 72 },
    { second: "5s", retention: 58 },
    { second: "10s", retention: 45 },
    { second: "15s", retention: 38 },
    { second: "20s", retention: 33 },
    { second: "25s", retention: 28 },
    { second: "30s", retention: 22 },
  ]

  return (
    <div className="space-y-3">
      <div className="flex items-end gap-1 h-[120px]">
        {retentionData.map((d, i) => (
          <div key={i} className="flex-1 flex flex-col items-center gap-1">
            <motion.div
              initial={{ height: 0 }}
              animate={{ height: `${d.retention}%` }}
              transition={{ delay: i * 0.1, duration: 0.5 }}
              className="w-full rounded-t"
              style={{
                background: `linear-gradient(to top, ${d.retention > 50 ? "rgba(6,182,212,0.3)" : d.retention > 30 ? "rgba(139,92,246,0.3)" : "rgba(244,63,94,0.3)"}, transparent)`,
                border: `1px solid ${d.retention > 50 ? "rgba(6,182,212,0.4)" : d.retention > 30 ? "rgba(139,92,246,0.4)" : "rgba(244,63,94,0.4)"}`,
                minHeight: "4px",
              }}
            />
            <span className="text-[8px] text-slate-500">{d.second}</span>
          </div>
        ))}
      </div>

      {/* Hook Drop-Off Highlight */}
      <div className="bg-red-500/5 border border-red-500/20 rounded-lg p-2">
        <div className="flex items-center gap-1.5">
          <AlertTriangle size={10} className="text-red-400" />
          <span className="text-[9px] text-red-400 font-medium">Hook Drop-Off Detected</span>
        </div>
        <div className="text-[9px] text-slate-400 mt-1">
          28% viewer loss in first 2 seconds — AI adjusting hook duration from 2.0s → 1.0s
        </div>
      </div>

      <div className="grid grid-cols-4 gap-2">
        {[
          { label: "Avg Watch", value: "18.3s", change: "+2.1s" },
          { label: "Hook Retention", value: "42%", change: "-16%" },
          { label: "Completion", value: "38%", change: "+9%" },
          { label: "Viral Coeff", value: "1.24", change: "+0.18" },
        ].map(m => (
          <div key={m.label} className="bg-[#050a14] rounded p-1.5">
            <div className="text-[8px] text-slate-500">{m.label}</div>
            <div className="text-[11px] font-mono text-slate-200">{m.value}</div>
            <div className={`text-[8px] font-mono ${m.change.startsWith("+") ? "text-emerald-400" : "text-red-400"}`}>{m.change}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
