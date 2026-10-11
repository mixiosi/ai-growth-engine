#!/usr/bin/env python3
"""
Autonomous Social Media Distribution Engine (Zernio SDK)
Reads promotional tips and scheduled content from CSV and publishes them
across LinkedIn, X (Twitter), and other supported channels via Zernio Unified API.
"""

import os
import sys
import csv
import time
import argparse
from pathlib import Path

# Load environment variables from .env file if present
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

def load_promotional_tips(csv_path: str):
    """Load promotional tips from CSV file."""
    tips = []
    if not os.path.exists(csv_path):
        print(f"[-] CSV file not found: {csv_path}", file=sys.stderr)
        return tips

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tips.append(row)
    return tips

def format_post_content(row: dict) -> str:
    """Format row data into high-converting social media copy."""
    headline = row.get("headline", "").strip()
    hook = row.get("hook", "").strip()
    body = row.get("content", "").strip()
    cta = row.get("cta", "").strip()
    
    parts = []
    if headline:
        parts.append(headline.upper())
    if hook:
        parts.append(hook)
    if body:
        parts.append(body)
    if cta:
        parts.append(f"\n👉 {cta}")
        
    return "\n\n".join(parts)

def build_platform_targets(platform_pref: str, linkedin_id: str, x_id: str):
    """Build list of platform target dictionaries for Zernio API."""
    platforms = []
    pref = platform_pref.lower().strip()
    
    if pref in ["all", "linkedin"] and linkedin_id:
        platforms.append({"platform": "linkedin", "accountId": linkedin_id})
    if pref in ["all", "x", "twitter"] and x_id:
        platforms.append({"platform": "x", "accountId": x_id})
        
    # Fallback to default dummy IDs if none supplied for dry-run
    if not platforms:
        if pref in ["all", "linkedin"]:
            platforms.append({"platform": "linkedin", "accountId": "YOUR_ACCOUNT_ID"})
        if pref in ["all", "x", "twitter"]:
            platforms.append({"platform": "x", "accountId": "YOUR_ACCOUNT_ID"})
            
    return platforms

def main():
    parser = argparse.ArgumentParser(description="Autonomous Social Media Distribution Engine")
    parser.add_argument("--csv", default=str(Path(__file__).parent / "promotional_tips.csv"), help="Path to promotional CSV")
    parser.add_argument("--limit", type=int, default=3, help="Max posts to publish in this run")
    parser.add_argument("--dry-run", action="store_true", help="Simulate publishing without calling live API")
    parser.add_argument("--delay", type=int, default=2, help="Delay in seconds between posts")
    args = parser.parse_args()

    api_key = os.environ.get("ZERNIO_API_KEY", "").strip()
    linkedin_acc = os.environ.get("LINKEDIN_ACCOUNT_ID", "YOUR_ACCOUNT_ID").strip()
    x_acc = os.environ.get("X_ACCOUNT_ID", "YOUR_ACCOUNT_ID").strip()

    is_placeholder_key = not api_key or api_key in [
        "your_api_key_goes_here",
        "placeholder",
        "YOUR_ZERNIO_API_KEY",
    ]
    dry_run = args.dry_run or is_placeholder_key

    print("=" * 70)
    print("🚀 AUTONOMOUS SOCIAL MEDIA DISTRIBUTION ENGINE")
    print(f"📡 API Provider: Zernio Unified Social API (zernio-sdk)")
    print(f"📄 Source CSV:   {args.csv}")
    print(f"⚙️ Mode:         {'DRY-RUN / SIMULATION' if dry_run else 'LIVE PRODUCTION'}")
    if is_placeholder_key and not args.dry_run:
        print("ℹ️ Note: Placeholder API key detected in .env. Running in safe Dry-Run mode.")
        print("  To publish live: update ZERNIO_API_KEY in distribution_engine/.env")
    print("=" * 70)

    tips = load_promotional_tips(args.csv)
    if not tips:
        print("[-] No promotional tips found to publish.")
        return 1

    # Initialize Zernio client if in live mode
    client = None
    if not dry_run:
        try:
            from zernio import Zernio
            client = Zernio(api_key=api_key)
            print("[+] Zernio client successfully initialized with API key.")
        except Exception as e:
            print(f"[-] Failed to initialize Zernio client: {e}", file=sys.stderr)
            return 1

    to_publish = tips[: args.limit]
    print(f"[+] Loaded {len(tips)} tips from CSV. Publishing top {len(to_publish)} posts...\n")

    for idx, tip in enumerate(to_publish, 1):
        content = format_post_content(tip)
        platform_pref = tip.get("platform", "all")
        platforms = build_platform_targets(platform_pref, linkedin_acc, x_acc)
        topic = tip.get("topic", "General")

        print(f"--- [Post #{idx}/{len(to_publish)}] Topic: {topic} ---")
        print(f"Target Platforms: {[p['platform'] for p in platforms]}")
        print(f"Content Length:   {len(content)} characters")
        print("Preview:")
        print("-" * 40)
        for line in content.split("\n"):
            print(f"  {line}")
        print("-" * 40)

        if dry_run:
            simulated_id = f"sim_post_{int(time.time())}_{idx}"
            print(f"✓ [DRY-RUN] Simulated dispatch successful! Post ID: {simulated_id}\n")
        else:
            try:
                # Integration pattern from Zernio SDK
                result = client.posts.create_post(
                    content=content,
                    platforms=platforms,
                    publish_now=True
                )
                post_id = "unknown"
                if isinstance(result, dict):
                    if "post" in result and isinstance(result["post"], dict):
                        post_id = result["post"].get("_id", "unknown")
                    else:
                        post_id = result.get("_id", "unknown")
                print(f"Posted successfully! {post_id}\n")
            except Exception as err:
                print(f"[-] Failed to publish post #{idx}: {err}\n", file=sys.stderr)

        if idx < len(to_publish) and args.delay > 0:
            time.sleep(args.delay)

    print("=" * 70)
    print("✅ Distribution batch completed successfully.")
    print("=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main())
