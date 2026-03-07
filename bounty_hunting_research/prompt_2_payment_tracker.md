# Payment Tracker Skill - Prompt for Claude Code

*Copy this entire prompt and paste into Claude Code*

---

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