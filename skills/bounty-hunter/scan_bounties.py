#!/usr/bin/env python3
"""
Bounty Scanner — Helper script for the bounty-hunter skill
============================================================
Scans GitHub for Algora and Opire bounties using the gh CLI.
Outputs a scored JSON report that Pam can read and act on.

Usage:
    python scan_bounties.py                    # Full scan
    python scan_bounties.py --min-reward 50    # Minimum $50 bounties
    python scan_bounties.py --platform algora  # Algora only
    python scan_bounties.py --platform opire   # Opire only

Requires: gh CLI authenticated (gh auth login)
"""

import subprocess
import json
import sys
import os
from datetime import datetime, timezone
from pathlib import Path

# ═══════════════════════════════════════════════════════════════
# CONFIGURATION — Pam or Daniel can adjust these
# ═══════════════════════════════════════════════════════════════

MIN_REWARD_DEFAULT = 25          # Minimum bounty amount in USD
OUR_LANGUAGES = ["python", "javascript", "typescript", "shell", "markdown", "yaml", "json", "css", "html"]
MAX_COMPETING_PRS = 2            # Skip bounties with more PRs than this
MAX_AGE_DAYS = 30                # Skip bounties older than this
RESULTS_FILE = "bounty_scan_results.json"

# Known Algora orgs that frequently post bounties (expand as discovered)
ALGORA_ORGS = [
    "activepieces", "calcom", "hoppscotch", "crowd-dev", "twenty",
    "highlight-io", "trigger-dev", "documenso", "formbricks", "infisical",
    "openbb-finance", "nangcr", "maybe-finance", "JuliaEarth", "Mudlet",
    "projectdiscovery", "windmill-labs",
]

# Bounty label patterns across both platforms
BOUNTY_LABELS = [
    "💎 Bounty",
    "bounty",
    "💰 Opire Reward",
    "💰 Reward",
    "reward",
    "💵",
    "paid",
]


# ═══════════════════════════════════════════════════════════════
# GITHUB CLI WRAPPER
# ═══════════════════════════════════════════════════════════════

def gh(args, timeout=30):
    """Run a gh CLI command and return parsed JSON output."""
    cmd = ["gh"] + args
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
        if result.returncode != 0:
            return None
        if result.stdout.strip():
            return json.loads(result.stdout)
        return None
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return None


def gh_text(args, timeout=30):
    """Run a gh CLI command and return raw text output."""
    cmd = ["gh"] + args
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
        return result.stdout.strip() if result.returncode == 0 else ""
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return ""


# ═══════════════════════════════════════════════════════════════
# BOUNTY DISCOVERY
# ═══════════════════════════════════════════════════════════════

def search_algora_bounties():
    """Search GitHub for issues with Algora bounty labels."""
    print("  Scanning Algora bounties...")
    issues = []

    # Search by common bounty labels
    for label in ["💎 Bounty", "bounty"]:
        results = gh([
            "search", "issues",
            "--label", label,
            "--state", "open",
            "--sort", "created",
            "--limit", "25",
            "--json", "number,title,repository,labels,createdAt,url,body,comments"
        ])
        if results:
            for item in results:
                item["_platform"] = "algora"
                item["_label_matched"] = label
                issues.append(item)

    # Search known Algora orgs
    for org in ALGORA_ORGS:
        results = gh([
            "search", "issues",
            "--owner", org,
            "--label", "bounty",
            "--state", "open",
            "--limit", "5",
            "--json", "number,title,repository,labels,createdAt,url,body,comments"
        ])
        if results:
            for item in results:
                item["_platform"] = "algora"
                item["_label_matched"] = f"org:{org}"
                issues.append(item)

    return _deduplicate(issues)


def search_opire_bounties():
    """Search GitHub for issues with Opire reward labels."""
    print("  Scanning Opire bounties...")
    issues = []

    for label in ["💰 Opire Reward", "💰 Reward", "reward"]:
        results = gh([
            "search", "issues",
            "--label", label,
            "--state", "open",
            "--sort", "created",
            "--limit", "20",
            "--json", "number,title,repository,labels,createdAt,url,body,comments"
        ])
        if results:
            for item in results:
                item["_platform"] = "opire"
                item["_label_matched"] = label
                issues.append(item)

    return _deduplicate(issues)


def _deduplicate(issues):
    """Remove duplicate issues (same repo + number)."""
    seen = set()
    unique = []
    for issue in issues:
        repo = issue.get("repository", {})
        key = f"{repo.get('nameWithOwner', '')}#{issue.get('number', '')}"
        if key not in seen:
            seen.add(key)
            unique.append(issue)
    return unique


# ═══════════════════════════════════════════════════════════════
# BOUNTY EVALUATION
# ═══════════════════════════════════════════════════════════════

def extract_reward_amount(issue):
    """Try to extract dollar amount from labels or issue body."""
    # Check labels for amount
    for label in issue.get("labels", []):
        name = label.get("name", "") if isinstance(label, dict) else str(label)
        # Match patterns like "$100", "💎 $500", "bounty:$200"
        import re
        amounts = re.findall(r'\$(\d+(?:,\d{3})*(?:\.\d{2})?)', name)
        if amounts:
            return float(amounts[0].replace(",", ""))

    # Check issue body for bounty amount
    body = issue.get("body", "") or ""
    import re
    amounts = re.findall(r'\$(\d+(?:,\d{3})*(?:\.\d{2})?)', body)
    if amounts:
        # Return the first amount found (usually the bounty)
        return float(amounts[0].replace(",", ""))

    return 0


def get_competing_prs(owner, repo, issue_number):
    """Count open PRs that reference this issue."""
    results = gh([
        "pr", "list",
        "--repo", f"{owner}/{repo}",
        "--search", str(issue_number),
        "--state", "open",
        "--json", "number,title,author"
    ])
    return results or []


def get_repo_language(owner, repo):
    """Get the primary language of a repository."""
    info = gh(["repo", "view", f"{owner}/{repo}", "--json", "primaryLanguage,languages"])
    if info:
        primary = info.get("primaryLanguage", {})
        return (primary.get("name", "") if primary else "").lower()
    return ""


def calculate_age_days(created_at):
    """Calculate how many days old an issue is."""
    try:
        created = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        return (now - created).days
    except:
        return 999


def score_bounty(reward, competing_prs, age_days, language_match, complexity_guess):
    """
    Calculate attractiveness score (1–10) using weighted factors.

    Weights: reward=25%, competition=25%, complexity=20%, skill=15%, freshness=15%
    """
    # Reward score
    if reward >= 200: reward_score = 10
    elif reward >= 100: reward_score = 7
    elif reward >= 50: reward_score = 5
    elif reward >= 25: reward_score = 3
    else: reward_score = 1

    # Competition score
    num_prs = len(competing_prs)
    if num_prs == 0: comp_score = 10
    elif num_prs == 1: comp_score = 6
    elif num_prs == 2: comp_score = 3
    else: comp_score = 1

    # Complexity score (rough guess based on title keywords)
    comp_map = {"docs": 9, "readme": 9, "typo": 9, "config": 8, "fix": 7,
                "bug": 7, "add": 6, "feature": 5, "refactor": 4, "redesign": 3}
    complexity_score = comp_map.get(complexity_guess, 5)

    # Skill match
    skill_score = 10 if language_match else 4

    # Freshness
    if age_days <= 3: fresh_score = 10
    elif age_days <= 7: fresh_score = 7
    elif age_days <= 14: fresh_score = 5
    elif age_days <= 30: fresh_score = 3
    else: fresh_score = 1

    total = (
        reward_score * 0.25 +
        comp_score * 0.25 +
        complexity_score * 0.20 +
        skill_score * 0.15 +
        fresh_score * 0.15
    )

    return round(total, 1), {
        "reward": reward_score,
        "competition": comp_score,
        "complexity": complexity_score,
        "skill_match": skill_score,
        "freshness": fresh_score,
    }


def guess_complexity(title):
    """Rough complexity guess from issue title keywords."""
    title_lower = title.lower()
    for keyword in ["docs", "readme", "documentation", "typo", "spelling"]:
        if keyword in title_lower:
            return "docs"
    for keyword in ["config", "env", "variable", "setting"]:
        if keyword in title_lower:
            return "config"
    for keyword in ["fix", "bug", "error", "crash", "broken"]:
        if keyword in title_lower:
            return "fix"
    for keyword in ["add", "new", "create", "implement"]:
        if keyword in title_lower:
            return "add"
    for keyword in ["refactor", "rewrite", "redesign", "migrate"]:
        if keyword in title_lower:
            return "refactor"
    return "feature"


# ═══════════════════════════════════════════════════════════════
# MAIN SCAN
# ═══════════════════════════════════════════════════════════════

def run_scan(min_reward=MIN_REWARD_DEFAULT, platform="all"):
    """Run a full bounty scan and return scored results."""
    print(f"\n🎯 Bounty Scanner — Scanning {'all platforms' if platform == 'all' else platform}")
    print(f"   Min reward: ${min_reward} | Max age: {MAX_AGE_DAYS} days\n")

    all_issues = []

    if platform in ("all", "algora"):
        all_issues += search_algora_bounties()

    if platform in ("all", "opire"):
        all_issues += search_opire_bounties()

    print(f"\n  Found {len(all_issues)} raw results. Evaluating...\n")

    scored = []

    for issue in all_issues:
        repo_info = issue.get("repository", {})
        full_name = repo_info.get("nameWithOwner", "unknown/unknown")
        owner, repo = full_name.split("/") if "/" in full_name else ("unknown", "unknown")
        number = issue.get("number", 0)
        title = issue.get("title", "")
        created = issue.get("createdAt", "")
        url = issue.get("url", "")

        # Age filter
        age = calculate_age_days(created)
        if age > MAX_AGE_DAYS:
            continue

        # Extract reward
        reward = extract_reward_amount(issue)

        # Reward filter
        if reward < min_reward and reward > 0:
            continue

        # Language check
        lang = get_repo_language(owner, repo)
        lang_match = lang in OUR_LANGUAGES

        # Competition check
        competing = get_competing_prs(owner, repo, number)
        if len(competing) > MAX_COMPETING_PRS:
            continue

        # Score it
        complexity = guess_complexity(title)
        total_score, breakdown = score_bounty(reward, competing, age, lang_match, complexity)

        scored.append({
            "platform": issue.get("_platform", "unknown"),
            "repo": full_name,
            "number": number,
            "title": title,
            "url": url,
            "reward_usd": reward,
            "age_days": age,
            "competing_prs": len(competing),
            "language": lang,
            "language_match": lang_match,
            "complexity": complexity,
            "score": total_score,
            "score_breakdown": breakdown,
            "created_at": created,
        })

    # Sort by score descending
    scored.sort(key=lambda x: x["score"], reverse=True)

    return scored


def print_report(scored):
    """Print a human-readable report."""
    if not scored:
        print("  No bounties found matching your criteria.\n")
        return

    print(f"\n{'='*80}")
    print(f"  🎯 BOUNTY REPORT — {len(scored)} candidates found")
    print(f"{'='*80}\n")

    for i, b in enumerate(scored[:15], 1):
        stars = "⭐" * min(int(b["score"]), 10)
        reward_str = f"${b['reward_usd']:.0f}" if b["reward_usd"] > 0 else "???"
        print(f"  {i:2}. [{b['score']:4.1f}] {stars}")
        print(f"      {b['platform'].upper()} | {b['repo']}#{b['number']}")
        print(f"      \"{b['title']}\"")
        print(f"      Reward: {reward_str} | PRs: {b['competing_prs']} | Age: {b['age_days']}d | Lang: {b['language'] or '?'}")
        print(f"      {b['url']}")
        print()

    # Summary
    high = [b for b in scored if b["score"] >= 7]
    med = [b for b in scored if 5 <= b["score"] < 7]
    print(f"  Summary: {len(high)} high-score (≥7), {len(med)} medium (5-6), "
          f"{len(scored) - len(high) - len(med)} low (<5)")
    if high:
        total_pot = sum(b["reward_usd"] for b in high)
        print(f"  Potential earnings from top picks: ${total_pot:.0f}")
    print()


def save_results(scored, filepath=RESULTS_FILE):
    """Save results to JSON for Pam to read."""
    output = {
        "scan_time": datetime.now(timezone.utc).isoformat(),
        "total_found": len(scored),
        "results": scored,
    }
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    print(f"  Results saved to {filepath}\n")


# ═══════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Bounty Scanner for Algora & Opire")
    parser.add_argument("--min-reward", type=int, default=MIN_REWARD_DEFAULT,
                        help=f"Minimum reward in USD (default: ${MIN_REWARD_DEFAULT})")
    parser.add_argument("--platform", choices=["all", "algora", "opire"], default="all",
                        help="Platform to scan (default: all)")
    parser.add_argument("--output", default=RESULTS_FILE,
                        help=f"Output file (default: {RESULTS_FILE})")
    args = parser.parse_args()

    # Verify gh CLI
    auth = gh_text(["auth", "status"])
    if "not logged in" in auth.lower() or not auth:
        print("  ❌ GitHub CLI not authenticated. Run: gh auth login")
        sys.exit(1)

    results = run_scan(min_reward=args.min_reward, platform=args.platform)
    print_report(results)
    save_results(results, args.output)
