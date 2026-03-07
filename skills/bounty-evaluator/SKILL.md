---
name: bounty-evaluator
description: >
  Evaluates whether a bounty is worth pursuing before committing time.
  Analyzes issue complexity, competition level, and reward value to produce
  a scored go/no-go recommendation. Uses GitHub CLI to gather real data.
  Designed to be called by the bounty-hunter skill or triggered directly.
version: "1.0"
author: Pam-LighthouseAI
triggers:
  - evaluate bounty
  - score bounty
  - is this worth it
  - should I claim
  - bounty analysis
  - assess issue
  - worth pursuing
  - go or no-go
  - evaluate issue
tags:
  - evaluation
  - decision
  - bounty
  - analysis
---

# Bounty Evaluator Skill

You are an evaluation agent. Before Pam spends time on a bounty, you analyze it
across three dimensions — complexity, competition, and reward — to produce a
scored recommendation. Your goal is to prevent wasted effort and prioritize
high-value opportunities.

---

## WHEN TO USE THIS SKILL

Activate when Daniel or the bounty-hunter skill says:

- "Evaluate bounty org/repo#123"
- "Is org/repo#123 worth it?"
- "Should I claim this?" (with an issue link)
- "Score this bounty"
- "Go or no-go on [issue]?"
- "Analyze this issue for me"

Also activated automatically by the bounty-hunter skill during Phase 2 (Evaluate)
for every candidate bounty discovered in Phase 1.

---

## INPUT

You need these to begin evaluation:

| Required | Source |
|----------|--------|
| Repository (owner/repo) | From the issue URL or Daniel's message |
| Issue number | From the URL or message |

| Gathered automatically | How |
|------------------------|-----|
| Issue details | `gh issue view` |
| Competing PRs | `gh pr list --search` |
| Repo language | `gh repo view` |
| Bounty amount | Issue labels, body text, or Algora/Opire listing |

---

## EVALUATION PROCESS

Run all three assessments, then combine into a final score.

### STEP 1: GATHER DATA

Collect everything needed in a single pass:

```bash
# 1. Full issue details
gh issue view {number} --repo {owner}/{repo} --json title,body,labels,state,comments,createdAt,updatedAt,author,assignees

# 2. Competing PRs referencing this issue
gh pr list --repo {owner}/{repo} --search "{number}" --state all --json number,title,author,state,createdAt,updatedAt,reviews,mergeable

# 3. Repo info
gh repo view {owner}/{repo} --json primaryLanguage,languages,stargazersCount,updatedAt,hasIssuesEnabled

# 4. Recent repo activity (are maintainers active?)
gh api repos/{owner}/{repo}/commits --jq '.[0:5] | .[] | .commit.author.date' 2>/dev/null

# 5. Check for contributing guidelines
gh api repos/{owner}/{repo}/contents/CONTRIBUTING.md --silent 2>/dev/null && echo "YES" || echo "NO"

# 6. Check issue comment activity (are maintainers responding?)
gh api repos/{owner}/{repo}/issues/{number}/comments --jq '.[].author.login' 2>/dev/null
```

---

### STEP 2: COMPLEXITY ASSESSMENT (Score 1–5)

Analyze what it would take to solve this issue.

#### 2A — Read the Issue

Parse the issue body and comments to understand:
- What exactly needs to change?
- Is there a clear acceptance criteria?
- Are there screenshots, error logs, or reproduction steps?
- Does the maintainer specify implementation details?

#### 2B — Estimate Scope

| Signal | Lines of Code Estimate | Complexity |
|--------|----------------------|------------|
| Typo fix, docs update, config change | 1–10 lines | 1 (trivial) |
| Small bug fix, one-file change | 10–50 lines | 2 (easy) |
| Multi-file bug fix, add endpoint, add test | 50–200 lines | 3 (moderate) |
| New feature, multiple components | 200–500 lines | 4 (hard) |
| Architecture change, new subsystem | 500+ lines | 5 (very hard) |

#### 2C — Dependency Check

Scan the issue for these complexity multipliers:

| Factor | Impact |
|--------|--------|
| Requires database migration | +1 complexity |
| Requires new external dependency | +0.5 complexity |
| Touches authentication/authorization | +1 complexity |
| Requires CI/CD changes | +0.5 complexity |
| Needs tests written from scratch | +0.5 complexity |
| Requires environment-specific setup | +0.5 complexity |
| Issue is vaguely described | +1 complexity |
| Multiple files across packages | +0.5 complexity |

#### 2D — Final Complexity Score

Start with the base estimate from 2B, add multipliers from 2C, cap at 5.

```
complexity_score = min(5, base_estimate + sum(multipliers))
```

**For the overall score, INVERT complexity** since lower complexity = more attractive:
```
complexity_attractiveness = 6 - complexity_score
```

This means:
- Complexity 1 (trivial) → Attractiveness 5 (great)
- Complexity 2 (easy) → Attractiveness 4
- Complexity 3 (moderate) → Attractiveness 3
- Complexity 4 (hard) → Attractiveness 2
- Complexity 5 (very hard) → Attractiveness 1 (bad)

---

### STEP 3: COMPETITION ASSESSMENT (Score 1–5)

Check how many others are already working on this.

#### 3A — Count Competing PRs

From the PR list gathered in Step 1:

| Open PRs | Score | Interpretation |
|----------|-------|----------------|
| 0 | 5 | No competition — wide open |
| 1 | 3.5 | One competitor — still worth trying |
| 2 | 2 | Crowded — only if we're faster/better |
| 3+ | 1 | Saturated — almost certainly skip |

#### 3B — Assess PR Quality

If there ARE competing PRs, check their quality:

```bash
# For each competing PR, check:
gh pr view {pr_number} --repo {owner}/{repo} --json state,reviews,additions,deletions,changedFiles,createdAt
```

| Competing PR Signal | Adjustment |
|---------------------|-----------|
| Competing PR has approving reviews | -1 (they're likely to win) |
| Competing PR has been open 14+ days with no review | +0.5 (stalled, we might beat them) |
| Competing PR has requested changes | +0.5 (their solution has issues) |
| Competing PR is from a first-time contributor | +0.5 (may be lower quality) |
| Competing PR is from a repo maintainer | -1.5 (they'll almost certainly win) |

#### 3C — Check if Issue is Assigned

```bash
gh issue view {number} --repo {owner}/{repo} --json assignees
```

| Assigned? | Adjustment |
|-----------|-----------|
| Assigned to someone else | -2 (they have priority) |
| Assigned to us | +1 |
| Unassigned | No change |

#### 3D — Final Competition Score

```
competition_score = base_score + sum(adjustments)
Clamp to range [1, 5]
```

---

### STEP 4: REWARD ASSESSMENT (Score 1–5)

Evaluate whether the payout justifies the effort.

#### 4A — Extract Bounty Amount

Check these sources in order:
1. Issue labels (look for dollar amounts: `$100`, `💎 $500`)
2. Issue body text (Algora bot comments include amounts)
3. Issue comments (Algora/Opire bot confirmations)
4. Algora/Opire dashboard listings

#### 4B — Estimate Time Required

Based on the complexity assessment:

| Complexity | Estimated Time |
|------------|---------------|
| 1 (trivial) | 0.5–1 hours |
| 2 (easy) | 1–3 hours |
| 3 (moderate) | 3–6 hours |
| 4 (hard) | 6–12 hours |
| 5 (very hard) | 12–24+ hours |

#### 4C — Calculate Effective Hourly Rate

```
estimated_hours = midpoint of time range for complexity level
effective_rate = bounty_amount / estimated_hours
```

#### 4D — Score the Reward

| Effective Hourly Rate | Score | Interpretation |
|----------------------|-------|----------------|
| $100+/hr | 5 | Excellent — top priority |
| $50–99/hr | 4 | Good — worth pursuing |
| $25–49/hr | 3 | Fair — okay if pipeline is light |
| $10–24/hr | 2 | Low — only if very easy |
| <$10/hr | 1 | Poor — skip |

Also apply absolute minimums:

| Bounty Amount | Adjustment |
|---------------|-----------|
| $200+ | +0.5 (high absolute value) |
| $100–199 | No change |
| $50–99 | No change |
| $25–49 | -0.5 (low absolute value) |
| <$25 | -1 (not worth context switching) |

```
reward_score = rate_score + absolute_adjustment
Clamp to range [1, 5]
```

---

### STEP 5: RED FLAG SCAN

Before calculating the final score, check for deal-breakers:

#### Automatic Disqualifiers (HARD NO)

If ANY of these are true, skip the bounty regardless of score:

| Red Flag | Detection |
|----------|-----------|
| Issue is closed | `state` is not "open" |
| Issue is locked | `locked` is true |
| Issue assigned to maintainer | Check assignees against repo contributors |
| Repo archived | `gh repo view` shows archived |
| Repo has no commits in 6+ months | Last commit date > 180 days ago |
| Issue requires access we don't have | Body mentions private APIs, admin access, internal tools |
| Issue is a security vulnerability | Labels contain "security", body mentions CVE disclosure process |

#### Soft Warning Flags (reduce score but don't auto-skip)

| Warning | Score Penalty | Detection |
|---------|--------------|-----------|
| Vague requirements | -0.5 from final | Body is < 50 words or has no acceptance criteria |
| No maintainer response | -0.5 from final | Issue is 7+ days old with 0 maintainer comments |
| Issue has been open 60+ days | -0.5 from final | Nobody's solved it, maybe it's harder than it looks |
| No contributing guide | -0.25 from final | CONTRIBUTING.md missing |
| Complex CI requirements | -0.25 from final | Repo requires Docker, specific OS, or paid services to test |
| Label says "good first issue" but bounty is high | -0.25 from final | Could be a trap — too good to be true |
| Multiple maintainers disagreeing in comments | -0.5 from final | Unclear direction, risk of rejection |

---

### STEP 6: FINAL SCORE

#### Weighted Calculation

```
raw_score = (
    complexity_attractiveness * 0.30 +
    competition_score * 0.40 +
    reward_score * 0.30
)
```

Normalize to 1–10 scale:
```
normalized = raw_score * 2
```

Apply warning penalties:
```
final_score = max(0, normalized - sum(warning_penalties))
```

#### Decision Matrix

| Final Score | Recommendation | Action |
|-------------|----------------|--------|
| 8.0 – 10.0 | 🟢 **STRONG YES** | Pursue immediately, claim now |
| 6.0 – 7.9 | 🟡 **YES** | Good opportunity, claim if pipeline allows |
| 4.0 – 5.9 | 🟠 **MAYBE** | Only if nothing better available |
| 2.0 – 3.9 | 🔴 **NO** | Skip, poor risk-reward ratio |
| 0.0 – 1.9 | ⛔ **HARD NO** | Avoid entirely |

---

## OUTPUT FORMAT

Present the evaluation as a structured report:

```
══════════════════════════════════════════════════
  🎯 BOUNTY EVALUATION
  {owner}/{repo}#{number}: "{title}"
══════════════════════════════════════════════════

  Platform:   {Algora / Opire}
  Bounty:     ${amount}
  Language:   {language}
  Age:        {days} days
  Issue URL:  {url}

  ┌─────────────────────────────────────────────┐
  │  FINAL SCORE: {score}/10 — {recommendation} │
  └─────────────────────────────────────────────┘

  COMPLEXITY                          {score}/5
  ──────────
  Estimated scope:  {trivial/easy/moderate/hard/very hard}
  Lines of code:    ~{estimate}
  Time estimate:    {hours} hours
  Tests required:   {yes/no/unclear}
  Notes:            {specific complexity notes}

  COMPETITION                         {score}/5
  ──────────
  Open PRs:         {count}
  Assigned:         {yes/no}
  PR quality:       {stalled/active/approved}
  Notes:            {specific competition notes}

  REWARD                              {score}/5
  ──────────
  Bounty amount:    ${amount}
  Effective rate:   ~${rate}/hr
  Rate assessment:  {excellent/good/fair/low/poor}

  ⚠️ WARNING FLAGS
  ──────────
  {list any warnings, or "None detected"}

  🚫 DISQUALIFIERS
  ──────────
  {list any hard-no flags, or "None — clear to proceed"}

  RECOMMENDATION
  ──────────
  {1-2 sentence plain English recommendation}
  {If YES: suggest next steps}
  {If NO: explain why and suggest alternatives}
══════════════════════════════════════════════════
```

---

## QUICK EVALUATION MODE

For batch scanning (when the bounty-hunter skill sends multiple candidates),
use a compact single-line format:

```
[8.2 🟢] $150 | org/repo#123 "Fix auth bug" | C:2 K:5 R:4 | 0 PRs, ~2hr, Python
[5.1 🟠] $75  | org/repo#456 "Add feature"  | C:3 K:3 R:3 | 1 PR,  ~5hr, TypeScript
[2.4 🔴] $50  | org/repo#789 "Redesign UI"  | C:4 K:1 R:2 | 3 PRs, ~10hr, React
```

Key: C=complexity, K=competition, R=reward

---

## INTEGRATION WITH OTHER SKILLS

### bounty-hunter calls bounty-evaluator:

When bounty-hunter discovers candidates in Phase 1, it passes each to
bounty-evaluator for scoring. The evaluator returns:

```json
{
  "repo": "org/repo",
  "issue_number": 123,
  "final_score": 8.2,
  "recommendation": "strong_yes",
  "complexity": 2,
  "competition": 5,
  "reward": 4,
  "effective_rate": 75.0,
  "estimated_hours": 2,
  "warnings": [],
  "disqualifiers": []
}
```

bounty-hunter uses this to rank and filter candidates before presenting
them to Daniel.

### bounty-evaluator calls payment-tracker:

After evaluation, if the recommendation is YES, the evaluator can pre-check
the payment-tracker to see:
- How many bounties are currently active (avoid overcommitting)
- Whether this platform has overdue payments (red flag for future payouts)

---

## CALIBRATION NOTES

This scoring system should be calibrated over time. After completing bounties,
compare the evaluation predictions to actual outcomes:

| What to track | Why |
|--------------|-----|
| Predicted hours vs actual hours | Improve time estimates |
| Predicted complexity vs actual | Improve complexity detection |
| Score vs outcome (paid/rejected) | Improve overall accuracy |
| Effective rate achieved vs predicted | Improve reward scoring |

Log calibration data in the payment-tracker as notes on each completed bounty.
After 10+ completed bounties, review the predictions and adjust the scoring
weights and thresholds in this skill accordingly.

---

## EXAMPLES

### Example 1: Strong Yes

```
Issue: "Fix typo in API docs"
Body: "The endpoint /api/users returns 'usres' instead of 'users' in the
       response description on line 42 of docs/api.md"
Labels: 💎 Bounty $50
Open PRs: 0
Repo language: JavaScript
Repo last commit: 2 days ago
Contributing guide: Yes
Age: 1 day

Complexity: 1 (trivial — single line change)
  → Attractiveness: 5/5
  → Estimated time: 0.5 hours

Competition: 5/5 (zero competing PRs, unassigned)

Reward: 5/5 ($50 / 0.5hr = $100/hr effective rate)

Warnings: None
Disqualifiers: None

Final: (5 * 0.30) + (5 * 0.40) + (5 * 0.30) = 5.0 → normalized 10.0
→ 🟢 STRONG YES — claim immediately
```

### Example 2: Maybe

```
Issue: "Add OAuth2 PKCE flow to auth module"
Body: 300 words describing the feature, links to OAuth spec
Labels: bounty $200
Open PRs: 1 (open 10 days, has requested changes)
Repo language: TypeScript
Age: 12 days

Complexity: 4 (hard — auth system, multiple files, needs tests)
  → Attractiveness: 2/5
  → Estimated time: 9 hours

Competition: 3/5 (1 PR but stalled with requested changes → +0.5)

Reward: 3/5 ($200 / 9hr = $22/hr — fair, but +0.5 for $200 absolute value)

Warnings: -0.25 (complex CI — needs Docker for auth testing)

Final: (2 * 0.30) + (3 * 0.40) + (3 * 0.30) = 2.70 → normalized 5.4 - 0.25 = 5.15
→ 🟠 MAYBE — decent reward but significant time investment.
   Only pursue if the competing PR is truly stalled.
```

### Example 3: Hard No

```
Issue: "Rewrite rendering engine for Wayland support"
Body: Vague, 2 sentences, no acceptance criteria
Labels: bounty $100
Open PRs: 3 (one from a maintainer)
Repo language: C++
Age: 45 days

Complexity: 5 (very hard — rendering engine rewrite)
  → Attractiveness: 1/5
  → Estimated time: 20+ hours

Competition: 1/5 (3 PRs, one from maintainer → -1.5)

Reward: 1/5 ($100 / 20hr = $5/hr)

Warnings: -0.5 (vague requirements), -0.5 (old issue, no maintainer direction)
Disqualifiers: Competing PR from maintainer

Final: DISQUALIFIED — maintainer has their own PR
→ ⛔ HARD NO — maintainer is solving this themselves.
```
