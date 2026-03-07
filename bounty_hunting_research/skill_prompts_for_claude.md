# Expert Prompts for Claude Code

*Created: 2026-03-04*
*Purpose: Prompts Daniel can give to Claude Code to build skills for Pam*

---

## How to Use These Prompts

Copy each prompt below and paste into Claude Code. Claude Code will build the skill file structure for you.

Each prompt includes:
- Context about what the skill needs to do
- Technical requirements (commands, APIs)
- Skill.md template structure
- Integration with nanobot's existing capabilities

---

## Prompt 1: Bounty Hunter Skill

```
You are an expert at creating nanobot skills. Create a complete "bounty-hunter" skill for autonomous bounty hunting on Algora and Opire platforms.

## Context

Pam is an AI assistant running on nanobot. She needs to autonomously find, evaluate, and submit bounties on:
- Algora.io (primary platform)
- Opire.dev (secondary platform)

She already has:
- GitHub CLI (`gh`) authenticated as Pam-LighthouseAI
- Web search capability
- File operations (read, write, edit)
- Memory system for tracking state

## Requirements

The skill should enable Pam to:

1. **Discover Bounties**
   - Scan Algora bounty board (https://algora.io/bounties)
   - Scan Opire issue list (https://app.opire.dev/issues)
   - Filter by skill match (Python, JavaScript, TypeScript, etc.)
   - Filter by bounty amount (minimum threshold configurable)
   - Filter by age (newer bounties = less competition)

2. **Evaluate Bounties**
   - Check if issue is still open
   - Check for existing PRs (competition level)
   - Assess complexity vs reward ratio
   - Estimate time to complete
   - Score bounty attractiveness (1-10)

3. **Claim Bounties**
   - Algora: Add `/claim #issue-number` in PR body
   - Opire: Use bot command or dashboard claim
   - Track claim status in memory

4. **Submit Solutions**
   - Clone repository
   - Create feature branch
   - Implement solution
   - Create PR with proper claim command
   - Reference issue in PR

5. **Track Status**
   - Monitor PR status (open, merged, closed)
   - Track payment status
   - Log all bounty activity to memory

## Technical Details

### Algora Claim Format
```
/claim #123
```
For joint contributions:
```
/claim #123 /split @username
```

### Opire Claim Format
Use Opire bot commands in issue comments or claim via dashboard.

### Payment Flow
- Algora: AutoPay triggers on merge, 1-3 days to Stripe
- Opire: Customer confirms, then Stripe payout

### Memory Tracking
Store in memory/MEMORY.md:
- Active bounties being worked
- Claimed bounties awaiting merge
- Completed bounties and payouts
- Running total of earnings

## Skill Structure

Create a SKILL.md file with:
- YAML frontmatter (name, description, metadata)
- When to use section
- Step-by-step workflow
- Command templates
- Decision criteria
- Error handling

## Output

Generate the complete SKILL.md file and any supporting scripts needed. Place in workspace/skills/bounty-hunter/SKILL.md
```

---

## Prompt 2: Payment Tracker Skill

```
You are an expert at creating nanobot skills. Create a complete "payment-tracker" skill for tracking bounty earnings, payouts, and tax obligations.

## Context

Pam is an AI assistant running on nanobot. She needs to track financial activity from bounty hunting on Algora and Opire platforms.

She already has:
- Memory system (MEMORY.md, HISTORY.md)
- File operations
- Web search capability
- bounty-hunter skill (for integration)

## Requirements

The skill should enable Pam to:

1. **Track Earnings**
   - Log each bounty claimed with:
     - Platform (Algora/Opire)
     - Bounty amount
     - Issue URL
     - PR URL
     - Claim date
     - Status (claimed, merged, paid)
   - Store in structured format (JSON or markdown table)

2. **Track Payouts**
   - Monitor payment status
   - Log payout dates
   - Track Stripe transaction IDs
   - Calculate pending vs received

3. **Tax Tracking** (US-focused)
   - Track total earnings per year
   - Flag when approaching $600 threshold (1099-NEC requirement)
   - Generate annual summary for tax purposes
   - Note: Algora issues 1099-NEC automatically

4. **Reporting**
   - Generate earnings summary on request
   - Show by time period (week, month, year)
   - Show by platform
   - Show by status (pending, paid)

5. **Alerts**
   - Alert when payment overdue (>7 days past merge)
   - Alert when approaching tax thresholds
   - Alert when milestone reached ($100, $500, $1000)

## Data Structure

Suggested format for memory/bounty_earnings.json:

```json
{
  "earnings": [
    {
      "id": "unique-id",
      "platform": "algora",
      "bounty_amount": 100.00,
      "currency": "USD",
      "issue_url": "https://github.com/...",
      "pr_url": "https://github.com/...",
      "claimed_date": "2026-03-04T17:00:00Z",
      "merged_date": null,
      "paid_date": null,
      "stripe_transaction_id": null,
      "status": "claimed",
      "notes": ""
    }
  ],
  "summary": {
    "total_earned": 0,
    "total_paid": 0,
    "total_pending": 0,
    "year_to_date": 0
  }
}
```

## Skill Structure

Create a SKILL.md file with:
- YAML frontmatter (name, description, metadata)
- When to use section
- Data structure documentation
- Logging commands
- Query commands
- Report generation
- Tax threshold alerts

## Output

Generate the complete SKILL.md file. Place in workspace/skills/payment-tracker/SKILL.md
```

---

## Prompt 3: Bounty Evaluator Skill (Optional Enhancement)

```
You are an expert at creating nanobot skills. Create a "bounty-evaluator" skill that analyzes bounty attractiveness before Pam commits time.

## Context

Pam needs to quickly evaluate whether a bounty is worth pursuing. This skill provides decision criteria and scoring.

## Requirements

The skill should enable Pam to:

1. **Complexity Assessment**
   - Analyze issue description
   - Estimate lines of code needed
   - Identify dependencies
   - Check if tests required
   - Score complexity (1-5)

2. **Competition Assessment**
   - Check for existing PRs
   - Count open PRs on issue
   - Check PR age and activity
   - Score competition (1-5, lower = better)

3. **Reward Assessment**
   - Get bounty amount
   - Calculate hourly rate estimate
   - Compare to minimum threshold
   - Score reward (1-5)

4. **Overall Score**
   - Weighted calculation
   - Complexity: 30%
   - Competition: 40%
   - Reward: 30%
   - Generate go/no-go recommendation

5. **Risk Factors**
   - Identify red flags (vague requirements, no maintainer response, old issue)
   - Flag potential issues

## Decision Matrix

| Score | Recommendation |
|-------|----------------|
| 8-10 | Strong yes - pursue immediately |
| 6-7 | Yes - good opportunity |
| 4-5 | Maybe - evaluate carefully |
| 2-3 | No - skip unless strategic value |
| 0-1 | Hard no - avoid |

## Output

Generate the complete SKILL.md file. Place in workspace/skills/bounty-evaluator/SKILL.md
```

---

## Security Reminder

After Claude Code generates each skill:

1. **Review the SKILL.md** — Read it before using
2. **Check for external calls** — Verify any API endpoints are legitimate
3. **No credential requests** — Skills should never ask for secrets
4. **Test in isolation** — Run with a test bounty before production use

---

## Integration Notes

These skills will integrate with Pam's existing capabilities:

| Skill | Depends On |
|-------|-----------|
| bounty-hunter | github (gh CLI), web_search, memory |
| payment-tracker | memory, bounty-hunter |
| bounty-evaluator | web_search, bounty-hunter |

Install order: bounty-hunter → payment-tracker → bounty-evaluator