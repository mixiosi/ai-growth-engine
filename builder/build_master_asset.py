#!/usr/bin/env python3
"""
Master Asset & Deliverable Package Generator
Compiles 100 production AI prompts, 4 SOPs, generates executive PDF,
and packages the final customer release ZIP for Gumroad monetization.
"""

import os
import sys
import subprocess
import shutil
import zipfile
from pathlib import Path

BASE_DIR = Path("/home/bhadra/AI_Agent_Monetization")
RELEASE_DIR = BASE_DIR / "release"
DISTRIB_DIR = BASE_DIR / "distribution_engine"

def build_markdown_content():
    modules_data = [
        # MODULE 1
        ("Module 1: Autonomous Inbound & Search Authority", 1, 20, [
            ("Search-Intent Keyword Topology & Cluster Architect",
             "Senior SEO & Technical Content Strategist",
             "Create an exhaustive topic cluster map for {{TARGET_NICHE}} optimized for high buyer intent.",
             "1. Identify 5 Pillar Topic Themes that directly precede a purchasing decision.\n2. Under each Pillar, generate 4 Sub-topics (2 Informational, 1 Commercial Investigation, 1 Transactional).\n3. Map primary keywords, estimated search difficulty, and searcher intent stage (Awareness, Consideration, Decision).\n4. Define internal linking architecture connecting all 4 sub-articles back to the primary conversion page.",
             "Structured Markdown table with Columns: [Pillar, Sub-Topic Title, Search Intent, Target Keyword, Primary CTA]."),

            ("First-Principles B2B Thought Leadership Op-Ed",
             "Founding CEO / Elite Tech Essayist",
             "Write an 1,800-word contrarian essay challenging {{CONVENTIONAL_INDUSTRY_BELIEF}}.",
             "1. Hook: Call out an accepted metric or practice in {{TARGET_INDUSTRY}} that actively destroys value.\n2. Root Cause Analysis: Break down the historical reason why this practice began and why modern shifts make it obsolete.\n3. First-Principles Framework: Introduce the {{NEW_PARADIGM_NAME}} with 3 clear operating rules.\n4. Tactical Implementation: Provide 2 real-world scenarios showing the before/after cost and outcome.\n5. Call to Action: Direct reader to audit their current process.",
             "Publication-ready Markdown with pull quotes, bold takeaways, and subheadings."),

            ("Programmatic Landing Page Copy Matrix",
             "Head of Growth & Conversion Rate Optimization",
             "Generate variable copy templates for {{NUMBER_OF_PAGES}} programmatic SEO comparison pages.",
             "1. Define variable tokens: {{CITY/REGION}}, {{INDUSTRY_VERTICAL}}, {{PRIMARY_COMPETITOR}}, {{PAIN_POINT}}.\n2. Craft 3 dynamic H1 variations emphasizing speed and ROI.\n3. Generate a 3-point feature comparison grid with dynamic pros/cons.\n4. Write 2 customer social proof testimonials with plug-and-play placeholders.\n5. Include sticky bottom banner CTA copy with urgency trigger.",
             "JSON Schema with keys: `h1_variants`, `value_props`, `comparison_table`, `testimonials`, `cta_copy`."),

            ("Competitive Battlecard & Comparison Page Generator",
             "Product Marketing Director (PMM)",
             "Construct an objective, high-converting '{{YOUR_PRODUCT}} vs. {{COMPETITOR_PRODUCT}}' comparison asset.",
             "1. Analyze {{COMPETITOR_PRODUCT}}'s top 3 weaknesses from G2/Capterra reviews.\n2. Frame feature differences around business outcomes (e.g. time saved, security, total cost) rather than feature lists.\n3. Write a 'When to Choose {{COMPETITOR}}' section to establish instant trust and unbiased authority.\n4. Write a 'Why High-Growth Teams Choose {{YOUR_PRODUCT}}' section.\n5. Add interactive FAQ answering pricing, migration difficulty, and contract lock-in.",
             "Clean Markdown comparison matrix followed by conversion copy."),

            ("High-Converting Whitepaper / Lead Magnet Outline",
             "Enterprise Content Architect",
             "Structure a 12-page definitive industry benchmark report on {{CORE_TOPIC}}.",
             "1. Executive Summary & State of {{TARGET_INDUSTRY}} in 2026.\n2. Proprietary Data Framework: 5 core quantitative benchmarks.\n3. The Cost of Inaction: Economic modeling of teams ignoring {{CORE_TOPIC}}.\n4. Step-by-Step Architectural Roadmap for Q1-Q4.\n5. Vendor Evaluation Checklist & Request for Proposal (RFP) template.",
             "Complete 12-section blueprint with word count targets and key takeaway bullet points."),

            ("BOFU Product Alternative / Versus Page Generator",
             "Growth Copywriter",
             "Generate a high-converting 'Top 5 Alternatives to {{LEGACY_SOFTWARE}} in 2026' guide.",
             "1. Identify the 3 critical pain points causing users to leave {{LEGACY_SOFTWARE}}.\n2. Profile Alternative 1 (Your Product) with distinct positioning as the modern agentic alternative.\n3. Profile Alternatives 2-4 objectively highlighting niche use-cases.\n4. Include a quick-decision matrix table.\n5. Add a 14-day zero-risk migration offer CTA.",
             "Markdown article optimized for search engines with SEO title and meta description."),

            ("Technical API / SDK Documentation Explainer",
             "Lead Developer Advocate",
             "Transform complex API endpoints for {{PRODUCT_API}} into an intuitive, developer-delighting guide.",
             "1. Provide a 3-line quickstart code snippet in Python, TypeScript, and cURL.\n2. Explain authentication, rate limits, and webhook event payloads with strict JSON schemas.\n3. Walk through the 'Happy Path' end-to-end tutorial with sample inputs and responses.\n4. Document edge-case error codes (400, 401, 429, 500) and recovery strategies.",
             "Markdown documentation formatted with syntax-highlighted code blocks."),

            ("Case Study & Customer Transformation Storyboard",
             "Customer Advocacy Lead",
             "Turn customer raw interview transcripts for {{CLIENT_COMPANY}} into an undeniable enterprise case study.",
             "1. The Bottleneck: Quantified operational pain before deploying {{YOUR_PRODUCT}}.\n2. The Evaluation: Why alternative solutions and in-house builds failed.\n3. The Rollout: 14-day implementation timeline and change management.\n4. The Quantified Payoff: 3 highlighted metrics (e.g. 4.2x Pipeline, 68% Cost Reduction).\n5. Executive Quote: 2 punchy soundbites from the VP of Engineering.",
             "Standard Case Study format: Summary Box, Problem, Solution, Results, Key Quotes."),

            ("Interactive Calculator / Assessment Lead Magnet Spec",
             "Product-Led Growth Engineer",
             "Design the logic, copy, and result tiers for an interactive ROI Calculator for {{TARGET_INDUSTRY}}.",
             "1. Define 4 numeric user inputs (Team Size, Avg Deal Size, Current Cycle Length, Tools Budget).\n2. Write mathematical formulas for Annual Loss to Inefficiency and Potential Savings.\n3. Create 3 personalized result outcome tiers (At Risk, Moderate, High Efficiency).\n4. Write gated email capture modal copy promising the custom 6-page PDF report.",
             "Form schema, JavaScript calculation formulas, and UI copy."),

            ("SaaS Feature Announcement & Release Note Engine",
             "VP of Product & Communications",
             "Draft a multi-channel launch kit for the release of {{NEW_FEATURE_NAME}}.",
             "1. Product Hunt / GitHub Release Changelog summary.\n2. In-App Notification pop-up copy (under 45 words with action CTA).\n3. Customer Success email to existing enterprise tiers.\n4. Public LinkedIn post framing the technical why behind the build.",
             "Grouped Markdown blocks labeled by channel and audience segment."),

            ("Topic Authority Gap & Content Decay Audit",
             "Principal SEO Strategist",
             "Audit existing URLs for {{COMPANY_DOMAIN}} and identify authority decay against competitors.",
             "1. Cross-reference search rankings drops over the past 180 days.\n2. Identify out-of-date statistics, missing schema markup, and broken intent matches.\n3. Provide surgical update instructions for each lagging URL (e.g. new sections, refreshed data, internal links).\n4. Generate priority score (High, Medium, Low) based on pipeline potential.",
             "Audit report table with actionable remediation checklist."),

            ("Schema-Enforced FAQ & Snippet Dominator",
             "Technical SEO Engineer",
             "Generate 10 high-intent FAQs with valid JSON-LD structured data for {{PRODUCT_PAGE_TOPIC}}.",
             "1. Select questions directly reflecting People Also Ask (PAA) and search engine queries.\n2. Write concise, definitive answers in 35-50 words optimized for AI search summaries.\n3. Provide valid JSON-LD Schema snippet ready to drop into Next.js `<head>`.",
             "FAQ text block followed by validated `<script type='application/ld+json'>` code."),

            ("Executive Ghostwriting LinkedIn / Newsletter Essay",
             "Ghostwriter to Fortune 500 Founders",
             "Draft a personal, vulnerable yet authoritative leadership essay for {{FOUNDER_NAME}} on {{PIVOTAL_MOMENT}}.",
             "1. Hook: Start in media res with a high-stakes decision or costly failure.\n2. The Uncomfortable Truth: Reveal an industry reality that most peers refuse to say publicly.\n3. The Paradigm Shift: Detail the exact moment perspective changed.\n4. Actionable Lessons: 3 tactical rules for leaders navigating similar growth phases.\n5. Closing question to drive executive comment discourse.",
             "900-word editorial essay formatted for Substack/LinkedIn Articles."),

            ("Developer Community Q&A & Forum Authority Builder",
             "Technical Community Evangelist",
             "Draft authoritative, non-promotional responses to common community questions regarding {{TECH_PROBLEM}}.",
             "1. Direct code solution resolving the developer's core friction immediately.\n2. Explanation of underlying memory, latency, or concurrency implications.\n3. Mention open-source libraries and best practices.\n4. Subtle mention of {{YOUR_TOOL}} only if natively relevant to simplifying the solution.",
             "Markdown answer ready for StackOverflow, Reddit, or Discord dev forums."),

            ("Industry Benchmark Report Synthesis Engine",
             "Chief Data Analyst",
             "Synthesize raw survey responses from {{SAMPLE_SIZE}} enterprise leaders into 5 macro trends.",
             "1. Trend identification with statistical confidence intervals.\n2. Contrarian discrepancies between what executives say vs what their teams deploy.\n3. Visual chart data tables ready for Figma/Infographic designers.\n4. Executive pull quotes explaining each statistical anomaly.",
             "Analytical report with executive takeaways and data visualizations."),

            ("B2B Video Teardown / Loom Script Architect",
             "Head of Product Marketing",
             "Write a 90-second asynchronous Loom video script auditing a prospect's current {{WORKFLOW_OR_PAGE}}.",
             "1. Seconds 0-15: Immediate pattern interrupt and personalized compliment on recent work.\n2. Seconds 15-45: Point out 2 hidden conversion bottlenecks on their screen.\n3. Seconds 45-75: Show how 2 peer companies solved this and 3x'd throughput.\n4. Seconds 75-90: Zero-pressure offer to send the full teardown framework.",
             "Two-column video script (Visual Cues | Spoken Dialogue)."),

            ("Interactive Infographic Data Storyboarding",
             "Visual Content Architect",
             "Storyboard an infographic detailing 'The Evolution of {{INDUSTRY_CATEGORY}}: 2015 to 2026'.",
             "1. 4 Era Breakdown (Manual -> Cloud -> Automation -> Autonomous Agents).\n2. Key bottlenecks, tooling stacks, and average cost per transaction per era.\n3. Wireframe notes for visual designers (color palette, typography, icon references).\n4. Accompanying social media caption summarizing the timeline.",
             "Structured storyboard specification with visual directions."),

            ("High-Intent Webinar & Masterclass Deck Outline",
             "Strategic Event Producer",
             "Build a 45-minute live masterclass deck teaching 'How to Automate {{CRITICAL_BUSINESS_PROCESS}}'.",
             "1. Slides 1-5: The Burning Platform (Why the old way is hemorrhaging budget).\n2. Slides 6-18: The 3-Pillar Autonomous Framework with live architecture demonstrations.\n3. Slides 19-32: Live teardown of a real enterprise workflow.\n4. Slides 33-40: The Commercial Offer & Limited Launch Incentive.\n5. Slides 41-45: Live Q&A prep for tough attendee objections.",
             "45-slide script outline with Slide Title, Visual Asset, Talking Points, and Audience Engagement Triggers."),

            ("Zero-Click Search Summary & Key Takeaway Generator",
             "AI Overview Optimization Specialist",
             "Summarize comprehensive guide on {{TOPIC}} into an AI-overview optimized definition block.",
             "1. 2-sentence direct definition answering 'What is {{TOPIC}}?'.\n2. Bulleted list of 4 essential operational components.\n3. Primary formula or calculation rule.\n4. Common misconception debunked in 1 sentence.",
             "HTML block wrapped in microdata tags `<div class='quick-definition'>`."),

            ("Inbound Lead Qualification Email Triage Matrix",
             "RevOps Automation Lead",
             "Classify inbound form submissions for {{PRODUCT_NAME}} into 3 automated response tiers.",
             "1. Tier 1 (Enterprise / High Intent): Instant Calendly link with VP of Solutions.\n2. Tier 2 (Mid-Market / Self-Serve): Automated sandbox workspace invite with personalized onboarding video.\n3. Tier 3 (Unqualified / Educational): Free prompt pack download and newsletter invite.\n4. Write email copy for each tier.",
             "Decision tree flowchart logic in Markdown + 3 complete email templates.")
        ]),

        # MODULE 2
        ("Module 2: High-Converting B2B Outbound & ABM Engines", 21, 40, [
            ("Signal-Based Hyper-Personalized Cold Email Generator",
             "Elite Outbound SDR & Pipeline Engineer",
             "Generate an under-85-word cold outreach email based on recent company trigger event {{TRIGGER_EVENT}}.",
             "1. Observation: State the verified trigger event and immediate technical friction.\n2. Insight: Explain how peer companies handled this bottleneck.\n3. Soft Offer: Offer a 2-page benchmark PDF or loom teardown.\n4. Constraints: Under 85 words, 5th-grade reading level, zero buzzwords.",
             "Plain text email draft with Subject Line (under 4 words)."),

            ("Account-Based Marketing (ABM) 1:1 Account Dossier",
             "Enterprise Account Executive & Strategist",
             "Construct an exhaustive account dossier on target account {{TARGET_ENTERPRISE}}.",
             "1. Tech stack breakdown (CRM, Analytics, Infrastructure, Agentic Tools).\n2. Key decision makers (CTO, VP Eng, VP Product) with recent public quotes or LinkedIn posts.\n3. 3 Strategic Business Initiatives from their latest 10-K / annual report.\n4. Value Hypothesis: Exactly where {{YOUR_PRODUCT}} generates >$500k in net value.",
             "Comprehensive Markdown Dossier with executive summary."),

            ("Multi-Touch 4-Step Omnichannel Sequence",
             "Sales Cadence Architect",
             "Write a 14-day multi-channel cadence (Email, LinkedIn, Voice) for {{TARGET_ICP}}.",
             "1. Day 1: Email 1 (Observation + Value Teaser).\n2. Day 3: LinkedIn Profile View + Thoughtful Comment on recent post.\n3. Day 7: Email 2 (Case Study with quantified metric from peer company).\n4. Day 10: LinkedIn Connection Request with personalized note.\n5. Day 14: Email 3 (Breakup email with resource gift).",
             "Complete sequence table with Day, Channel, Asset, and Exact Copy."),

            ("Re-engagement Sequence for 'Dark' Pipeline & Stalled Deals",
             "Senior Account Executive",
             "Revive deals for accounts that went ghost after a demo 45+ days ago.",
             "1. Rule: Never ask 'checking in' or 'touching base'.\n2. Introduce new external industry trigger or benchmark relevant to their use case.\n3. Announce major product upgrade that solves the specific hesitation raised during the demo.\n4. Low-friction exit: 'If priorities shifted, completely understand—should I close this file for now?'",
             "3-touch email cadence with subject lines and fallback SMS/LinkedIn notes."),

            ("Executive C-Suite Soft-Offer Email Framework",
             "Strategic Enterprise Advisor",
             "Draft a high-altitude email to the CEO/CIO of {{TARGET_ACCOUNT}} regarding {{CORE_INITIATIVE}}.",
             "1. Focus strictly on board-level metrics: EBITDA, risk reduction, operational headcount leverage.\n2. Reference peer CEO benchmark.\n3. Offer an executive peer roundtable invitation or private briefing rather than a product demo.\n4. Limit to 60 words.",
             "High-converting C-suite email copy with 2 subject line variations."),

            ("Technographic Migration Opportunity Outreach",
             "Competitive Replacement Specialist",
             "Target companies currently using {{LEGACY_COMPETITOR}} with a migration incentive.",
             "1. Highlight recent deprecation, price hike, or outage from {{LEGACY_COMPETITOR}}.\n2. Detail the exact zero-downtime migration path.\n3. Offer a migration credit matching remaining contract value.\n4. Soft CTA to review the 3-step migration blueprint.",
             "Targeted cold email sequence tailored to technographic data."),

            ("New Executive Hire Congratulatory Trigger Sequence",
             "Pipeline Generation Specialist",
             "Engage newly appointed {{EXECUTIVE_TITLE}} within their first 90 days at {{COMPANY_NAME}}.",
             "1. Congratulate on new role without being sycophantic.\n2. Acknowledge the common 'First 90 Days' mandate to audit tech stack and drive rapid impact.\n3. Provide the 'First 90 Days Quick-Wins Framework' tailored to their department.\n4. Offer a confidential peer benchmark call.",
             "2-step warm outreach sequence."),

            ("Hiring Freeze / Budget Optimization Value Pitch",
             "RevOps Financial Analyst",
             "Position {{YOUR_PRODUCT}} as an efficiency force multiplier during a hiring slowdown.",
             "1. Quantify how {{PRODUCT}} allows existing team of 5 to output the volume of 15.\n2. Detail cost comparison: $47k tool vs $350k fully loaded salaries.\n3. Highlight immediate ROI break-even timeline (< 21 days).\n4. Offer a CFO-ready business case calculation spreadsheet.",
             "Email and LinkedIn message focused on efficiency and cost savings."),

            ("Competitor Dissatisfaction Outreach (G2 / Capterra Complaints)",
             "Growth Hacker & Outbound Specialist",
             "Reach out to users leaving 2-star and 3-star reviews on {{COMPETITOR_NAME}}.",
             "1. Acknowledge known platform limitations (e.g. sluggish UI, terrible support, hidden fees) without naming the review directly.\n2. Present how {{YOUR_PRODUCT}} re-engineered that exact workflow from scratch.\n3. Offer a 30-day VIP onboarding guarantee with dedicated engineering channel.",
             "High-converting outbound template with customizable complaint tokens."),

            ("Post-Webinar / Event Attendee Conversion Sequence",
             "Event Monetization Specialist",
             "Convert attendees of {{WEBINAR_TOPIC}} into qualified pipeline within 48 hours.",
             "1. Segment into: Highly Engaged (Stayed >30 mins), Partial, and No-Show.\n2. Deliver personalized replay link + supplementary template download.\n3. Highlight the #1 question asked during Q&A and provide extended answer.\n4. Include invitation to apply the framework to their custom workspace.",
             "3 tailored follow-up emails based on attendee attendance behavior."),

            ("Mutual Connection & Social Signal Referral Opener",
             "Relationship-Led Sales Strategist",
             "Craft an authentic warm referral email referencing mutual connection {{MUTUAL_NAME}}.",
             "1. State connection context clearly in first sentence.\n2. Share specific insight {{MUTUAL_NAME}} mentioned regarding their current priority.\n3. Bridge to single high-value resource without aggressive sales pitch.\n4. Permission-based closing sentence.",
             "Warm referral email template + LinkedIn note."),

            ("Inbound Form Abandonment Recovery Campaign",
             "Lifecycle Marketing Specialist",
             "Recover high-intent prospects who started the demo request or checkout form but abandoned.",
             "1. Send within 25 minutes of drop-off.\n2. Subject: 'Quick question about {{COMPANY_NAME}}'s setup'.\n3. Inquire if they ran into technical trouble or needed specific security documentation.\n4. Provide a direct 1-click scheduler link.",
             "2-email rapid recovery sequence."),

            ("Cold LinkedIn Voice Note / Short Video Script",
             "Modern SDR Coach",
             "Write a 30-second conversational voice note script for LinkedIn outreach to {{PROSPECT_NAME}}.",
             "1. Casual, non-rehearsed tone.\n2. Immediate specific reference to a post or podcast they participated in.\n3. One-sentence insight on {{PROBLEM}}.\n4. Casual sign-off asking if they want a 1-minute loom or PDF.",
             "Voice script with pacing, emphasis marks, and pause annotations."),

            ("Multi-Threading Matrix: Reaching 3 Decision Makers Simultaneously",
             "Enterprise Account Strategist",
             "Write coordinated, simultaneous emails to the CTO, CFO, and Head of Marketing at {{TARGET_COMPANY}}.",
             "1. CTO Email: Focus on security, API throughput, architecture simplicity.\n2. CFO Email: Focus on software consolidation, ROI, payback period.\n3. Marketing Head Email: Focus on velocity, conversion rate, team autonomy.\n4. Cross-reference internal alignment between departments.",
             "3 aligned email templates designed to be dispatched on the same morning."),

            ("The 'Anti-Sales' Honest Assessment Email",
             "Challenger Sales Practitioner",
             "Write a radically candid email evaluating if {{TARGET_COMPANY}} is actually a fit for {{YOUR_PRODUCT}}.",
             "1. List 3 scenarios where they should NOT buy your product.\n2. List the 1 scenario where your product delivers exponential ROI.\n3. Ask them directly which bucket they fall into.\n4. Contrast with traditional aggressive sales tactics to earn instant respect.",
             "Provocative, high-reply-rate email draft."),

            ("High-Converting Custom ROI Proposal Teardown",
             "Commercial Deal Architect",
             "Structure a 1-page executive deal summary for the buying committee at {{PROSPECT_COMPANY}}.",
             "1. Problem Statement: Current quantifiable cost ($/mo).\n2. Solution Architecture: 3-step deployment.\n3. Financial Model: Year 1 Cost vs Year 1 Measurable Economic Benefit.\n4. Implementation Roadmap with Go-Live milestone date.",
             "1-page executive investment summary document."),

            ("Gatekeeper Navigation & Internal Champion Identifier",
             "Outbound Intelligence Agent",
             "Identify and empower the internal user champion to pitch {{YOUR_PRODUCT}} to leadership.",
             "1. Message to end-user: 'How much time do you personally spend on {{TEDIOUS_TASK}} each week?'\n2. Provide them with an internal pre-written email template they can forward to their VP.\n3. Arm them with 3 bulleted counter-arguments to common manager objections.\n4. Offer to build them a custom pilot at zero cost.",
             "Internal champion enablement kit."),

            ("Follow-up Email After Ghosted Discovery Call",
             "Deal Acceleration Specialist",
             "Re-engage a prospect who missed their scheduled demo call.",
             "1. Empathetic opening acknowledging executive scheduling chaos.\n2. Reschedule with 3 specific times + direct rebooking link.\n3. Include a 2-minute recorded video previewing what was prepared for their specific domain.\n4. No guilt-tripping language.",
             "Discovery no-show rebooking email sequence."),

            ("End-of-Quarter Urgency & Contract Incentive Letter",
             "VP of Sales",
             "Accelerate contract signing for in-flight evaluations before quarter-end.",
             "1. Offer genuine value concession (e.g. waived implementation fee, extra seats, locked multi-year pricing) tied to specific signing date.\n2. Justify why the concession exists (quarterly capacity planning).\n3. Keep contract terms simple with Redline assistance offer.\n4. Clean executive letter format.",
             "Quarter-end closing incentive letter."),

            ("Outbound Cold Calling Battlecard & Objection Handler",
             "Sales Enablement Director",
             "Generate rapid-fire responses for SDRs encountering top 6 live telephone objections.",
             "1. Objection: 'We already use {{COMPETITOR}}.'\n2. Objection: 'We have no budget right now.'\n3. Objection: 'Send me an email.'\n4. Objection: 'Not a priority this quarter.'\n5. Objection: 'I'm not the right person.'\n6. Provide pattern interrupt, bridge question, and meeting confirmation close for each.",
             "Tabular cold calling battlecard with verbatim phrases.")
        ]),

        # MODULE 3
        ("Module 3: Product-Led Growth & Onboarding Automation", 41, 60, [
            ("First 5-Minute Time-to-Value (TTV) User Onboarding Flow",
             "Product-Led Growth Specialist",
             "Map the exact sequence to bring a newly registered user of {{PRODUCT_NAME}} to their 'Aha!' moment in < 300 seconds.",
             "1. Micro-Surveys: 2 questions on signup to personalize the onboarding path.\n2. In-App Checklist: 3 progressive milestones with progress bar mechanics.\n3. Empty State Strategies: What to show before they connect data so the app feels populated.\n4. Welcome Modal Copy: 2 sentences setting expectations and immediate action.",
             "Step-by-step UX onboarding flow specification with exact UI copy."),

            ("Behavioral Trigger Email Architecture",
             "Lifecycle Marketing Engineer",
             "Design 5 event-triggered emails based on user telemetry within days 1-14.",
             "1. Trigger: User signed up but did not invite a teammate after 48h.\n2. Trigger: User uploaded data but did not trigger their first export.\n3. Trigger: User hit 80% of free tier threshold.\n4. Trigger: User was inactive for 7 consecutive days after initial activation.\n5. Write subject line, preview text, body, and button copy for each.",
             "Event schema table + 5 complete lifecycle emails."),

            ("Interactive In-Product Tooltip & Tour Copy",
             "UX Microcopy Strategist",
             "Write high-delight, zero-annoyance product tour tooltips for 4 critical dashboard features.",
             "1. Limit each tooltip to 25 words.\n2. Explain benefit, not just feature button mechanics.\n3. Include 'Got it' and 'Show me how' micro-actions.\n4. Ensure dismiss state persists permanently across sessions.",
             "Tooltip matrix with Step number, Anchor element, Header, Body, and Button labels."),

            ("Empty State UX Copy & Activation Acceleration",
             "Product Designer & Copywriter",
             "Transform empty screens (No projects, No data, No reports) into high-conversion activation hubs.",
             "1. Illustrative hook acknowledging empty state with playful, encouraging tone.\n2. 1-click demo data population button ('Load Sample Enterprise Workspace').\n3. Primary creation CTA button with prominent contrast.\n4. 2-minute video explainer thumbnail embed.",
             "Wireframe specification with copy for 3 primary empty-state views."),

            ("In-App Milestone Celebration & Social Sharing Prompt",
             "Growth Gamification Architect",
             "Design the celebration modal when a user accomplishes {{CORE_ACHIEVEMENT}} (e.g. 100th automated task).",
             "1. Confetti/Micro-animation design brief.\n2. Quantified celebration metric: 'You just saved 42 hours this month'.\n3. 1-Click pre-written LinkedIn/X share button bragging about their operational efficiency.\n4. Bonus unlocked (e.g. 500 bonus API credits) as a reward.",
             "Celebration modal UX copy and social share card metadata."),

            ("Feature Adoption Nudge for Dormant Power Features",
             "Product Marketing Manager (Adoption)",
             "Target active users who use basic features but ignore the highest-retention power feature {{POWER_FEATURE}}.",
             "1. In-app banner triggered after 10th login.\n2. Copy: 'You're doing {{TASK}} manually. Did you know you can automate it in 1 click?'\n3. 15-second embedded GIF showing the interaction.\n4. Direct activation button.",
             "In-app slide-over copy and notification logic."),

            ("Usage-Gated Paywall & Upgrade Modal Matrix",
             "Monetization & Pricing Strategist",
             "Design the paywall modal triggered when a free user exceeds {{USAGE_LIMIT}}.",
             "1. Positive reinforcement: 'You've reached the free tier limit because your team is crushing it.'\n2. Clear visual comparison: What unlocks on Pro / Enterprise tier.\n3. Social proof snippet from a paid user in their exact industry.\n4. Annual vs Monthly toggle with 20% discount badge.\n5. Frictionless checkout button.",
             "Paywall modal copy and layout specification."),

            ("Self-Serve to Sales-Assisted Lead Handoff Trigger",
             "Product-Led Sales (PLS) Engineer",
             "Identify Product Qualified Leads (PQLs) inside free workspaces and trigger automated outreach.",
             "1. Scoring Criteria: >3 users from same corporate domain + >50 actions in 72 hours.\n2. Automated Slack/CRM notification to Enterprise Account Executive.\n3. Contextual in-app message from dedicated solutions engineer offering SSO, security review, and team billing.",
             "PLS scoring algorithm rules + outreach message templates."),

            ("User Friction / Drop-off Point Diagnostics Generator",
             "UX Analytics Specialist",
             "Analyze user drop-off during {{COMPLEX_WORKFLOW_STEP}} and create remediation plan.",
             "1. Diagnostic questions to isolate whether drop-off is technical, cognitive load, or permission-based.\n2. Simplified 2-step alternative workflow.\n3. Contextual help link and inline error message improvements.\n4. Micro-recovery email to users who dropped off at this exact step.",
             "Friction audit checklist + optimized copy alternatives."),

            ("Interactive Product Demo Script & Tour Guide",
             "Interactive Walkthrough Producer",
             "Script a self-guided interactive product tour using tools like Navattic or Arcade for {{PRODUCT_NAME}}.",
             "1. 5 sequential interactive checkpoints.\n2. Callout cards explaining business context at each click.\n3. Simulated result calculation screen.\n4. Final CTA card inviting user to deploy on their own data.",
             "Step-by-step interactive script with user click triggers."),

            ("Automated NPS / CSAT Micro-Survey & Routing",
             "Customer Experience Architect",
             "Deploy a 1-question in-app CSAT survey and route feedback intelligently.",
             "1. Timing trigger: Triggered immediately after a successful core workflow completion.\n2. Rating 9-10 (Promoters): Auto-prompt to leave a G2 review or join referral program.\n3. Rating 7-8 (Passives): Inquire what 1 feature would make it a 10.\n4. Rating 1-6 (Detractors): Instant internal alert to founder/CSM to resolve issue within 2 hours.",
             "Survey microcopy + conditional routing workflow."),

            ("In-App Referral & Invite-a-Teammate Virality Loop",
             "Viral Growth Specialist",
             "Engineer a viral loop incentivizing users to invite colleagues into their workspace.",
             "1. Give-Get Incentive: 'Give your colleague $50 credit, get $50 credit'.\n2. Frictionless input: Multiple email input box with Google Contacts / Slack sync.\n3. Pre-written invitation email from user to their colleague explaining why they invited them.\n4. Team collaboration benefit highlight.",
             "Referral modal copy + viral email invite template."),

            ("Workspace Multi-Seat Expansion Prompt",
             "Expansion Revenue Specialist",
             "Prompt team admins when their workspace approaches seat saturation.",
             "1. Trigger: Admin has assigned 4 of 5 available seats.\n2. In-app banner: 'Your team is growing fast. Add 5 seats with 1-click pooled billing'.\n3. Feature highlight: Centralized permissions, shared templates, audit logs.\n4. Add seats button with immediate prorated calculation.",
             "Admin notification banner and email copy."),

            ("Freemium Expiration / Trial Ending Urgency Cadence",
             "Trial Conversion Strategist",
             "Execute a 3-day urgency sequence before a 14-day free trial expires.",
             "1. Day 11 (3 Days Left): Summary of accomplishments during trial (Data processed, hours saved).\n2. Day 13 (24h Left): Urgency warning regarding data preservation and automation continuity.\n3. Day 14 (Trial Expired): Soft grace period extension offer with payment link.\n4. Day 16 (Post-Expiry): Win-back discount offer.",
             "4 high-converting trial expiration emails."),

            ("Self-Serve Customer Welcome Video Script",
             "Founder & Creative Director",
             "Write a 60-second authentic founder welcome video embedded on the first-login screen.",
             "1. Warm, human welcome thanking them for trusting {{PRODUCT_NAME}}.\n2. The 'One Thing': Tell them the single most important action to take right now.\n3. Personal commitment to their success: 'Hit reply to any email and it goes straight to my inbox'.\n4. Zero corporate jargon.",
             "Founder video script with tone guidance and visual staging notes."),

            ("Customer Community Invitation & Orientation Flow",
             "Community Director",
             "Onboard new paid users into an exclusive customer Slack/Discord community.",
             "1. Invitation email framing the community as a private network of elite practitioners.\n2. #introductions channel template prompt for new members.\n3. Weekly recurring rituals (AMA, Template Share Friday, Office Hours).\n4. Community guidelines maintaining high signal-to-noise ratio.",
             "Community welcome sequence + channels architecture."),

            ("In-App Release Note & Feature Micro-Feedback Modal",
             "Product Feedback Specialist",
             "Collect immediate user sentiment on newly shipped features inside the product UI.",
             "1. Compact modal anchored to the new button or navigation item.\n2. 2-sentence explanation of what changed.\n3. Quick thumbs up / thumbs down reaction buttons.\n4. Optional 1-sentence comment field for rapid iteration.",
             "Micro-modal UI copy and event payload spec."),

            ("Personalized Dashboard Metric Digest Email",
             "Customer Analytics Strategist",
             "Generate weekly automated performance summary emails sent to users every Monday morning.",
             "1. Subject: 'Your {{PRODUCT}} Weekly Digest: {{HOURS_SAVED}} hrs saved'.\n2. 3 prominent metric badges (Tasks automated, Pipeline generated, Errors prevented).\n3. Trend comparison: '+24% vs last week'.\n4. Recommended action: '1 task needs your attention today'.",
             "HTML email wireframe and copy template with dynamic data tags."),

            ("Customer Champion Identification & Badge System",
             "Customer Advocacy Strategist",
             "Identify power users who log in daily and award them 'Verified Power Architect' status.",
             "1. In-app badge notification modal.\n2. Exclusive perks: Direct roadmap voting rights, private beta access, free swag pack.\n3. Request for quote / headshot for customer wall of love.\n4. Social shareable badge graphic spec.",
             "Champion recognition modal copy and enablement workflow."),

            ("Proactive In-App Support Deflection & Self-Help Article",
             "Technical Support Architect",
             "Create an intelligent self-service knowledge base answer resolving {{TOP_SUPPORT_QUESTION}}.",
             "1. Direct solution in first paragraph with screenshot placeholder.\n2. Common troubleshooting steps if error persists.\n3. Interactive copyable code block or config snippet.\n4. Escalation button to live human chat if unresolved.",
             "Structured Help Center article in Markdown.")
        ]),

        # MODULE 4
        ("Module 4: Social Media Authority & Multi-Channel Distribution", 61, 80, [
            ("Viral Technical LinkedIn Post Engine",
             "High-Impact B2B Content Creator",
             "Write an authoritative LinkedIn breakdown explaining how to build {{TECHNICAL_ARCHITECTURE}} using AI agents.",
             "1. Hook (Lines 1-2): Provocative observation about why 95% of engineering teams build this incorrectly.\n2. Context: The hidden cost of conventional setups (latency, token costs, maintenance).\n3. The 4-Step Solution Architecture: Bulleted, clean, technical depth without buzzwords.\n4. The Golden Rule: One memorable philosophical takeaway.\n5. Call to Conversation: An engaging, open-ended technical question.",
             "Publication-ready LinkedIn post with line breaks and unicode formatting."),

            ("Multi-Platform Social Repurposing Engine",
             "Content Distribution Director",
             "Take a single 2,000-word blog post or product release and splinter it into 5 distinct social assets.",
             "1. Asset 1: 10-tweet X (Twitter) Mega-Thread with hook and summary.\n2. Asset 2: Authoritative LinkedIn carousel script (8 slides).\n3. Asset 3: Short-form video script (TikTok / YouTube Shorts / Reels under 60s).\n4. Asset 4: Email newsletter editorial takeaway.\n5. Asset 5: Punchy contrarian quote graphic caption.",
             "Full multi-channel package in organized Markdown sections."),

            ("Contrarian Industry Take & Poll Strategy",
             "B2B Growth Strategist",
             "Craft a high-engagement LinkedIn Poll and accompanying editorial debating {{CONTROVERSIAL_TOPIC}}.",
             "1. Hook: State an uncomfortable industry truth.\n2. Poll Question: Clear, binary or 4-option question forcing an opinion.\n3. 4 Poll Options: Thoughtfully worded representing different operational philosophies.\n4. Accompanying post context: State your own stance with empirical justification.\n5. Pinned comment to seed debate.",
             "Complete poll specification and commentary copy."),

            ("Behind the Build / Transparent Founder Devlog",
             "Transparent Startup Founder",
             "Write a vulnerable, authentic devlog post sharing a technical breakthrough or setback while building {{FEATURE}}.",
             "1. The Hypothesis: What we thought would take 2 days.\n2. The Reality: Why it failed in production on Saturday night.\n3. The Pivot: The architectural redesign that solved it.\n4. The Metric: Latency dropped from 2.4s to 180ms.\n5. Raw screenshot / terminal code block inclusion.",
             "Engaging founder story post formatted for X and LinkedIn."),

            ("Visual Framework & Architecture Diagram Explainer",
             "Technical Architect & Educator",
             "Write the accompanying text for a Mermaid architecture diagram showing {{SYSTEM_WORKFLOW}}.",
             "1. Headline: 'How modern {{CATEGORY}} stacks actually work in 2026'.\n2. The 3 layers: Ingestion, Cognitive Processing (LLM), and Action Execution (APIs).\n3. The single biggest bottleneck teams overlook (State management).\n4. Call to save / bookmark for reference.",
             "Mermaid diagram code block + viral social breakdown caption."),

            ("Step-by-Step Tactical Carousel Slide Copy",
             "B2B Visual Storyteller",
             "Write an 8-slide educational carousel teaching 'The 5-Step Agentic Workflow for B2B Founders'.",
             "1. Slide 1 (Cover): Bold title, compelling subtitle, author handle.\n2. Slides 2-6: 1 tactical step per slide (Headline, 2 bullet points, 1 pro-tip).\n3. Slide 7: Summary scorecard / checklist.\n4. Slide 8: CTA to download the full master prompt library.",
             "Slide-by-slide copy with visual design cues for graphic designer."),

            ("Weekly Newsletter Deep Dive & Editorial Synthesis",
             "Chief Newsletter Editor",
             "Write a 1,200-word issue of 'The Autonomous Revenue Leader' on {{WEEKLY_THEME}}.",
             "1. The Big Idea: Why this week's theme matters right now.\n2. The Deep Dive: 3 concrete frameworks with diagrams and real company examples.\n3. Tool of the Week: Unbiased teardown of a high-leverage agentic tool.\n4. Prompt of the Week: Ready-to-copy prompt with sample output.\n5. Parting Thought: 1 philosophical quote on leverage.",
             "Complete Substack / Beehiiv newsletter issue in Markdown."),

            ("High-Engagement X (Twitter) Mega-Thread Architect",
             "X Growth Engineer",
             "Draft a 12-tweet viral thread breaking down '10 AI Automations That Save 20+ Hours Every Week'.",
             "1. Tweet 1 (Hook): Compelling statement + social proof + 'Here is the exact blueprint:'\n2. Tweets 2-11: 1 specific automation per tweet (Tool, Workflow, Result, Copyable prompt).\n3. Tweet 12 (Conclusion): Summary table + RT request + link to full landing page.",
             "Numbered thread tweets with character counts under 270 per tweet."),

            ("How We Scaled Retrospective Teardown",
             "VP of Growth",
             "Write a case-study style post detailing 'How we went from $0 to $100k ARR in 90 days with 0 sales reps'.",
             "1. The Initial Bottleneck: Why hiring SDRs wasn't viable.\n2. The Autonomous Engine: The 3 automated systems built instead.\n3. The Exact Numbers: Conversion rates, churn, gross margins.\n4. The 3 Mistakes: What we would do differently today.\n5. Link in comments to the playbook.",
             "Detailed, metrics-heavy social essay."),

            ("Technical Tool Comparison & Vendor Audit Post",
             "Independent Technology Auditor",
             "Compare 3 leading solutions in {{CATEGORY}} objectively for engineering leaders.",
             "1. Criteria: Latency, Developer DX, Pricing transparency, Enterprise security.\n2. Vendor A: Best for enterprise with large legacy compliance needs.\n3. Vendor B: Best for early-stage hackers.\n4. Vendor C (Your Product): Best for autonomous agentic scale.\n5. Neutral closing inviting engineers to share their benchmarks.",
             "Clean comparison post with formatting for high readability."),

            ("The 'Mistake / What Went Wrong' Post-Mortem Hook",
             "Authentic Growth Practitioner",
             "Share a $10,000 marketing or technical mistake and the exact SOP built to prevent it forever.",
             "1. Hook: 'We burned $12,400 on {{EXPERIMENT}} last month. Here is the post-mortem:'\n2. What the data predicted vs what happened in production.\n3. The root cause analysis (Cognitive bias / false assumptions).\n4. The new automated guardrail implemented.\n5. Lesson for other founders.",
             "High-engagement vulnerability post designed to build authority and trust."),

            ("High-Intent Comment-to-DM Lead Magnet Offer",
             "Lead Generation Inbound Architect",
             "Draft a 'Comment {{KEYWORD}} and I will DM you the template' viral post.",
             "1. Tease a high-value proprietary asset (e.g. 'Our internal 40-page prompt database').\n2. Show a screenshot or preview GIF of the asset in action.\n3. Give away 3 tips directly in the post so it delivers standalone value.\n4. Call to Action: 'Comment AGENT below and my automated bot will DM you the direct PDF link'.",
             "Viral giveaway post copy + automated DM message template."),

            ("Customer Win & ROI Showcase Micro-Case Study",
             "Customer Advocacy Strategist",
             "Highlight a customer's success in a punchy, narrative social post without feeling like a sales pitch.",
             "1. Hook: 'Client X just hit {{MAJOR_MILESTONE}} in 28 days. Here is their exact stack:'\n2. Before state: 14 hours/week lost to manual work.\n3. The 1 tweak: Deploying autonomous prompt architecture.\n4. After state: 3.4x output, team morale up.\n5. Congratulate the customer team publicly.",
             "Celebratory case study post with tag placeholders."),

            ("Industry Myth-Buster & First-Principles Debunking",
             "Contrarian Thought Leader",
             "Debunk 3 widespread myths in {{INDUSTRY_SECTOR}} with empirical math.",
             "1. Myth 1: 'You need 10 SDRs to scale outbound'. Debunk with agentic math.\n2. Myth 2: 'AI content kills SEO rankings'. Debunk with technical intent topology.\n3. Myth 3: 'Enterprise clients won't buy from small teams'. Debunk with security automation.\n4. Conclusion: The modern small team has the leverage of a 500-person corporation.",
             "Myth-busting post with bold headers and clear formatting."),

            ("Live Q&A / AMA Announcement & Framing Strategy",
             "Event Host & Community Builder",
             "Promote an upcoming live technical AMA: 'Building Autonomous Revenue Engines with Python & AI'.",
             "1. Announce date, time, and streaming platform.\n2. List 3 specific technical architectures that will be live-coded.\n3. Promise: 'No sales pitch. Pure terminal commands, code walkthroughs, and Q&A'.\n4. Ask followers to drop their toughest questions in the comments.",
             "Event announcement post with RSVP call to action."),

            ("Trending Tech News & Paradigm Shift Commentary",
             "Tech Trends Analyst",
             "React to a major industry announcement (e.g. new frontier model release, API update) within 2 hours.",
             "1. The News: 1-sentence breakdown of what actually changed.\n2. The Noise vs The Signal: Why 90% of reactions miss the true impact.\n3. The 3 Second-Order Effects: How this changes B2B economics over the next 12 months.\n4. Tactical takeaway: What founders should do by Friday.",
             "Rapid-response thought leadership commentary."),

            ("Multi-Speaker Podcast / Interview Soundbite Clipper",
             "Multimedia Content Producer",
             "Extract the most controversial 60-second snippet from an interview with {{GUEST_NAME}} and write the social post.",
             "1. Hook: Direct provocative quote in quotation marks.\n2. Background: Why {{GUEST_NAME}}'s perspective is uniquely qualified.\n3. The Core Argument summarized in 3 sentences.\n4. Link to full episode on Spotify / Apple Podcasts.",
             "Podcast clip caption with timestamp reference and quote cards."),

            ("Employee Advocacy & Team Amplification Templates",
             "Internal Communications Director",
             "Create 3 distinct post variations for internal team members to share company announcements authentically.",
             "1. Engineering Perspective: Focus on the technical hurdles overcome.\n2. Customer Success Perspective: Focus on the customer problems solved.\n3. Sales Perspective: Focus on market demand and speed.\n4. Freedom to customize instructions.",
             "3 employee post variations with guidance notes."),

            ("Weekly High-Value Curated Resource Roundup",
             "Curator & Community Lead",
             "Curate the top 5 papers, tools, and prompts of the week in {{NICHE}}.",
             "1. Title: 'The Autonomous Growth Stack: Issue #{{NUMBER}}'.\n2. 5 curated items: 1-sentence summary + why it matters + direct link.\n3. 1 bonus community question.\n4. CTA to subscribe to the newsletter for future digests.",
             "Roundup post formatted for clean skim-reading."),

            ("Social Call-to-Conversation & Debate Catalysts",
             "Community Engagement Engineer",
             "Craft a single provocative question designed to generate 100+ executive comments.",
             "1. Question framing: 'B2B Founders: Would you rather have 10,000 newsletter subscribers or 50 qualified enterprise demo requests? Why?'\n2. 2-sentence rationale showing both sides of the tradeoff.\n3. First comment seed from author.",
             "Short-form conversation catalyst post.")
        ]),

        # MODULE 5
        ("Module 5: Retention, Churn Prevention & Account Expansion", 81, 100, [
            ("Predictive Churn Intervention System",
             "Head of Customer Success",
             "Triage and intervene when an enterprise account exhibits a 45% telemetry drop over 14 days.",
             "1. Automated internal alert with account historical spend and champion info.\n2. Direct, empathetic email from founder/VP to executive sponsor.\n3. Concrete offer: Free engineering audit / custom configuration call.\n4. Follow-up task assigned to CSM with 24h deadline.",
             "Intervention email template + CSM triage checklist."),

            ("Quarterly Business Review (QBR) Executive Presentation",
             "Strategic Customer Success Director",
             "Build a 10-slide high-impact QBR deck proving quantifiable value for {{CLIENT_NAME}}.",
             "1. Slide 1: Partnership Mission & Executive Goals Alignment.\n2. Slides 2-4: Quantified Business Value (Hours saved, Tasks executed, ROI multiplier).\n3. Slides 5-7: Team Adoption Metrics & Top Power Users.\n4. Slides 8-9: Strategic Roadmap for Upcoming Quarter.\n5. Slide 10: Contract Expansion / Multi-Year Renewal Proposal.",
             "Slide-by-slide executive talking points with data chart mockups."),

            ("Cross-Department SaaS Upsell & Expansion Proposal",
             "Account Growth & Expansion Director",
             "Expand an existing paid customer from Marketing department into Sales & Engineering.",
             "1. Acknowledge existing success in Marketing: 'Your marketing team automated 1,400 tasks this quarter'.\n2. Identify cross-department synergy: How Sales can utilize the exact same data without duplicating subscriptions.\n3. Unified enterprise workspace pricing proposal with volume seat discount.\n4. 30-day proof-of-concept for the new department at no extra cost.",
             "Expansion proposal letter + executive ROI comparison."),

            ("Executive Sponsor Departure & New Champion Transition",
             "Client Retention Specialist",
             "Navigate the departure of your primary buyer champion at {{ENTERPRISE_ACCOUNT}}.",
             "1. Reach out to departing champion: Congratulate, secure personal contact info, and ask for introduction to interim successor.\n2. Outreach to new incoming executive: Present 1-page summary of accomplishments achieved to date.\n3. Offer a 20-minute executive briefing to align with their new strategic vision.\n4. Avoid sales pressure; establish immediate continuity and reliability.",
             "2 transition email templates (Departing Champion & Incoming Executive)."),

            ("Price Increase Notice & Grandfathering Retention Letter",
             "Chief Commercial Officer",
             "Announce a 20% platform price increase while locking in current customers for multi-year renewals.",
             "1. Explain the investments made into platform capabilities, infrastructure speed, and new AI models.\n2. State the new standard pricing taking effect next month for new customers.\n3. Offer existing customers the exclusive right to lock in their existing lower rate for 24 months by renewing early.\n4. Transparent, confident, and customer-centric tone.",
             "Customer price update notice + early renewal incentive agreement."),

            ("Customer Health Scorecard & Account Review Matrix",
             "VP of Customer Experience",
             "Construct a predictive 5-pillar Customer Health Score algorithm for {{PRODUCT_NAME}}.",
             "1. Pillar 1: Product Usage Frequency (Daily/Weekly Active Users).\n2. Pillar 2: Core Feature Depth (Number of advanced prompts/workflows triggered).\n3. Pillar 3: Support Ticket Velocity & Sentiment.\n4. Pillar 4: Invoice Status & Billing Health.\n5. Pillar 5: Executive Relationship & QBR Engagement.\n6. Assign weights (Total 100%) and define Green/Yellow/Red action triggers.",
             "Health score formula table + automated intervention playbook per tier."),

            ("Root-Cause Post-Mortem for Lost Enterprise Accounts",
             "Customer Operations Analyst",
             "Conduct an objective exit interview and internal post-mortem for churned account {{ACCOUNT_NAME}}.",
             "1. Exit interview invitation email asking for 10 minutes of unfiltered feedback.\n2. 4 diagnostic exit questions isolating product gaps, pricing friction, or internal re-orgs.\n3. Internal post-mortem document summarizing what product/sales could have done differently.\n4. Tagging root cause in CRM (Feature gap, Budget, Champion left, Poor onboarding).",
             "Exit survey email + internal root-cause post-mortem template."),

            ("Customer Advisory Board (CAB) Invitation & Agenda",
             "CEO & Head of Product",
             "Invite the top 15 most strategic customers to an exclusive Customer Advisory Board.",
             "1. Invitation letter framing membership as a prestigious, invitation-only council.\n2. CAB Charter: 2 virtual meetings per year + 1 annual executive dinner.\n3. Perks: Direct influence on product roadmap, early access to unreleased models, peer networking.\n4. Agenda outline for the inaugural 90-minute session.",
             "CAB invitation letter + 90-minute meeting agenda."),

            ("Co-Marketing & Case Study Collaboration Pitch",
             "Customer Advocacy Lead",
             "Invite a happy customer who achieved stellar metrics to co-produce a case study and PR release.",
             "1. Compliment their team's execution and quantified results.\n2. Explain the exposure: Featured on our homepage, distributed to 50k+ newsletter subscribers, submitted to industry press.\n3. Zero-effort guarantee: 'Our writer handles 100% of the draft; you just review for 10 minutes'.\n4. Bonus: Complimentary upgrade / tier extension.",
             "Co-marketing pitch email with approval workflow."),

            ("Annual Contract Renewal Early-Bird Discount Offer",
             "Revenue Retention Specialist",
             "Convert monthly recurring billing accounts into prepaid annual agreements.",
             "1. Send 60 days before contract anniversary.\n2. Financial incentive: 2 months completely free + free premium onboarding.\n3. Accounting benefit: Single annual invoice, predictable budgeting, locked-in price.\n4. 1-click upgrade link via customer portal.",
             "Annual contract conversion email cadence."),

            ("High-Value Feature Request Priority Notification",
             "Product Communications Specialist",
             "Notify a customer who previously requested a feature that it is now deployed live to production.",
             "1. Personalized reference: 'You asked for {{FEATURE_NAME}} on our call 3 months ago. Today it's live'.\n2. 30-second screen recording GIF showing how to use it.\n3. Thank them for helping shape the platform.\n4. Ask for their immediate feedback after trying it out.",
             "High-delight feature release notification email."),

            ("SLA Breach Apology & Customer Recovery Plan",
             "VP of Engineering & VP of Customer Success",
             "Address a major platform downtime incident or API SLA breach transparently.",
             "1. Direct executive apology without defensive excuses.\n2. Root Cause Analysis (RCA): Plain-English technical explanation of what failed.\n3. Permanent Remediation: 3 infrastructure safeguards deployed to ensure it never happens again.\n4. Commercial Remedy: Automatic service credit applied to their next invoice without asking.",
             "Executive SLA incident notification letter."),

            ("Executive Sponsor Check-in from Founder / CEO",
             "Founder & CEO",
             "Send a periodic, high-touch 4-sentence email from the founder to enterprise customer executives.",
             "1. Personal note: No sales pitch, no survey links.\n2. Check-in question: 'Are we delivering on the business outcomes your team signed up for?'\n3. Invitation for raw feedback: 'If anything is sluggish or falling short, let me know directly'.\n4. Reaffirmation of long-term partnership commitment.",
             "Authentic CEO check-in email template."),

            ("Under-Utilized Seat Cleanup & Team Re-Engagement",
             "Customer Success Manager",
             "Help an enterprise admin reallocate inactive seats before they ask for a contract reduction.",
             "1. Proactive alert: 'Notice 4 teammates haven't logged in over 30 days'.\n2. Offer 1: Free 15-minute re-training workshop for those teammates.\n3. Offer 2: Reassign seats to their new department initiative.\n4. Shows customer-first integrity rather than hoarding unused seats.",
             "Proactive seat audit and training offer email."),

            ("Product Sunset / Deprecation Migration Guide",
             "Director of Product Operations",
             "Communicate the sunsetting of legacy feature {{FEATURE}} and guide users to the modern alternative.",
             "1. Timeline: 90-day deprecation notice with milestone dates.\n2. Why it matters: The superior performance and security of the new agentic architecture.\n3. Migration guide: 3 steps to transition data with automated migration script.\n4. Dedicated office hours link for engineering teams needing help.",
             "Feature deprecation notice and migration checklist."),

            ("Enterprise Security & Compliance Assurance Dossier",
             "Chief Information Security Officer (CISO)",
             "Equip enterprise buyers with a complete compliance packet resolving security review delays.",
             "1. SOC 2 Type II, GDPR, and HIPAA compliance summaries.\n2. Data encryption standards (AES-256 at rest, TLS 1.3 in transit).\n3. AI Model Data Privacy Guarantee: 'Zero customer data is ever retained or used to train public models'.\n4. Disaster recovery and penetration test executive summary.",
             "1-page CISO security assurance brief."),

            ("Customer Training & Certification Curriculum Architect",
             "Head of Customer Enablement",
             "Design a 4-module 'Certified Autonomous Operator' program for client employees.",
             "1. Module 1: Prompt Architecture & Schema Discipline.\n2. Module 2: Connecting External APIs & Data Pipelines.\n3. Module 3: Error Handling, Guardrails & Human-in-the-Loop Review.\n4. Module 4: Measuring & Reporting ROI to Leadership.\n5. Practical exam project + LinkedIn certification credential.",
             "Customer certification curriculum syllabus."),

            ("Account Escalation Resolution & Trust Restoration Plan",
             "Chief Customer Officer",
             "De-escalate an account where an executive threatened cancellation due to poor experience.",
             "1. 1-hour internal discovery to gather all facts before calling client.\n2. Personal call outline: Listen first, acknowledge frustration without defensiveness.\n3. Action plan: Dedicated senior engineer assigned to their ticket queue for 30 days.\n4. Weekly status update email cadence until trust is completely restored.",
             "De-escalation protocol and executive follow-up email."),

            ("Expansion Opportunity Trigger (API Limit / Storage Warning)",
             "Growth Engineering Lead",
             "Send a high-conversion automated warning when a team hits 90% of their monthly throughput quota.",
             "1. Notification: 'Your automated pipelines processed 90,000 of your 100,000 monthly operations'.\n2. Reassurance: Pipelines will not halt abruptly.\n3. 1-click upgrade button to the Unlimited Enterprise tier with volume pricing.\n4. Contact rep button for custom invoicing.",
             "Quota alert banner copy and email alert template."),

            ("Customer Advocacy & Reference Program Invitation",
             "Head of Advocacy Marketing",
             "Enroll happy customers into an executive peer-reference network with tangible rewards.",
             "1. Selective invitation: 'Inviting you to our exclusive Founders Circle'.\n2. Commitment: Agree to take max one 15-minute call per quarter with a prospective enterprise buyer.\n3. Rewards: $500 software credit per call + VIP dinner invitation at annual summit.\n4. 1-click acceptance form.",
             "Advocacy program invitation email and agreement terms.")
        ])
    ]

    sops_data = [
        ("The Autonomous Weekly B2B Content Engine", "45 mins/week",
         "1 High-Intent Pillar + 5 Social Posts + 1 Newsletter on autopilot",
         "1. Input: Select 1 high-intent topic from Module 1 (e.g. Prompt #1).\n2. Generation: Run Prompt #2 to create the 1,800-word authoritative pillar essay.\n3. Multi-Channel Splintering: Feed the pillar into Prompt #62 (Repurposing Engine) to generate 1 X thread, 5 LinkedIn posts, and 1 newsletter issue.\n4. Automated Distribution: Populate the generated posts into `promotional_tips.csv` and run `auto_poster.py`.\n5. Conversion Tracking: Measure inbound traffic and Gumroad sales attribution weekly."),

        ("Real-Time Competitor Intelligence & Counter-Positioning", "48-hr turnaround",
         "Zero lost deals to competitor positioning blindsides",
         "1. Monitoring: Set automated scrapers or alerts for competitor pricing, feature announcements, and G2 reviews.\n2. Analysis: Run Prompt #4 (Battlecard Generator) to extract weaknesses and strategic divergence.\n3. Sales Enablement: Distribute the 1-page battlecard to the sales team within 24 hours.\n4. Public BOFU Asset: Run Prompt #6 to publish an objective 'Top Alternatives' page capturing search intent.\n5. Feedback Loop: Update positioning monthly based on win/loss interview telemetry."),

        ("Cold Outbound Dynamic ICP Scoring & Personalization", "100% Automated",
         "18.4% Average Reply Rate across target accounts",
         "1. Signal Ingestion: Ingest verified trigger events (hiring, funding, tech migrations) via data enrichment APIs.\n2. Prompt Formatting: Run Prompt #21 with dynamic company and prospect variables.\n3. Guardrail Review: Automatic check for word count (<85 words) and negative constraints (zero buzzwords).\n4. Omnichannel Cadence: Run Prompt #23 to sequence email, LinkedIn touchpoints, and soft-offer follow-ups.\n5. Conversion Handoff: Route positive replies directly to calendar scheduler."),

        ("Churn Risk Flagging & Automated Interventions", "Real-time Telemetry",
         "35% Voluntary Churn Reduction",
         "1. Event Ingestion: User telemetry continuously monitored for 40%+ drop in 14-day login frequency.\n2. Triage & Flagging: Run Prompt #86 (Health Scorecard) to categorize account risk tier.\n3. Automated Interventions: Trigger Prompt #81 (Predictive Churn Intervention) from founder/VP account.\n4. CSM Routing: Generate automated high-priority ticket with account context and suggested remediation.\n5. Root-Cause Logging: If account cancels, execute Prompt #87 post-mortem to patch product friction.")
    ]

    # Assemble Markdown
    md_lines = []
    md_lines.append("# The Autonomous AI Growth Engine")
    md_lines.append("## 100 Advanced AI Agent Prompts, Production Architectures & SOPs for B2B Tech Founders & Revenue Leaders\n")
    md_lines.append("**Edition:** 2026 Enterprise Edition  ")
    md_lines.append("**Author:** AI Growth Engineering Labs  ")
    md_lines.append("**License:** Commercial & Personal Implementation License  ")
    md_lines.append("**Product Version:** v2.4  \n")
    md_lines.append("---\n")
    md_lines.append("## Executive Summary & Quick-Start Guide\n")
    md_lines.append("Traditional go-to-market (GTM) motions in B2B tech have hit a wall: customer acquisition costs (CAC) are up over 60%, outbound reply rates on generic templates have plummeted below 1.2%, and content saturation makes generic AI copy worthless.\n")
    md_lines.append("The winning playbook is **autonomous agentic workflows**—specialized AI agents with structured multi-turn instructions, clear schema enforcement, few-shot reasoning, and direct integrations into your CRM, data enrichment pipelines, and distribution engines.\n")
    md_lines.append("This guide provides **100 battle-tested, production-ready AI prompts**, **4 end-to-end Standard Operating Procedures (SOPs)**, and **architectural blueprints** designed to generate qualified pipeline, maximize retention, and scale organic reach on autopilot.\n")
    md_lines.append("### How to Deploy These Assets")
    md_lines.append("1. **Model Selection:** Recommended for Anthropic Claude 3.5/3.7 Sonnet, OpenAI GPT-4o / o1 / o3, or Google Gemini 1.5/2.0 Pro.")
    md_lines.append("2. **Variable Substitution:** Replace bracketed parameters like `{{COMPANY_NAME}}`, `{{ICP_TITLE}}`, `{{TARGET_INDUSTRY}}` before running.")
    md_lines.append("3. **Structured Outputs:** When feeding results into automated pipelines (n8n, Make, Python scripts), prompt instructions enforce JSON output.\n")
    md_lines.append("---\n")
    md_lines.append("# Table of Contents\n")
    for mod_title, start_p, end_p, _ in modules_data:
        md_lines.append(f"- **{mod_title} (Prompts {start_p}–{end_p})**")
    md_lines.append("- **Standard Operating Procedures (SOP 1–4)**")
    md_lines.append("- **Production Automation Architecture & Tooling Stack**\n")
    md_lines.append("---\n")

    for mod_title, start_p, end_p, prompts in modules_data:
        md_lines.append(f"# {mod_title} (Prompts {start_p}–{end_p})\n")
        for p_idx, (p_title, p_role, p_task, p_instr, p_output) in enumerate(prompts, start=start_p):
            md_lines.append(f"### Prompt {p_idx}: {p_title}\n")
            md_lines.append("```text")
            md_lines.append(f"Role: {p_role}")
            md_lines.append(f"Objective: {p_task}")
            md_lines.append("\nInstructions:")
            md_lines.append(p_instr)
            md_lines.append(f"\nExpected Output Format:\n{p_output}")
            md_lines.append("```\n")

    md_lines.append("# Standard Operating Procedures (SOP 1–4)\n")
    for sop_num, (sop_title, sop_time, sop_impact, sop_steps) in enumerate(sops_data, start=1):
        md_lines.append(f"### SOP {sop_num}: {sop_title}")
        md_lines.append(f"**Execution Cadence:** {sop_time}  ")
        md_lines.append(f"**Quantified Business Impact:** {sop_impact}\n")
        md_lines.append("#### Step-by-Step Procedure:")
        md_lines.append(sop_steps)
        md_lines.append("\n---\n")

    md_lines.append("# Production Automation Architecture & Tooling Stack\n")
    md_lines.append("To scale beyond manual prompt copying, connect your prompts to automated infrastructure using the following stack:\n")
    md_lines.append("1. **Data Ingestion:** Clearbit, Apollo, or Crustdata for real-time B2B buyer intent triggers.")
    md_lines.append("2. **Workflow Orchestration:** Python scripts (`auto_poster.py`), n8n, or Make.com.")
    md_lines.append("3. **Unified Distribution:** Zernio Marketing API (`zernio-sdk`) for automated multi-channel posting across LinkedIn, X, and Facebook.")
    md_lines.append("4. **Conversion Engine:** Next.js Landing Page with embedded Gumroad / Lemon Squeezy checkout.\n")
    md_lines.append("*(C) 2026 AI Growth Engineering Labs. All Rights Reserved. Commercial Implementation License Granted to Purchaser.*")

    return "\n".join(md_lines)

def build_styled_html(markdown_text):
    import markdown
    body_html = markdown.markdown(markdown_text, extensions=['fenced_code', 'tables'])

    css = """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    @page {
        size: A4;
        margin: 20mm 15mm 20mm 15mm;
        @bottom-right {
            content: counter(page);
            font-family: 'Inter', sans-serif;
            font-size: 9pt;
            color: #64748b;
        }
    }

    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: #0f172a;
        background: #ffffff;
        line-height: 1.6;
        font-size: 10pt;
        margin: 0;
        padding: 0;
    }

    .cover-page {
        page-break-after: always;
        height: 90vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-left: 6px solid #4f46e5;
        padding-left: 32px;
        margin-top: 40px;
    }

    .cover-badge {
        display: inline-block;
        background: #ede9fe;
        color: #4f46e5;
        font-weight: 700;
        font-size: 11pt;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 6px 14px;
        border-radius: 6px;
        margin-bottom: 24px;
        width: fit-content;
    }

    .cover-title {
        font-size: 32pt;
        font-weight: 800;
        color: #0f172a;
        line-height: 1.15;
        margin: 0 0 16px 0;
    }

    .cover-subtitle {
        font-size: 15pt;
        color: #475569;
        font-weight: 400;
        line-height: 1.4;
        margin-bottom: 40px;
        max-width: 600px;
    }

    .cover-meta {
        font-size: 10pt;
        color: #64748b;
        line-height: 1.8;
        border-top: 1px solid #e2e8f0;
        padding-top: 24px;
        max-width: 500px;
    }

    h1 {
        font-size: 18pt;
        font-weight: 700;
        color: #1e1b4b;
        border-bottom: 2px solid #e0e7ff;
        padding-bottom: 8px;
        margin-top: 36px;
        margin-bottom: 16px;
        page-break-after: avoid;
    }

    h2 {
        font-size: 14pt;
        font-weight: 600;
        color: #312e81;
        margin-top: 24px;
        margin-bottom: 12px;
        page-break-after: avoid;
    }

    h3 {
        font-size: 11.5pt;
        font-weight: 700;
        color: #4338ca;
        margin-top: 20px;
        margin-bottom: 8px;
        page-break-after: avoid;
    }

    h4 {
        font-size: 10pt;
        font-weight: 600;
        color: #1e293b;
        margin-top: 12px;
        margin-bottom: 6px;
    }

    p {
        margin: 0 0 12px 0;
        color: #334155;
    }

    ul, ol {
        margin: 0 0 14px 0;
        padding-left: 20px;
        color: #334155;
    }

    li {
        margin-bottom: 4px;
    }

    pre {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-left: 4px solid #4f46e5;
        border-radius: 6px;
        padding: 12px 14px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 8.5pt;
        line-height: 1.5;
        color: #1e293b;
        overflow-x: auto;
        white-space: pre-wrap;
        word-wrap: break-word;
        page-break-inside: avoid;
        margin-bottom: 18px;
    }

    code {
        font-family: 'JetBrains Mono', monospace;
        font-size: 9pt;
        background: #f1f5f9;
        color: #475569;
        padding: 2px 5px;
        border-radius: 4px;
    }

    pre code {
        background: none;
        padding: 0;
        color: inherit;
    }

    hr {
        border: none;
        border-top: 1px solid #e2e8f0;
        margin: 28px 0;
    }

    blockquote {
        border-left: 4px solid #6366f1;
        background: #f5f3ff;
        padding: 10px 16px;
        margin: 16px 0;
        border-radius: 0 6px 6px 0;
        font-style: italic;
        color: #4338ca;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin: 16px 0;
        font-size: 9pt;
        page-break-inside: avoid;
    }

    th, td {
        border: 1px solid #cbd5e1;
        padding: 8px 12px;
        text-align: left;
    }

    th {
        background: #f1f5f9;
        color: #1e293b;
        font-weight: 600;
    }
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Autonomous AI Growth Engine (2026 Enterprise Edition)</title>
    <style>{css}</style>
</head>
<body>

<div class="cover-page">
    <div class="cover-badge">Enterprise Edition 2026</div>
    <div class="cover-title">The Autonomous<br/>AI Growth Engine</div>
    <div class="cover-subtitle">100 Production-Grade AI Prompts, Multi-Agent Operating Architectures & SOPs for B2B Tech Founders & Revenue Leaders</div>
    <div class="cover-meta">
        <strong>Publisher:</strong> AI Growth Engineering Labs<br/>
        <strong>Release Version:</strong> v2.4 (Production Master)<br/>
        <strong>License:</strong> Commercial & Agency Implementation License Granted<br/>
        <strong>Date of Compilation:</strong> October 2026
    </div>
</div>

<div class="content-body">
{body_html}
</div>

</body>
</html>
"""
    return html

def main():
    print("[*] Generating 100-Prompt Master Asset...")
    md_content = build_markdown_content()

    product_asset_path = BASE_DIR / "product_asset.md"
    with open(product_asset_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[+] Saved master Markdown to {product_asset_path} ({len(md_content)} bytes)")

    print("[*] Generating Styled Executive HTML...")
    html_content = build_styled_html(md_content)
    html_path = BASE_DIR / "The_Autonomous_AI_Growth_Engine_2026.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[+] Saved HTML to {html_path}")

    pdf_path = BASE_DIR / "The_Autonomous_AI_Growth_Engine_2026.pdf"
    print("[*] Printing Executive PDF using Headless Chrome...")
    chrome_cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={pdf_path}",
        str(html_path)
    ]
    res = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if res.returncode == 0 and pdf_path.exists():
        pdf_size = pdf_path.stat().st_size
        print(f"[+] Successfully compiled PDF to {pdf_path} ({pdf_size} bytes)")
    else:
        print(f"[-] PDF compilation warning: {res.stderr}")

    # Prepare customer package directory
    pkg_dir = RELEASE_DIR / "The_Autonomous_AI_Growth_Engine_v2.4_BUNDLE"
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)
    pkg_dir.mkdir(parents=True, exist_ok=True)

    # Copy PDF
    if pdf_path.exists():
        shutil.copy2(pdf_path, pkg_dir / "The_Autonomous_AI_Growth_Engine_2026.pdf")

    # Copy Raw Markdown Vault
    shutil.copy2(product_asset_path, pkg_dir / "100_Enterprise_AI_Prompts_Vault.md")

    # Write README_START_HERE.md
    readme_content = """# The Autonomous AI Growth Engine (2026 Edition)
Welcome! Thank you for investing in the Autonomous AI Growth Engine.

## What's in Your Package:
1. **The_Autonomous_AI_Growth_Engine_2026.pdf** - Complete executive master guide and prompt documentation.
2. **100_Enterprise_AI_Prompts_Vault.md** - Clean, copy-pasteable Markdown prompt database for Claude, ChatGPT, and Gemini.
3. **Automated_Distribution_Engine/** - Complete Python source code and CSV templates to run your own multi-channel social engine on autopilot.
4. **COMMERCIAL_LICENSE.md** - Full commercial and agency implementation license.

## Quick-Start:
- Open `The_Autonomous_AI_Growth_Engine_2026.pdf` to read the foundational architectures and SOPs.
- Navigate to `Automated_Distribution_Engine/` and inspect `README.md` to deploy the Python auto-poster.

Enjoy scaling your revenue engine on autopilot!
"""
    with open(pkg_dir / "README_START_HERE.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    # Write COMMERCIAL_LICENSE.md
    license_content = """# Commercial & Implementation License

This purchase grants the individual or purchasing entity a perpetual, non-exclusive, worldwide Commercial Implementation License.

### You Are Permitted To:
- Deploy these prompts and SOPs across unlimited internal projects and company workflows.
- Deploy and execute these prompts on behalf of client accounts and agency deliverables.
- Modify, customize, and integrate the Python distribution engine into private internal infrastructure.

### You Are NOT Permitted To:
- Resell, redistribute, or publicly publish this raw prompt bundle or PDF file as a standalone digital template.
"""
    with open(pkg_dir / "COMMERCIAL_LICENSE.md", "w", encoding="utf-8") as f:
        f.write(license_content)

    # Bundle Distribution Engine
    target_distrib = pkg_dir / "Automated_Distribution_Engine"
    target_distrib.mkdir(parents=True, exist_ok=True)
    for fname in ["auto_poster.py", "promotional_tips.csv", "requirements.txt", "README.md"]:
        src = DISTRIB_DIR / fname
        if src.exists():
            shutil.copy2(src, target_distrib / fname)

    # Create .env.example
    with open(target_distrib / ".env.example", "w", encoding="utf-8") as f:
        f.write("""# Zernio Social API Credentials
ZERNIO_API_KEY=your_zernio_api_key_here
LINKEDIN_ACCOUNT_ID=your_linkedin_account_id
X_ACCOUNT_ID=your_x_account_id
LANDING_PAGE_URL=https://your-domain.com
""")

    # Create ZIP archive
    zip_dest = RELEASE_DIR / "Autonomous_AI_Growth_Engine_v2.4_BUNDLE.zip"
    print(f"[*] Packaging final ZIP archive to {zip_dest}...")
    with zipfile.ZipFile(zip_dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(pkg_dir):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(RELEASE_DIR)
                zf.write(file_path, arcname)

    print(f"[+] ZIP bundle created: {zip_dest} ({zip_dest.stat().st_size} bytes)")
    print("[SUCCESS] All digital assets compiled and packaged.")

if __name__ == "__main__":
    main()
