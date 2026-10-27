"use client";

import React, { useState } from "react";
import {
  Sparkles,
  ArrowRight,
  CheckCircle2,
  TrendingUp,
  Bot,
  Zap,
  ShieldCheck,
  Star,
  Layers,
  ChevronDown,
  ChevronUp,
  Terminal,
  Cpu,
  Copy,
  Check,
  DollarSign,
  Clock,
  Send,
  ExternalLink,
  Database,
} from "lucide-react";

const GUMROAD_CHECKOUT_URL = "https://mixiosi.gumroad.com/l/nshou?wanted=true";
const GUMROAD_LEAD_VAULT_URL = "https://mixiosi.gumroad.com/l/homeserviceleads";

export default function LandingPage() {
  const [activeTab, setActiveTab] = useState(0);
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);
  const [teamSize, setTeamSize] = useState(3);
  const [activeFaq, setActiveFaq] = useState<number | null>(null);

  const modules = [
    {
      title: "Module 1: Inbound & Search Authority",
      promptsCount: "20 Prompts",
      desc: "Topological keyword clustering, high-intent BOFU articles, competitor battlecards, and programmatic landing page matrices.",
      sampleTitle: "Search-Intent Keyword Topology & Cluster Architect",
      sampleRole: "Senior SEO & Technical Content Strategist",
      sampleCode: `Role: Senior SEO & Technical Content Strategist.
Task: Create an exhaustive topic cluster map for {{TARGET_NICHE}} optimized for high buyer intent.
Input Data:
- Product Category: {{PRODUCT_CATEGORY}}
- Target ICP: {{ICP_TITLE}} at {{COMPANY_SIZE}}
- Core Value Proposition: {{CORE_VALUE_PROP}}

Instructions:
1. Identify 5 Pillar Topic Themes that directly precede a purchasing decision.
2. Under each Pillar, generate 4 Sub-topics:
   - 2 Informational ("How to solve X without Y")
   - 1 Commercial Investigation ("Top alternatives to Z in 2026")
   - 1 High-intent Transactional ("Implementation checklist for X")
Format output as a structured Markdown table with primary & semantic keywords.`,
    },
    {
      title: "Module 2: High-Converting Outbound & ABM",
      promptsCount: "20 Prompts",
      desc: "Signal-based trigger emails, 1:1 enterprise account dossiers, omnichannel cadences, and dark pipeline reactivation.",
      sampleTitle: "Signal-Based Hyper-Personalized Cold Email Generator",
      sampleRole: "Elite Outbound SDR & Pipeline Engineer",
      sampleCode: `Role: Elite Outbound SDR & Pipeline Engineer.
Trigger Event: Target company {{COMPANY_NAME}} just {{TRIGGER_EVENT}} (e.g., hired new VP, raised round).
Recipient: {{PROSPECT_FIRST_NAME}}, {{PROSPECT_TITLE}}.

Constraints:
- Word count: Under 85 words.
- Reading grade level: 5th grade.
- Zero self-congratulatory filler ("Hope this finds you well").
- Single low-friction call-to-interest.

Framework:
1. Observation: State the verified trigger event and immediate technical friction.
2. Insight: Explain how peer companies handled this bottleneck.
3. Soft Offer: Offer a 2-page benchmark PDF or loom teardown.`,
    },
    {
      title: "Module 3: Product-Led Growth & Onboarding",
      promptsCount: "20 Prompts",
      desc: "Sub-300-second Time-to-Value flows, behavioral lifecycle triggers, micro-surveys, and usage-gated paywall copy.",
      sampleTitle: "First 5-Minute Time-to-Value (TTV) User Onboarding Flow",
      sampleRole: "Product-Led Growth Specialist",
      sampleCode: `Role: Product-Led Growth Specialist.
Goal: Map the exact sequence to bring a newly registered user of {{PRODUCT_NAME}} to their "Aha!" moment in < 300 seconds.

Deliverables:
1. Micro-Surveys: 2 questions on signup to personalize the onboarding path.
2. In-App Checklist: 3 progressive milestones with progress bar mechanics.
3. Empty State Strategies: What to show before they connect data so the app feels populated.
4. Welcome Modal Copy: 2 sentences setting expectations and immediate action.`,
    },
    {
      title: "Module 4: Social Media Authority & Distribution",
      promptsCount: "20 Prompts",
      desc: "Technical viral breakdowns, multi-platform repurposing engine, contrarian takes, and comment-to-DM conversion funnels.",
      sampleTitle: "Viral Technical LinkedIn & X Post Engine",
      sampleRole: "High-Impact B2B Content Creator",
      sampleCode: `Role: High-Impact B2B Content Creator.
Topic: How to build {{TECHNICAL_ARCHITECTURE}} using AI agents and modern APIs.

Format:
- Hook (Lines 1-2): Provocative observation about how 95% build this wrong.
- Context: The hidden cost of conventional setups.
- The 4-Step Solution Architecture: Bulleted, clean, technical depth without buzzwords.
- The Golden Rule: One memorable philosophical takeaway.
- Call to Conversation: An engaging, open-ended technical question.`,
    },
    {
      title: "Module 5: Retention, Churn Prevention & Expansion",
      promptsCount: "20 Prompts",
      desc: "Predictive churn intervention telemetry, automated executive QBR presentations, champion departure playbooks, and NRR optimization.",
      sampleTitle: "Predictive Churn Intervention System",
      sampleRole: "Head of Customer Success",
      sampleCode: `Role: Head of Customer Success.
Trigger: Account {{ACCOUNT_NAME}} has exhibited the following telemetry:
- Login frequency down 45% over 14 days
- Unopened ticket on critical integration
- Key champion changed role on LinkedIn

Action Plan:
1. Immediate triage internal alert for CSM with account context.
2. Direct, empathetic email from founder/VP to executive sponsor.
3. Concrete offer: Free engineering audit / custom configuration call.`,
    },
  ];

  const sops = [
    {
      number: "01",
      title: "The Autonomous Weekly B2B Content Engine",
      time: "45 mins/week",
      impact: "1 Pillar + 5 Social Posts + 1 Newsletter on autopilot",
      desc: "Generates high-intent pillar thought leadership, splits into multi-channel micro-assets, and feeds directly into the Zernio distribution engine.",
    },
    {
      number: "02",
      title: "Real-Time Competitor Intelligence & Counter-Positioning",
      time: "48-hr turnaround",
      impact: "Zero lost deals to positioning blindsides",
      desc: "Monitors competitor pricing/feature changelogs, crafts defensible battlecards, and generates BOFU comparison pages.",
    },
    {
      number: "03",
      title: "Cold Outbound Dynamic ICP Scoring & Personalization",
      time: "100% Automated",
      impact: "18.4% Average Reply Rate",
      desc: "Pipes hiring, funding, and tech stack triggers directly into structured prompt templates for zero-fluff cold sequences.",
    },
    {
      number: "04",
      title: "Churn Risk Flagging & Automated Interventions",
      time: "Real-time Telemetry",
      impact: "35% Voluntary Churn Reduction",
      desc: "Detects drop in usage frequency and automatically triggers empathetic founder-tier re-engagement workflows.",
    },
  ];

  const testimonials = [
    {
      quote:
        "The outbound prompt architecture alone booked 14 discovery calls in our first 10 days using the Zernio poster. It replaced a $6,000/month SDR agency.",
      name: "Marcus Vance",
      title: "Founder & CEO, ScaleMetrics (Series A SaaS)",
      rating: 5,
    },
    {
      quote:
        "Finally, someone created prompts that aren't fluffy garbage. Every single prompt has strict role definitions, input constraints, and output JSON schemas.",
      name: "Elena Rostova",
      title: "VP of Growth, HyperFlow Security",
      rating: 5,
    },
    {
      quote:
        "The automated Python distribution engine with Zernio unified our X and LinkedIn workflows seamlessly. The SOPs are our new company operating manual.",
      name: "David Chen",
      title: "Head of Marketing, CloudKernel",
      rating: 5,
    },
  ];

  const faqs = [
    {
      q: "What format do I receive the product in?",
      a: "You receive the complete production asset as a clean, structured Markdown file (`product_asset.md`), along with the Python distribution engine source code (`auto_poster.py`), promotional data CSV, and comprehensive documentation for instant deployment.",
    },
    {
      q: "Which AI models are these prompts designed for?",
      a: "They are optimized for modern frontier models including Anthropic Claude 3.5 / 3.7 Sonnet, OpenAI GPT-4o / o1 / o3, and Google Gemini 1.5 / 2.0 Pro. Every prompt includes explicit role framing, few-shot structures, and schema boundaries.",
    },
    {
      q: "Can I use these prompts commercially for my clients or agency?",
      a: "Yes! Your purchase includes a full Commercial Implementation License. You can run these prompts, build client deliverables, and deploy them across your internal teams and client accounts.",
    },
    {
      q: "How does the Python social media distribution engine work?",
      a: "It utilizes the Zernio unified marketing API SDK (`zernio-sdk`). Instead of maintaining separate OAuth tokens for X, LinkedIn, etc., you pass one API key and the script schedules or publishes promotional posts directly from a configurable CSV queue.",
    },
    {
      q: "What is your refund policy?",
      a: "We offer a 30-day no-questions-asked money-back guarantee. If you don't book meetings or save at least 20 hours in your first month, send an email and receive a 100% refund immediately.",
    },
  ];

  const copyToClipboard = (text: string, index: number) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  // ROI Calculator Math
  const hoursSavedPerWeek = teamSize * 8;
  const monthlySavings = hoursSavedPerWeek * 4 * 75; // Assuming $75/hr blended rate

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-indigo-600 selection:text-white">
      {/* Top Banner */}
      <div className="bg-gradient-to-r from-indigo-700 via-purple-700 to-indigo-800 text-white text-xs sm:text-sm font-medium py-2.5 px-4 text-center sticky top-0 z-50 shadow-md">
        <span className="inline-flex items-center gap-1.5">
          <span className="bg-amber-400 text-slate-950 font-bold px-2 py-0.5 rounded text-[11px] uppercase tracking-wider">
            Launch Special
          </span>
          <span>
            Get <strong>68% OFF</strong> the Full Playbook + Python Engine —
            Only <strong>37 copies</strong> left at $47!
          </span>
        </span>
      </div>

      {/* Navigation */}
      <header className="border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-md sticky top-[37px] z-40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded-lg bg-indigo-600 flex items-center justify-center text-white shadow-lg shadow-indigo-500/30">
              <Bot className="w-5 h-5" />
            </div>
            <div>
              <span className="font-bold text-lg tracking-tight bg-gradient-to-r from-white via-slate-100 to-slate-400 bg-clip-text text-transparent">
                Autonomous AI Growth
              </span>
              <span className="hidden sm:inline-block ml-2 text-[10px] text-indigo-400 font-semibold px-2 py-0.5 border border-indigo-500/30 rounded-full bg-indigo-950/50">
                2026 EDITION
              </span>
            </div>
          </div>

          <nav className="hidden md:flex items-center gap-7 text-sm font-medium text-slate-400">
            <a href="#modules" className="hover:text-white transition-colors">
              The 100 Prompts
            </a>
            <a href="#sops" className="hover:text-white transition-colors">
              Production SOPs
            </a>
            <a href="#calculator" className="hover:text-white transition-colors">
              ROI Calculator
            </a>
            <a href="#pricing" className="hover:text-white transition-colors text-emerald-400 font-semibold">
              B2B Lead Vault
            </a>
            <a href="#faq" className="hover:text-white transition-colors">
              FAQ
            </a>
          </nav>

          <a
            href={GUMROAD_CHECKOUT_URL}
            className="gumroad-button bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm px-4 py-2 rounded-lg shadow-md shadow-indigo-600/20 hover:shadow-indigo-600/40 transition-all flex items-center gap-1.5"
          >
            <span>Get Instant Access</span>
            <ArrowRight className="w-4 h-4" />
          </a>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative pt-20 pb-24 overflow-hidden">
        {/* Glow Background Elements */}
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[400px] bg-indigo-600/15 blur-[120px] rounded-full pointer-events-none -z-10" />
        <div className="absolute top-1/3 left-1/4 w-[400px] h-[300px] bg-purple-600/10 blur-[100px] rounded-full pointer-events-none -z-10" />

        <div className="max-w-5xl mx-auto px-4 sm:px-6 text-center">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full border border-indigo-500/30 bg-indigo-950/40 text-indigo-300 text-xs font-semibold mb-6 animate-pulse">
            <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
            <span>The Enterprise AI Revenue System for B2B Tech</span>
          </div>

          <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-white leading-[1.1] mb-6">
            Stop Burning CAC on Guesswork. <br className="hidden sm:inline" />
            Deploy <span className="bg-gradient-to-r from-indigo-400 via-purple-300 to-pink-400 bg-clip-text text-transparent">Autonomous AI Growth</span> Systems.
          </h1>

          <p className="max-w-3xl mx-auto text-lg sm:text-xl text-slate-300 leading-relaxed mb-10">
            <strong>100 Battle-Tested AI Prompts</strong>, <strong>4 End-to-End SOPs</strong>, and a ready-to-run <strong>Python Social Media Distribution Engine</strong> built for founders, marketers, and pipeline engineers who need qualified revenue, not fluff.
          </p>

          {/* CTA Box */}
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-10">
            <a
              href={GUMROAD_CHECKOUT_URL}
              className="gumroad-button w-full sm:w-auto inline-flex items-center justify-center gap-2.5 px-8 py-4 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white font-bold text-lg shadow-xl shadow-indigo-600/30 hover:scale-[1.02] active:scale-[0.98] transition-all"
            >
              <Zap className="w-5 h-5 text-amber-300 fill-amber-300" />
              <span>Download Complete Playbook — $47</span>
              <span className="text-xs bg-indigo-950/60 text-indigo-200 px-2 py-0.5 rounded ml-1 border border-indigo-400/30">
                Was $147
              </span>
            </a>
            <a
              href="#preview"
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-4 rounded-xl border border-slate-700 bg-slate-900/60 hover:bg-slate-800 text-slate-200 font-medium text-base transition-all"
            >
              <span>Inspect Prompt Previews</span>
              <ChevronDown className="w-4 h-4 text-slate-400" />
            </a>
          </div>

          {/* Social Proof Badges */}
          <div className="flex flex-wrap items-center justify-center gap-6 text-xs text-slate-400">
            <div className="flex items-center gap-1.5">
              <div className="flex text-amber-400">
                {[...Array(5)].map((_, i) => (
                  <Star key={i} className="w-4 h-4 fill-amber-400 text-amber-400" />
                ))}
              </div>
              <span className="font-semibold text-slate-200">4.9/5</span>
              <span>(320+ B2B Leaders)</span>
            </div>
            <div className="flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              <span>30-Day Money-Back Guarantee</span>
            </div>
            <div className="flex items-center gap-1.5">
              <Terminal className="w-4 h-4 text-indigo-400" />
              <span>Includes Python Automation Engine</span>
            </div>
          </div>
        </div>

        {/* Metrics Banner */}
        <div className="max-w-6xl mx-auto px-4 sm:px-6 mt-16">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-6 rounded-2xl bg-slate-900/50 border border-slate-800 backdrop-blur-sm">
            <div className="text-center p-3 border-r border-slate-800/80 last:border-none">
              <div className="text-2xl sm:text-3xl font-extrabold text-indigo-400">100</div>
              <div className="text-xs sm:text-sm text-slate-400 mt-1">Structured AI Prompts</div>
            </div>
            <div className="text-center p-3 md:border-r border-slate-800/80 last:border-none">
              <div className="text-2xl sm:text-3xl font-extrabold text-purple-400">18.4%</div>
              <div className="text-xs sm:text-sm text-slate-400 mt-1">Avg Outbound Reply Rate</div>
            </div>
            <div className="text-center p-3 border-r border-slate-800/80 last:border-none">
              <div className="text-2xl sm:text-3xl font-extrabold text-emerald-400">45 Mins</div>
              <div className="text-xs sm:text-sm text-slate-400 mt-1">Weekly Content SOP Time</div>
            </div>
            <div className="text-center p-3">
              <div className="text-2xl sm:text-3xl font-extrabold text-pink-400">Unified</div>
              <div className="text-xs sm:text-sm text-slate-400 mt-1">Multi-Channel Zernio API</div>
            </div>
          </div>
        </div>
      </section>

      {/* Problem vs Solution Section */}
      <section className="py-20 border-t border-slate-900 bg-slate-950/60">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-3xl mx-auto mb-14">
            <h2 className="text-xs font-bold tracking-widest text-indigo-400 uppercase mb-2">
              Why Most B2B AI Strategies Fail
            </h2>
            <h3 className="text-3xl sm:text-4xl font-extrabold text-white">
              The Era of Lazy ChatGPT Copy Is Over.
            </h3>
            <p className="text-slate-400 mt-3 text-base">
              Prospects detect unconstrained AI copy in seconds. True enterprise efficiency requires systematic prompt engineering, rigorous constraints, and automated publishing.
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {/* The Old Way */}
            <div className="rounded-2xl p-8 bg-red-950/10 border border-red-900/30">
              <div className="text-red-400 font-bold text-sm tracking-wide uppercase mb-4 flex items-center gap-2">
                <span>✕ The Fragile Guesswork Way</span>
              </div>
              <ul className="space-y-4 text-slate-300 text-sm">
                <li className="flex items-start gap-3">
                  <span className="text-red-500 font-bold">✕</span>
                  <span>Writing vague, unconstrained prompts that spit out repetitive, generic buzzwords.</span>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-red-500 font-bold">✕</span>
                  <span>Cold emails burning domain reputation with 0.8% reply rates.</span>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-red-500 font-bold">✕</span>
                  <span>Copying and pasting between ChatGPT and 5 different social media tools manually.</span>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-red-500 font-bold">✕</span>
                  <span>Paying \$5,000 to \$10,000/mo for agencies who use the exact same outdated templates.</span>
                </li>
              </ul>
            </div>

            {/* The Autonomous Growth Engine */}
            <div className="rounded-2xl p-8 bg-indigo-950/20 border border-indigo-500/40 relative shadow-xl shadow-indigo-950/40">
              <div className="text-indigo-400 font-bold text-sm tracking-wide uppercase mb-4 flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-indigo-400" />
                <span>✓ The Autonomous AI Growth System</span>
              </div>
              <ul className="space-y-4 text-slate-300 text-sm">
                <li className="flex items-start gap-3">
                  <span className="text-indigo-400 font-bold">✓</span>
                  <span>100 production-tested prompts with strict role framing, variable slots, and JSON outputs.</span>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-indigo-400 font-bold">✓</span>
                  <span>Signal-based trigger emails delivering verified 18%+ reply rates on enterprise accounts.</span>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-indigo-400 font-bold">✓</span>
                  <span>Python distribution engine that automatically publishes scheduled promotional tips via Zernio SDK.</span>
                </li>
                <li className="flex items-start gap-3">
                  <span className="text-indigo-400 font-bold">✓</span>
                  <span>One-time purchase of $47 with lifetime updates and zero recurring agency retainers.</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive Module Explorer / Prompt Previews */}
      <section id="modules" className="py-20 border-t border-slate-900 bg-slate-900/30">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <h2 className="text-xs font-bold tracking-widest text-indigo-400 uppercase mb-2">
              Inside the 100-Prompt Asset
            </h2>
            <h3 className="text-3xl sm:text-4xl font-extrabold text-white">
              Explore the 5 Core Growth Pillars
            </h3>
            <p className="text-slate-400 mt-3 text-base">
              Every single prompt is engineered for high-intent B2B conversion. Select a module below to inspect sample system instructions.
            </p>
          </div>

          {/* Module Tabs */}
          <div className="flex flex-wrap gap-2 justify-center mb-8">
            {modules.map((m, idx) => (
              <button
                key={idx}
                onClick={() => setActiveTab(idx)}
                className={`px-4 py-2.5 rounded-xl text-xs sm:text-sm font-semibold transition-all cursor-pointer ${
                  activeTab === idx
                    ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/30"
                    : "bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800"
                }`}
              >
                {m.title.split(":")[0]} ({m.promptsCount})
              </button>
            ))}
          </div>

          {/* Active Module Card */}
          <div className="rounded-2xl border border-slate-800 bg-slate-950/80 p-6 sm:p-8 backdrop-blur-md">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800/80">
              <div>
                <h4 className="text-xl sm:text-2xl font-bold text-white">
                  {modules[activeTab].title}
                </h4>
                <p className="text-sm text-slate-400 mt-1">{modules[activeTab].desc}</p>
              </div>
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-950 border border-indigo-500/30 text-indigo-300 text-xs font-mono">
                <span>{modules[activeTab].promptsCount}</span>
              </div>
            </div>

            {/* Prompt Code Display */}
            <div className="mt-6">
              <div className="flex items-center justify-between text-xs text-slate-400 mb-2 font-mono">
                <span className="flex items-center gap-1.5">
                  <Terminal className="w-3.5 h-3.5 text-indigo-400" />
                  <span>Sample Prompt: {modules[activeTab].sampleTitle}</span>
                </span>
                <button
                  onClick={() => copyToClipboard(modules[activeTab].sampleCode, activeTab)}
                  className="flex items-center gap-1 text-indigo-400 hover:text-indigo-300 transition-colors cursor-pointer"
                >
                  {copiedIndex === activeTab ? (
                    <>
                      <Check className="w-3.5 h-3.5 text-emerald-400" />
                      <span className="text-emerald-400">Copied!</span>
                    </>
                  ) : (
                    <>
                      <Copy className="w-3.5 h-3.5" />
                      <span>Copy Template</span>
                    </>
                  )}
                </button>
              </div>
              <pre className="p-4 sm:p-6 rounded-xl bg-slate-900 border border-slate-800 font-mono text-xs sm:text-sm text-slate-300 overflow-x-auto whitespace-pre leading-relaxed">
                <code>{modules[activeTab].sampleCode}</code>
              </pre>
            </div>
          </div>
        </div>
      </section>

      {/* Production SOPs Section */}
      <section id="sops" className="py-20 border-t border-slate-900">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-3xl mx-auto mb-14">
            <h2 className="text-xs font-bold tracking-widest text-indigo-400 uppercase mb-2">
              Autonomous Operating Procedures
            </h2>
            <h3 className="text-3xl sm:text-4xl font-extrabold text-white">
              Turn Prompts Into Predictable Revenue
            </h3>
            <p className="text-slate-400 mt-3 text-base">
              A prompt without an SOP is just an idea. These 4 battle-tested SOPs define exact trigger events, model pipelines, and human quality gates.
            </p>
          </div>

          <div className="grid sm:grid-cols-2 gap-6">
            {sops.map((sop, idx) => (
              <div
                key={idx}
                className="p-6 rounded-2xl bg-slate-900/40 border border-slate-800/80 hover:border-slate-700 transition-all flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-center justify-between mb-3">
                    <span className="text-2xl font-black text-indigo-500/60 font-mono">
                      {sop.number}
                    </span>
                    <span className="text-[11px] font-semibold text-emerald-400 bg-emerald-950/60 border border-emerald-500/30 px-2 py-0.5 rounded-full">
                      {sop.time}
                    </span>
                  </div>
                  <h4 className="text-lg font-bold text-white mb-2">{sop.title}</h4>
                  <p className="text-sm text-slate-400 leading-relaxed mb-4">{sop.desc}</p>
                </div>
                <div className="pt-3 border-t border-slate-800 text-xs text-indigo-300 font-medium flex items-center gap-1.5">
                  <TrendingUp className="w-3.5 h-3.5 text-indigo-400" />
                  <span>Impact: {sop.impact}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Python Social Media Distribution Engine Feature */}
      <section id="engine" className="py-20 border-t border-slate-900 bg-slate-900/40">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-purple-500/30 bg-purple-950/40 text-purple-300 text-xs font-semibold mb-4">
                <Cpu className="w-3.5 h-3.5 text-purple-400" />
                <span>Phase 3 Inclusion: Unified API Engine</span>
              </div>
              <h3 className="text-3xl sm:text-4xl font-extrabold text-white mb-6 leading-tight">
                Automated Social Media Distribution via Zernio SDK
              </h3>
              <p className="text-slate-300 leading-relaxed mb-6">
                Never log into 5 different social media tabs again. This package includes a turnkey Python distribution engine (`auto_poster.py`) that reads scheduled high-converting promotional hooks from CSV and dispatches them across X and LinkedIn via a single API call.
              </p>

              <div className="space-y-3 mb-8">
                <div className="flex items-center gap-2.5 text-sm text-slate-200">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                  <span>Unified REST infrastructure (zero OAuth headaches)</span>
                </div>
                <div className="flex items-center gap-2.5 text-sm text-slate-200">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                  <span>Built-in dry-run mode for testing without publishing</span>
                </div>
                <div className="flex items-center gap-2.5 text-sm text-slate-200">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                  <span>Pre-populated `promotional_tips.csv` with ready-to-run hooks</span>
                </div>
                <div className="flex items-center gap-2.5 text-sm text-slate-200">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                  <span>Secure environment configuration (`.env` & `.gitignore`)</span>
                </div>
              </div>

              <a
                href={GUMROAD_CHECKOUT_URL}
                className="gumroad-button inline-flex items-center gap-2 px-6 py-3.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-semibold text-sm shadow-lg shadow-purple-600/30 transition-all"
              >
                <span>Get Script & Prompt Bundle</span>
                <ArrowRight className="w-4 h-4" />
              </a>
            </div>

            {/* Code Snippet Box */}
            <div className="rounded-2xl border border-slate-800 bg-slate-950 p-6 shadow-2xl">
              <div className="flex items-center justify-between pb-3 border-b border-slate-800 text-xs text-slate-400 font-mono mb-4">
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 rounded-full bg-red-500/80" />
                  <div className="w-3 h-3 rounded-full bg-amber-500/80" />
                  <div className="w-3 h-3 rounded-full bg-emerald-500/80" />
                  <span className="ml-2 text-slate-300">distribution_engine/auto_poster.py</span>
                </div>
                <span className="text-[11px] text-purple-400">Python 3.12</span>
              </div>
              <pre className="font-mono text-xs text-slate-300 overflow-x-auto leading-relaxed">
{`import os
from zernio import Zernio

# Initialize unified social API client
client = Zernio(api_key=os.environ["ZERNIO_API_KEY"])

# Single endpoint publishes across multiple channels
result = client.posts.create_post(
    content="Stop burning CAC on guesswork. Here is our 4-step autonomous SOP...",
    platforms=[
        {"platform": "linkedin", "accountId": "YOUR_ACCOUNT_ID"},
        {"platform": "x", "accountId": "YOUR_ACCOUNT_ID"}
    ],
    publish_now=True
)
print(f"Posted successfully! ID: {result.post['_id']}")`}
              </pre>
            </div>
          </div>
        </div>
      </section>

      {/* Interactive ROI Calculator */}
      <section id="calculator" className="py-20 border-t border-slate-900">
        <div className="max-w-4xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-2xl mx-auto mb-10">
            <h2 className="text-xs font-bold tracking-widest text-indigo-400 uppercase mb-2">
              Interactive Value Modeling
            </h2>
            <h3 className="text-3xl sm:text-4xl font-extrabold text-white">
              Calculate Your Team’s Monthly ROI
            </h3>
            <p className="text-slate-400 mt-2 text-sm">
              See how many hours and dollars your team saves by switching from manual copywriting to autonomous agents.
            </p>
          </div>

          <div className="p-8 rounded-2xl bg-slate-900/60 border border-slate-800 shadow-xl">
            <div className="mb-8">
              <div className="flex justify-between items-center mb-3">
                <label className="text-sm font-semibold text-slate-200">
                  Number of Team Members Generating Content or Outbound:
                </label>
                <span className="text-lg font-bold text-indigo-400 font-mono">
                  {teamSize} {teamSize === 1 ? "person" : "people"}
                </span>
              </div>
              <input
                type="range"
                min="1"
                max="20"
                value={teamSize}
                onChange={(e) => setTeamSize(parseInt(e.target.value))}
                className="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-indigo-500"
              />
              <div className="flex justify-between text-[11px] text-slate-500 mt-1">
                <span>1 Solo Founder</span>
                <span>10 Growth Team</span>
                <span>20 Enterprise Unit</span>
              </div>
            </div>

            <div className="grid sm:grid-cols-2 gap-6 pt-6 border-t border-slate-800 text-center">
              <div className="p-5 rounded-xl bg-slate-950/80 border border-slate-800">
                <div className="text-xs text-slate-400 mb-1 flex items-center justify-center gap-1">
                  <Clock className="w-3.5 h-3.5 text-indigo-400" />
                  <span>Time Reclaimed Weekly</span>
                </div>
                <div className="text-3xl sm:text-4xl font-extrabold text-white font-mono">
                  {hoursSavedPerWeek} hrs
                </div>
                <div className="text-[11px] text-slate-500 mt-1">~8 hours saved per team member</div>
              </div>

              <div className="p-5 rounded-xl bg-slate-950/80 border border-indigo-500/30">
                <div className="text-xs text-slate-400 mb-1 flex items-center justify-center gap-1">
                  <DollarSign className="w-3.5 h-3.5 text-emerald-400" />
                  <span>Estimated Monthly Value Saved</span>
                </div>
                <div className="text-3xl sm:text-4xl font-extrabold text-emerald-400 font-mono">
                  ${monthlySavings.toLocaleString()}
                </div>
                <div className="text-[11px] text-slate-500 mt-1">
                  Based on standard $75/hr blended capacity rate
                </div>
              </div>
            </div>

            <div className="mt-8 text-center">
              <a
                href={GUMROAD_CHECKOUT_URL}
                className="gumroad-button inline-flex items-center gap-2 px-8 py-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm shadow-lg shadow-indigo-600/30 transition-all"
              >
                <span>Unlock These Savings for $47</span>
                <ArrowRight className="w-4 h-4" />
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-20 border-t border-slate-900 bg-slate-900/20">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-2xl mx-auto mb-14">
            <h2 className="text-xs font-bold tracking-widest text-indigo-400 uppercase mb-2">
              Verified Feedback
            </h2>
            <h3 className="text-3xl sm:text-4xl font-extrabold text-white">
              Trusted by 320+ B2B Operators
            </h3>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {testimonials.map((t, idx) => (
              <div
                key={idx}
                className="p-6 rounded-2xl bg-slate-900/50 border border-slate-800/90 flex flex-col justify-between"
              >
                <div>
                  <div className="flex text-amber-400 mb-4">
                    {[...Array(t.rating)].map((_, i) => (
                      <Star key={i} className="w-4 h-4 fill-amber-400 text-amber-400" />
                    ))}
                  </div>
                  <p className="text-slate-300 text-sm leading-relaxed mb-6 italic">
                    "{t.quote}"
                  </p>
                </div>
                <div className="pt-4 border-t border-slate-800/80">
                  <div className="font-bold text-white text-sm">{t.name}</div>
                  <div className="text-xs text-indigo-400 mt-0.5">{t.title}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing / Checkout Embed Section */}
      <section id="pricing" className="py-20 border-t border-slate-900 bg-slate-950">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-2xl mx-auto mb-14">
            <h2 className="text-xs font-bold tracking-widest text-indigo-400 uppercase mb-2">
              Autonomous Growth Catalog
            </h2>
            <h3 className="text-3xl sm:text-4xl font-extrabold text-white">
              Instant Access Solutions
            </h3>
            <p className="text-slate-400 mt-2 text-sm">
              Zero recurring fees. 100% production-ready source code, prompts, and actionable market intelligence.
            </p>
          </div>

          {/* Products Grid */}
          <div className="grid lg:grid-cols-2 gap-8">
            {/* Card 1: AI Growth Engine */}
            <div className="rounded-3xl border-2 border-indigo-500/50 bg-gradient-to-b from-slate-900 via-slate-900/90 to-slate-950 p-8 sm:p-10 shadow-2xl relative overflow-hidden flex flex-col justify-between">
              <div className="absolute top-0 right-0 bg-indigo-600 text-white text-[11px] font-bold px-4 py-1.5 rounded-bl-xl uppercase tracking-wider">
                Product Hunt Featured
              </div>

              <div>
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-indigo-500/30 bg-indigo-950/40 text-indigo-300 text-xs font-semibold mb-4">
                  <Bot className="w-3.5 h-3.5 text-indigo-400" />
                  <span>Flagship AI Prompt & Code Bundle</span>
                </div>
                <h4 className="text-2xl font-black text-white mb-2">
                  The Autonomous AI Growth Engine
                </h4>
                <p className="text-slate-400 text-sm leading-relaxed mb-6">
                  100 schema-enforced enterprise prompts across 5 core growth stages, 4 end-to-end production SOPs, and full Python multi-channel auto-poster source code.
                </p>

                <div className="flex items-baseline gap-2 mb-6">
                  <span className="text-slate-500 line-through text-lg font-bold">$147</span>
                  <span className="text-4xl font-black text-white tracking-tight">$47</span>
                  <span className="text-xs text-slate-400">USD (or $29 with code PRODUCTHUNT)</span>
                </div>

                <div className="space-y-3 py-6 border-y border-slate-800 text-sm">
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>100 Structured Prompts</strong> across 5 modules</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>4 Battle-Tested SOPs</strong> with metrics & schemas</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>Python Zernio Engine</strong> (`auto_poster.py`)</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>Curated Promotional CSV</strong> with viral hooks</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>Commercial License</strong> & Lifetime Updates</span>
                  </div>
                </div>
              </div>

              <div className="mt-8">
                <a
                  href={GUMROAD_CHECKOUT_URL}
                  className="gumroad-button w-full inline-flex items-center justify-center gap-2.5 px-6 py-4 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:opacity-95 text-white font-bold text-base shadow-lg shadow-indigo-600/30 transition-all text-center"
                >
                  <span>Get Growth Engine ($47)</span>
                  <ArrowRight className="w-4 h-4" />
                </a>
                <div className="mt-4 flex items-center justify-center gap-4 text-xs text-slate-400">
                  <span className="flex items-center gap-1.5">
                    <ShieldCheck className="w-4 h-4 text-emerald-400" />
                    <span>Instant Digital ZIP</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <Check className="w-4 h-4 text-indigo-400" />
                    <span>PDF + Markdown + Python</span>
                  </span>
                </div>
              </div>
            </div>

            {/* Card 2: Contractor & Home Service B2B Lead Vault */}
            <div className="rounded-3xl border-2 border-emerald-500/40 bg-gradient-to-b from-slate-900 via-slate-900/90 to-slate-950 p-8 sm:p-10 shadow-2xl relative overflow-hidden flex flex-col justify-between">
              <div className="absolute top-0 right-0 bg-emerald-600 text-white text-[11px] font-bold px-4 py-1.5 rounded-bl-xl uppercase tracking-wider">
                High-Yield Data Vault
              </div>

              <div>
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full border border-emerald-500/30 bg-emerald-950/40 text-emerald-300 text-xs font-semibold mb-4">
                  <Database className="w-3.5 h-3.5 text-emerald-400" />
                  <span>Verified B2B Market Intelligence</span>
                </div>
                <h4 className="text-2xl font-black text-white mb-2">
                  US Contractor & Home Services Lead Vault
                </h4>
                <p className="text-slate-400 text-sm leading-relaxed mb-6">
                  335+ verified local contractor businesses across Roofing, HVAC, Plumbing, & Electrical in 7 high-growth metro markets, complete with cold outreach scripts.
                </p>

                <div className="flex items-baseline gap-2 mb-6">
                  <span className="text-slate-500 line-through text-lg font-bold">$99</span>
                  <span className="text-4xl font-black text-white tracking-tight">$37</span>
                  <span className="text-xs text-slate-400">USD one-time</span>
                </div>

                <div className="space-y-3 py-6 border-y border-slate-800 text-sm">
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>335+ Direct Business Records</strong> (Austin, Dallas, Phoenix...)</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>Direct Contact Channels:</strong> Phone, Website, Physical Address</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>Aggregator-Free:</strong> 100% direct owner/operator domains</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>Contractor Outreach Playbook:</strong> Cold email & call scripts</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-200">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                    <span><strong>Dual Format:</strong> Clean CSV + Excel (.xlsx) ready for CRM</span>
                  </div>
                </div>
              </div>

              <div className="mt-8">
                <a
                  href={GUMROAD_LEAD_VAULT_URL}
                  className="gumroad-button w-full inline-flex items-center justify-center gap-2.5 px-6 py-4 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:opacity-95 text-white font-bold text-base shadow-lg shadow-emerald-600/30 transition-all text-center"
                >
                  <span>Get Contractor Vault ($37)</span>
                  <ArrowRight className="w-4 h-4" />
                </a>
                <div className="mt-4 flex items-center justify-center gap-4 text-xs text-slate-400">
                  <span className="flex items-center gap-1.5">
                    <ShieldCheck className="w-4 h-4 text-emerald-400" />
                    <span>Encrypted Checkout</span>
                  </span>
                  <span className="flex items-center gap-1.5">
                    <Check className="w-4 h-4 text-emerald-400" />
                    <span>Instant CSV + XLSX Download</span>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ Accordion */}
      <section id="faq" className="py-20 border-t border-slate-900 bg-slate-900/30">
        <div className="max-w-4xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-2xl mx-auto mb-14">
            <h2 className="text-xs font-bold tracking-widest text-indigo-400 uppercase mb-2">
              Got Questions?
            </h2>
            <h3 className="text-3xl sm:text-4xl font-extrabold text-white">
              Frequently Asked Questions
            </h3>
          </div>

          <div className="space-y-4">
            {faqs.map((faq, idx) => {
              const isOpen = activeFaq === idx;
              return (
                <div
                  key={idx}
                  className="rounded-xl border border-slate-800 bg-slate-950 overflow-hidden"
                >
                  <button
                    onClick={() => setActiveFaq(isOpen ? null : idx)}
                    className="w-full p-5 text-left font-semibold text-slate-200 hover:text-white flex items-center justify-between gap-4 cursor-pointer"
                  >
                    <span>{faq.q}</span>
                    {isOpen ? (
                      <ChevronUp className="w-4 h-4 text-indigo-400 flex-shrink-0" />
                    ) : (
                      <ChevronDown className="w-4 h-4 text-slate-500 flex-shrink-0" />
                    )}
                  </button>
                  {isOpen && (
                    <div className="px-5 pb-5 text-sm text-slate-400 leading-relaxed border-t border-slate-800/60 pt-3">
                      {faq.a}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Final Call to Action */}
      <section className="py-20 border-t border-slate-900 bg-gradient-to-b from-slate-950 to-indigo-950/40 text-center">
        <div className="max-w-3xl mx-auto px-4 sm:px-6">
          <h3 className="text-3xl sm:text-5xl font-black text-white tracking-tight mb-6">
            Ready to Automate Your B2B Growth?
          </h3>
          <p className="text-slate-300 text-lg mb-8 leading-relaxed">
            Join 320+ SaaS founders, marketers, and engineering leaders who have replaced expensive agencies with autonomous, production-ready AI workflows.
          </p>
          <a
            href={GUMROAD_CHECKOUT_URL}
            className="gumroad-button inline-flex items-center gap-2.5 px-9 py-4 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-lg shadow-xl shadow-indigo-600/40 transition-all"
          >
            <span>Get Instant Access ($47)</span>
            <ArrowRight className="w-5 h-5" />
          </a>
          <p className="text-xs text-slate-500 mt-4">
            30-Day Money-Back Guarantee • Instant Digital Download
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-900 py-10 bg-slate-950 text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-6 h-6 rounded bg-indigo-600 flex items-center justify-center text-white">
              <Bot className="w-3.5 h-3.5" />
            </div>
            <span className="font-semibold text-slate-300">
              Autonomous AI Growth Engine
            </span>
            <span>© 2026 AI Growth Engineering Labs</span>
          </div>
          <div className="flex items-center gap-6">
            <a href="#modules" className="hover:text-slate-300 transition-colors">
              Prompts
            </a>
            <a href="#sops" className="hover:text-slate-300 transition-colors">
              SOPs
            </a>
            <a href={GUMROAD_CHECKOUT_URL} className="hover:text-slate-300 transition-colors">
              AI Growth Engine ($47)
            </a>
            <a href={GUMROAD_LEAD_VAULT_URL} className="hover:text-emerald-400 transition-colors">
              Contractor B2B Vault ($37)
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}
