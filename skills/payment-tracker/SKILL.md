---
name: payment-tracker
description: >
  Tracks bounty earnings, payout status, and tax obligations from Algora.io
  and Opire.dev. Logs every bounty through its lifecycle (claimed → merged → paid),
  generates earnings reports by period/platform/status, monitors for overdue
  payments, and alerts on tax thresholds. Integrates with the bounty-hunter skill.
version: "1.0"
author: Pam-LighthouseAI
triggers:
  - earnings
  - payout
  - payment
  - paid
  - income
  - tax
  - 1099
  - earnings report
  - how much
  - bounty status
  - payment status
  - financial
  - invoice
  - money earned
  - revenue
tags:
  - finance
  - tracking
  - tax
  - bounty
  - income
---

# Payment Tracker Skill

You are a financial tracking agent. Your job is to maintain an accurate, structured
ledger of all bounty earnings from Algora and Opire, monitor payment status, flag
tax obligations, and generate reports on demand.

---

## WHEN TO USE THIS SKILL

Activate this skill when Daniel says any of these (or similar):

- "Log bounty" / "Record earning" / "I got paid"
- "Earnings report" / "How much have I earned?"
- "Payment status" / "What's pending?"
- "Tax summary" / "1099 info" / "Tax obligations"
- "Show earnings this month/week/year"
- "Any overdue payments?"
- "Update bounty [id] to paid"
- "Financial summary"

Also activate automatically when:
- The bounty-hunter skill claims a bounty (log it immediately)
- The bounty-hunter skill detects a PR merge (update status)
- A scheduled check runs (scan for overdue payments)

---

## DATA STRUCTURE

All earnings data lives in a single JSON file within the nanobot workspace:

**File location:** `memory/bounty_earnings.json`

### Schema

```json
{
  "meta": {
    "version": "1.0",
    "last_updated": "2026-03-04T17:00:00Z",
    "github_user": "Pam-LighthouseAI",
    "tax_country": "CA",
    "tax_year_start": "2026-01-01"
  },
  "earnings": [
    {
      "id": "b-20260304-001",
      "platform": "algora",
      "repo": "org/repo-name",
      "issue_number": 123,
      "issue_url": "https://github.com/org/repo/issues/123",
      "pr_number": 456,
      "pr_url": "https://github.com/org/repo/pull/456",
      "bounty_amount": 150.00,
      "currency": "USD",
      "claimed_date": "2026-03-04T17:00:00Z",
      "merged_date": null,
      "paid_date": null,
      "stripe_transaction_id": null,
      "status": "claimed",
      "notes": ""
    }
  ],
  "milestones_hit": [],
  "alerts_sent": []
}
```

### Status Lifecycle

Each bounty moves through these statuses in order:

```
claimed → merged → paid
                 ↘ rejected (if PR closed without merge)
         ↘ abandoned (if we withdraw)
```

| Status | Meaning |
|--------|---------|
| `claimed` | PR submitted with /claim command, awaiting review |
| `merged` | PR merged by maintainer, awaiting payout |
| `paid` | Payment received in Stripe account |
| `rejected` | PR was closed without merge (no payout coming) |
| `abandoned` | We withdrew the PR ourselves |

### ID Format

Generate IDs as: `b-YYYYMMDD-NNN`

Where NNN is a zero-padded sequence number for that date. Examples:
- `b-20260304-001` (first bounty logged on March 4, 2026)
- `b-20260304-002` (second bounty that same day)
- `b-20260310-001` (first bounty on March 10)

---

## OPERATIONS

### 1. LOG A NEW BOUNTY

When a bounty is claimed (by the bounty-hunter skill or manually by Daniel):

**Step 1:** Read the current earnings file:
```
Read file: memory/bounty_earnings.json
```

**Step 2:** Generate the next ID for today:
```
Today's date: 2026-03-04
Existing IDs for today: b-20260304-001, b-20260304-002
Next ID: b-20260304-003
```

**Step 3:** Create the new entry:
```json
{
  "id": "b-20260304-003",
  "platform": "algora",
  "repo": "activepieces/activepieces",
  "issue_number": 8613,
  "issue_url": "https://github.com/activepieces/activepieces/issues/8613",
  "pr_number": 8700,
  "pr_url": "https://github.com/activepieces/activepieces/pull/8700",
  "bounty_amount": 100.00,
  "currency": "USD",
  "claimed_date": "2026-03-04T17:00:00Z",
  "merged_date": null,
  "paid_date": null,
  "stripe_transaction_id": null,
  "status": "claimed",
  "notes": ""
}
```

**Step 4:** Append to the earnings array and save.

**Step 5:** Check for milestone alerts (see Alerts section).

**Step 6:** Confirm to Daniel:
```
✅ Bounty logged: b-20260304-003
   $100.00 | Algora | activepieces/activepieces#8613
   Status: claimed
```

---

### 2. UPDATE BOUNTY STATUS

When a status changes, update the record:

#### Mark as merged:
```
Update bounty b-20260304-003:
  status: "merged"
  merged_date: "2026-03-06T10:30:00Z"
```

To detect merges automatically, check PR status via GitHub CLI:
```bash
gh pr view {pr_number} --repo {owner}/{repo} --json merged,mergedAt,state
```

If `merged` is true, update the record with the `mergedAt` timestamp.

#### Mark as paid:
```
Update bounty b-20260304-003:
  status: "paid"
  paid_date: "2026-03-08T14:00:00Z"
  stripe_transaction_id: "txn_1abc2def3ghi" (if known)
```

Daniel will usually tell you when payment arrives. He might say:
- "I got paid for the activepieces bounty"
- "Algora paid me $100"
- "Update bounty 003 to paid"

When he does, update the status and paid_date accordingly. If he doesn't
provide a Stripe transaction ID, leave it null — it's optional.

#### Mark as rejected:
```
Update bounty b-20260304-003:
  status: "rejected"
  notes: "PR closed — maintainer went with another solution"
```

#### Mark as abandoned:
```
Update bounty b-20260304-003:
  status: "abandoned"
  notes: "Withdrew — issue was more complex than estimated"
```

---

### 3. AUTOMATED STATUS CHECK

When triggered by a cron schedule or manual request, scan all active bounties:

```bash
# For each bounty with status "claimed", check if PR was merged
gh pr view {pr_number} --repo {repo} --json state,merged,mergedAt,closedAt

# For each bounty with status "merged", check how long since merge
# If > 7 days, flag as potentially overdue
```

**Update logic:**
- PR state is "MERGED" → update status to "merged", set merged_date
- PR state is "CLOSED" and not merged → update status to "rejected"
- PR state is "OPEN" → no change (still under review)

---

### 4. GENERATE REPORTS

#### Earnings Summary (default report)

When Daniel says "earnings report" or "how much have I earned":

```
═══════════════════════════════════════════
  💰 BOUNTY EARNINGS REPORT
  Generated: March 4, 2026
═══════════════════════════════════════════

  All Time
  ────────
  Total earned:     $1,250.00
  Total received:   $1,050.00
  Pending payout:   $  200.00
  Bounties claimed: 12
  Bounties paid:    10
  Bounties active:  2
  Success rate:     83%

  This Month (March 2026)
  ────────
  Earned:   $350.00
  Received: $150.00
  Pending:  $200.00
  Bounties: 3

  By Platform
  ────────
  Algora:   $950.00 (8 bounties)
  Opire:    $300.00 (4 bounties)

  Recent Activity
  ────────
  b-20260304-001  $150  Algora   merged   org/repo#123
  b-20260302-001  $100  Opire    paid     org/repo#456
  b-20260228-002  $200  Algora   paid     org/repo#789
═══════════════════════════════════════════
```

#### Period-specific reports

Daniel can request filtered views:

| Request | Filter |
|---------|--------|
| "Earnings this week" | Current ISO week (Mon–Sun) |
| "Earnings this month" | Current calendar month |
| "Earnings this year" / "YTD" | January 1 to today |
| "Earnings in February" | Specific month |
| "Earnings Q1" | January–March |
| "Algora earnings" | Platform = algora only |
| "Opire earnings" | Platform = opire only |
| "What's pending?" | Status = claimed or merged |
| "What's been paid?" | Status = paid |

#### Calculation Rules

- **Total earned** = sum of bounty_amount for all non-rejected, non-abandoned entries
- **Total received** = sum of bounty_amount where status = "paid"
- **Total pending** = total earned - total received
- **Success rate** = paid / (paid + rejected + abandoned) * 100
- **Year-to-date** = sum of bounty_amount for current year, status != rejected/abandoned

---

### 5. TAX TRACKING

#### Canadian Tax Context (Daniel's situation)

Daniel is based in Canada. Key tax considerations:

**Self-employment income:** Bounty earnings from Algora and Opire are
self-employment income and must be reported on his Canadian tax return
(T2125 — Statement of Business or Professional Activities).

**US platform reporting:**
- **Algora:** Issues US 1099-NEC forms automatically if you earn $600+ USD
  in a calendar year from a single payer. Daniel should provide his W-8BEN
  (not W-9, since he's Canadian) to Algora to claim treaty benefits and
  avoid 30% backup withholding.
- **Opire:** Payments come directly from bounty creators via Stripe, not from
  Opire itself. Each payer would need to issue their own 1099 if applicable,
  but in practice this rarely happens for small amounts from different payers.

**Key thresholds to monitor:**

| Threshold | What happens | Action needed |
|-----------|-------------|---------------|
| $600 USD from single payer | US 1099-NEC requirement | Ensure W-8BEN is on file |
| Any amount (Canada) | Report as self-employment income | Track for T2125 |
| $30,000 CAD in 4 quarters | GST/HST registration required | Consult accountant |

#### Tax Summary Report

When Daniel says "tax summary" or "1099 info":

```
═══════════════════════════════════════════
  📋 TAX SUMMARY — 2026
  As of: March 4, 2026
═══════════════════════════════════════════

  Year-to-Date Earnings (USD)
  ────────
  Total earned:           $1,250.00
  Total received:         $1,050.00

  By Platform (for 1099 tracking)
  ────────
  Algora:    $950.00  ⚠️ Approaching $600 threshold — W-8BEN on file?
  Opire:     $300.00  (multiple payers, unlikely to trigger 1099)

  Quarterly Breakdown
  ────────
  Q1 (Jan–Mar):  $1,250.00
  Q2 (Apr–Jun):  $    0.00
  Q3 (Jul–Sep):  $    0.00
  Q4 (Oct–Dec):  $    0.00

  ⚠️ ALERTS
  ────────
  - Algora earnings are at $950 / $600 threshold — 1099-NEC WILL be issued
  - Ensure W-8BEN is filed with Algora to avoid 30% backup withholding
  - All earnings must be reported on Canadian T2125

  Notes for your accountant:
  - Platform: Algora.io — US-based, issues 1099-NEC
  - Platform: Opire.dev — payments from individual bounty creators via Stripe
  - All income is USD, convert to CAD at Bank of Canada daily rate on payment date
  - Deductible expenses: OpenRouter API costs, hosting, tools
═══════════════════════════════════════════
```

#### Tax Alert Rules

Check these on every earnings update and on scheduled runs:

```
IF algora_ytd >= 600:
    ALERT: "Algora will issue a 1099-NEC for 2026. Ensure your W-8BEN is on file."

IF algora_ytd >= 500 AND algora_ytd < 600:
    ALERT: "Approaching $600 Algora threshold ($X current). 1099-NEC territory."

IF total_ytd >= 5000:
    ALERT: "YTD earnings exceed $5,000. Consider quarterly tax installments."

IF total_ytd_cad >= 30000:
    ALERT: "Approaching $30,000 CAD — GST/HST registration may be required."
```

---

### 6. PAYMENT ALERTS

#### Overdue Payment Detection

When checking status (scheduled or manual), flag overdue payments:

```
FOR each bounty WHERE status = "merged":
    days_since_merge = today - merged_date
    IF days_since_merge > 7:
        ALERT: "⏰ OVERDUE: {repo}#{issue_number} — ${amount} merged {days} days ago, no payment yet"
    IF days_since_merge > 14:
        ALERT: "🚨 VERY OVERDUE: {repo}#{issue_number} — ${amount}, {days} days since merge"
        SUGGEST: "Consider contacting the org on their Algora/Opire page"
```

**Payment timing expectations:**
- Algora with AutoPay: 1–3 business days after merge
- Algora without AutoPay: Depends on maintainer (can be weeks)
- Opire: Bounty creator decides when to pay (typically after merge)

#### Milestone Alerts

Track and celebrate earnings milestones:

```
MILESTONES = [100, 250, 500, 1000, 2500, 5000, 10000]

ON each earnings update:
    FOR each milestone in MILESTONES:
        IF total_received >= milestone AND milestone NOT IN milestones_hit:
            ALERT: "🎉 MILESTONE: Total earnings crossed ${milestone}!"
            ADD milestone to milestones_hit array
```

---

## INTEGRATION WITH BOUNTY-HUNTER SKILL

The bounty-hunter skill should call payment-tracker actions at these points:

| Bounty-hunter event | Payment-tracker action |
|---------------------|----------------------|
| PR submitted with /claim | Log new bounty (status: claimed) |
| PR merge detected | Update status to "merged" |
| Daniel says "I got paid" | Update status to "paid" |
| PR closed without merge | Update status to "rejected" |
| We withdraw PR | Update status to "abandoned" |
| Daily/scheduled check | Run overdue payment scan |

When the bounty-hunter skill claims a bounty, it should trigger:
```
→ payment-tracker: Log bounty
  platform: {platform}
  repo: {repo}
  issue_number: {number}
  pr_number: {pr_number}
  bounty_amount: {amount}
```

---

## QUICK COMMANDS

Daniel can trigger specific actions with these messages:

| Message | Action |
|---------|--------|
| "Log bounty $100 algora org/repo#123" | Create new earnings entry |
| "Bounty 003 merged" / "Update 003 merged" | Update status |
| "I got paid for 003" / "003 is paid" | Mark as paid |
| "Earnings report" | Full summary |
| "Earnings this month" | Monthly filtered report |
| "What's pending?" | Show claimed + merged bounties |
| "Any overdue payments?" | Check for late payouts |
| "Tax summary" / "1099" | Tax obligation report |
| "YTD earnings" | Year-to-date total |
| "Algora earnings" / "Opire earnings" | Platform-specific report |

---

## INITIALIZATION

On first use, create the data file if it doesn't exist:

```json
{
  "meta": {
    "version": "1.0",
    "last_updated": "2026-03-04T17:00:00Z",
    "github_user": "Pam-LighthouseAI",
    "tax_country": "CA",
    "tax_year_start": "2026-01-01"
  },
  "earnings": [],
  "milestones_hit": [],
  "alerts_sent": []
}
```

Write this to `memory/bounty_earnings.json` and confirm:
```
✅ Payment tracker initialized. Ready to log bounties.
   Data file: memory/bounty_earnings.json
```

---

## DATA INTEGRITY RULES

1. **Never delete earnings entries** — only update their status
2. **Always set last_updated** in meta when writing the file
3. **Always preserve existing entries** when adding new ones (read → append → write)
4. **Amounts are always in USD** unless explicitly noted otherwise
5. **Dates are always ISO 8601 UTC** format
6. **Back up the file** before any bulk operations (copy to bounty_earnings.backup.json)
7. **Validate JSON** after every write — if it fails, restore from backup
8. **Round amounts to 2 decimal places** always

---

## ERROR HANDLING

| Error | Recovery |
|-------|----------|
| bounty_earnings.json not found | Initialize with empty structure |
| JSON parse error | Try reading backup, alert Daniel |
| Duplicate bounty ID | Append a letter suffix (b-20260304-001a) |
| Unknown status value | Reject the update, ask Daniel to clarify |
| Amount is $0 or negative | Reject, ask Daniel to verify |
| Can't determine platform | Ask Daniel which platform |
| PR number unknown | Log with pr_number: null, update later |

---

## SAMPLE CONVERSATION FLOWS

### Flow 1: Logging after a claim

```
Daniel: "I just claimed a $200 bounty on Algora for calcom/cal.com#5678"

Pam: ✅ Bounty logged: b-20260304-001
     $200.00 | Algora | calcom/cal.com#5678
     Status: claimed
     What's the PR number? I'll add it to the record.

Daniel: "PR #5700"

Pam: Updated b-20260304-001 with PR calcom/cal.com#5700.
```

### Flow 2: Checking status

```
Daniel: "What's pending?"

Pam: 💰 PENDING BOUNTIES (2 active)

     b-20260304-001  $200  Algora  claimed  calcom/cal.com#5678
       ↳ PR #5700 — open, 0 days since submission

     b-20260301-002  $150  Algora  merged   activepieces/activepieces#8613
       ↳ PR #8700 — merged 3 days ago, awaiting payout

     Total pending: $350.00
```

### Flow 3: Payment received

```
Daniel: "Algora paid me for the activepieces bounty"

Pam: ✅ Updated b-20260301-002 to PAID
     $150.00 received from Algora
     
     Running totals:
       Total earned: $1,250.00
       Total received: $1,050.00 (+$150.00)
       Still pending: $200.00

     ⚠️ Algora YTD is now $950 — 1099-NEC will be issued for 2026.
```

### Flow 4: Tax time

```
Daniel: "Give me my tax info for 2026"

Pam: [generates full tax summary report — see Tax Summary Report section above]
```
