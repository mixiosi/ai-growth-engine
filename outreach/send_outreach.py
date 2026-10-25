#!/usr/bin/env python3
"""
Autonomous B2B Cold Email Outreach Engine
Executes targeted outbound campaigns to generate sales for The Autonomous AI Growth Engine.
Supports Gmail SMTP automated dispatch or generates 1-click web compose & mailto links.
"""

import os
import sys
import csv
import smtplib
import argparse
import urllib.parse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROSPECTS_FILE = BASE_DIR / "prospects.csv"
OUTREACH_ENV = BASE_DIR / ".env"

# Load environment if present
if OUTREACH_ENV.exists():
    with open(OUTREACH_ENV, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ[k.strip()] = v.strip().strip('"').strip("'")

EMAIL_SUBJECT = "quick question regarding {company}'s AI workflows"

EMAIL_BODY_TEMPLATE = """Hi {first_name},

Saw your recent work at {company} in the {industry} space.

Most B2B agencies and growth teams I speak with are trying to move past generic AI prompts that spit out robotic copy and get zero organic reach.

I just engineered a complete production-grade asset: The Autonomous AI Growth Engine (2026 Enterprise Edition). It includes:
- 100 battle-tested enterprise prompts across Inbound, Outbound, PLG, Social, and Retention
- 4 production SOPs (Weekly Content Engine, Competitor Battlecards, ICP Scoring, Churn Detection)
- An automated Python social media distribution engine
- Full commercial & agency implementation license (deploy for client deliverables)

It's currently on a launch special for $47 (instant digital download):
👉 {checkout_url}

If you or your team are looking to standardize your AI growth workflows this quarter, I think you'll get huge value from the architecture.

Best regards,
Chris Klatt
AI Growth Engineering Labs
chris.growthlabs@gmail.com
https://mixiosi.gumroad.com/l/nshou
"""

def load_prospects(csv_path):
    prospects = []
    if not os.path.exists(csv_path):
        print(f"[-] Prospects file not found: {csv_path}", file=sys.stderr)
        return prospects
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            prospects.append(r)
    return prospects

def send_smtp_campaign(prospects, checkout_url, host, port, user, password, dry_run=True, delay=15):
    import time
    print("=" * 75)
    print("🚀 GMAIL AUTOMATED SMTP OUTREACH ENGINE")
    print(f"📧 Sender: {user}")
    print(f"⚙️ Mode:   {'DRY-RUN (Simulation)' if dry_run else 'LIVE PRODUCTION DISPATCH'}")
    print(f"📄 Target: {len(prospects)} Verified Prospects")
    print("=" * 75 + "\n")

    if not dry_run:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(user, password)
        print(f"[+] Successfully authenticated with Gmail SMTP server {host}:{port} as {user}\n")
    else:
        server = None

    for idx, p in enumerate(prospects, 1):
        first_name = p.get("first_name", "there").strip()
        company = p.get("company", "your team").strip()
        industry = p.get("industry", "B2B").strip()
        email = p.get("email", "").strip()

        subject = EMAIL_SUBJECT.format(company=company)
        body = EMAIL_BODY_TEMPLATE.format(
            first_name=first_name,
            company=company,
            industry=industry,
            checkout_url=checkout_url
        )

        print(f"--- [Outreach #{idx}/{len(prospects)}] To: {email} ({company}) ---")
        print(f"Subject: {subject}")
        print("Body Preview (first 3 lines):")
        for line in body.split("\n")[:3]:
            print(f"  {line}")

        if dry_run:
            print(f"✓ [DRY-RUN] Simulated dispatch to {email} succeeded.\n")
        else:
            msg = MIMEMultipart()
            msg["From"] = f"Chris Klatt <{user}>"
            msg["To"] = email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain", "utf-8"))
            try:
                server.sendmail(user, email, msg.as_string())
                print(f"✅ Dispatched successfully to {email}!\n")
            except Exception as e:
                print(f"[-] Failed to dispatch to {email}: {e}\n", file=sys.stderr)

            if idx < len(prospects) and delay > 0:
                print(f"⏳ Waiting {delay}s before next dispatch to maintain high sender reputation...")
                time.sleep(delay)

    if server:
        server.quit()
        print("[+] SMTP session closed cleanly.")

def main():
    parser = argparse.ArgumentParser(description="Autonomous Cold Email Outreach Engine")
    parser.add_argument("--csv", default=str(PROSPECTS_FILE), help="Path to prospects CSV")
    parser.add_argument("--checkout-url", default="https://mixiosi.gumroad.com/l/nshou?wanted=true", help="Checkout URL")
    parser.add_argument("--send", action="store_true", help="Dispatch via SMTP")
    parser.add_argument("--dry-run", action="store_true", default=False, help="Simulate without sending")
    parser.add_argument("--delay", type=int, default=15, help="Delay in seconds between emails")
    args = parser.parse_args()

    prospects = load_prospects(args.csv)
    if not prospects:
        print("[-] No prospects found in CSV.")
        return 1

    host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    port = int(os.environ.get("SMTP_PORT", 587))
    user = os.environ.get("SMTP_USER", "chris.growthlabs@gmail.com")
    password = os.environ.get("SMTP_PASSWORD", "")

    dry_run = not args.send or not password or args.dry_run

    if args.send and not password:
        print("ℹ️ Note: SMTP_PASSWORD not found in outreach/.env. Running in safe Dry-Run mode.")
        print("  To send live: add your Google App Password to outreach/.env and re-run.")

    send_smtp_campaign(prospects, args.checkout_url, host, port, user, password, dry_run=dry_run, delay=args.delay)
    return 0

if __name__ == "__main__":
    sys.exit(main())
