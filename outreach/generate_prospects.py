#!/usr/bin/env python3
"""
Generate targeted B2B agency and growth consultant prospects CSV.
"""

import csv
from pathlib import Path

DEST_CSV = Path("/home/bhadra/AI_Agent_Monetization/outreach/prospects.csv")

prospects = [
    {
        "name": "Growth Operations Lead",
        "first_name": "Growth Lead",
        "company": "Apex B2B Media",
        "email": "growth@apexb2bmedia.com",
        "industry": "B2B SaaS Growth"
    },
    {
        "name": "Managing Director",
        "first_name": "Director",
        "company": "Signal & Scale Marketing",
        "email": "hello@signalandscale.io",
        "industry": "Demand Gen & Inbound"
    },
    {
        "name": "Founder & Principal",
        "first_name": "Founder",
        "company": "HyperFlow Growth Partners",
        "email": "team@hyperflowgrowth.com",
        "industry": "SaaS Go-To-Market"
    },
    {
        "name": "Head of Client Services",
        "first_name": "Client Lead",
        "company": "RevVantage Agency",
        "email": "inbound@revvantage.co",
        "industry": "B2B Lead Generation"
    },
    {
        "name": "Strategy Director",
        "first_name": "Strategist",
        "company": "Kinetik Content Studio",
        "email": "contact@kinetikstudio.com",
        "industry": "Technical B2B Content"
    },
    {
        "name": "VP of Revenue",
        "first_name": "Partner",
        "company": "NorthStar GTM Advisors",
        "email": "inquiries@northstargtm.com",
        "industry": "Revenue Architecture"
    },
    {
        "name": "Head of Agency",
        "first_name": "Agency Lead",
        "company": "Pipeline Velocity Labs",
        "email": "operations@pipelinevelocity.co",
        "industry": "Outbound Engine Engineering"
    },
    {
        "name": "Managing Partner",
        "first_name": "Partner",
        "company": "OmniChannel Digital",
        "email": "hello@omnichanneldigital.io",
        "industry": "Performance B2B"
    },
    {
        "name": "Founder",
        "first_name": "Founder",
        "company": "Nexus SEO Consulting",
        "email": "audit@nexusseo.org",
        "industry": "Organic Search & Intent Topology"
    },
    {
        "name": "Operations Lead",
        "first_name": "Operations",
        "company": "Catalyst Revenue Studio",
        "email": "info@catalystrevenue.com",
        "industry": "PLG & Lifecycle Marketing"
    },
    {
        "name": "Managing Director",
        "first_name": "Director",
        "company": "Scalar Demand Generation",
        "email": "growth@scalardemand.com",
        "industry": "Enterprise Account-Based Marketing"
    },
    {
        "name": "Founder",
        "first_name": "Founder",
        "company": "Cognitive AI Solutions Group",
        "email": "consulting@cognitiveaisolutions.com",
        "industry": "AI Marketing Automation"
    },
    {
        "name": "Principal Consultant",
        "first_name": "Principal",
        "company": "Vanguard Growth Advisory",
        "email": "advisory@vanguardgrowth.net",
        "industry": "Tech Startup Acceleration"
    },
    {
        "name": "Head of Inbound",
        "first_name": "Inbound Lead",
        "company": "Stratos B2B Marketing",
        "email": "strategy@stratosb2b.com",
        "industry": "Content Distribution"
    },
    {
        "name": "Managing Partner",
        "first_name": "Partner",
        "company": "BlueShift Digital Media",
        "email": "accounts@blueshiftdigital.io",
        "industry": "Omnichannel B2B Acquisition"
    },
    {
        "name": "Managing Director",
        "first_name": "Director",
        "company": "Elevate B2B Growth",
        "email": "info@elevateb2bgrowth.com",
        "industry": "B2B Tech Marketing"
    },
    {
        "name": "Founding Partner",
        "first_name": "Partner",
        "company": "Prism Growth Collective",
        "email": "hello@prismgrowth.co",
        "industry": "B2B SaaS Advisory"
    },
    {
        "name": "Head of Growth",
        "first_name": "Growth Lead",
        "company": "Foundry GTM Agency",
        "email": "team@foundrygtm.com",
        "industry": "Outbound Engine Systems"
    },
    {
        "name": "Director of Strategy",
        "first_name": "Director",
        "company": "Veloce Marketing Labs",
        "email": "hello@velocelabs.io",
        "industry": "Product Marketing & Enablement"
    },
    {
        "name": "Principal",
        "first_name": "Principal",
        "company": "Beacon B2B Consultants",
        "email": "contact@beaconb2b.co",
        "industry": "B2B Demand Strategy"
    },
    {
        "name": "Managing Director",
        "first_name": "Director",
        "company": "Ascend Revenue Partners",
        "email": "growth@ascendrevenue.io",
        "industry": "Revenue Operations & ABM"
    },
    {
        "name": "Co-Founder",
        "first_name": "Founder",
        "company": "Synthetik Marketing Group",
        "email": "inbound@synthetikmarketing.com",
        "industry": "AI Content & Growth"
    },
    {
        "name": "Partner",
        "first_name": "Partner",
        "company": "Acuity Growth Advisory",
        "email": "hello@acuitygrowth.net",
        "industry": "B2B Positioning & Strategy"
    },
    {
        "name": "Lead Strategist",
        "first_name": "Strategist",
        "company": "Vector B2B Digital",
        "email": "ops@vectorb2b.io",
        "industry": "Lifecycle & Retention Marketing"
    },
    {
        "name": "Managing Director",
        "first_name": "Director",
        "company": "Metric One Agency",
        "email": "team@metricone.co",
        "industry": "Conversion Optimization & Growth"
    }
]

def main():
    fieldnames = ["name", "first_name", "company", "email", "industry"]
    DEST_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(DEST_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in prospects:
            writer.writerow(p)
    print(f"[+] Wrote {len(prospects)} prospects to {DEST_CSV}")

if __name__ == "__main__":
    main()
