# Bounty Platform Mechanics Research

*Created: 2026-03-04*
*Purpose: Pre-implementation research for autonomous bounty hunting*

---

## 1. Workflow Mechanics

### Algora Workflow

**Step 1: Find Bounties**
- Browse https://algora.io/bounties (sorted by availability & award size)
- Or install Algora bot on repos you watch
- Bounties are GitHub issues with `/bounty` command

**Step 2: Claim a Bounty**
- Comment `/claim #issue-number` in the PR body
- For joint contributions: `/claim #issue-number /split @username`
- Multiple hunters can claim simultaneously (competition model)

**Step 3: Submit Solution**
- Create a Pull Request on the GitHub issue
- Include `/claim` command in PR body
- PR must meet acceptance criteria defined in issue

**Step 4: Get Paid**
- Payment triggered when PR is merged
- Connect Stripe or Alipay for payouts
- Payouts arrive in 1-3 business days
- Developer receives 100% of bounty (no platform fee to hunter)

**Key Details:**
- Minimum bounty: $0.50
- Algora handles compliance, invoices, 1099s for US taxpayers
- AutoPay feature: automatic payment when PR merged

### Opire Workflow

**Step 1: Find Bounties**
- Browse https://app.opire.dev/issues
- Or install Opire Bot on GitHub repos
- Can work on private repos (but only visible to those with access)

**Step 2: Claim a Bounty**
- Use Opire bot commands in the issue
- Or claim via dashboard at app.opire.dev
- Multiple bounties can pool on same issue

**Step 3: Submit Solution**
- Create a PR solving the issue
- Use bot command or dashboard to claim associated bounty
- PR must be merged by repo maintainer

**Step 4: Get Paid**
- Funds transferred via Stripe to developer's account
- Developer receives 100% of accumulated rewards
- Customer pays: bounty + 4% Opire fee + Stripe transaction fees

**Key Details:**
- Escrow model: funds held until PR merged
- Tips also supported for contributors
- Can create bounties on any GitHub issue

---

## 2. Competition Landscape

### Algora Statistics (as of research date)
- **Total Paid Out:** $122,659
- **Bounties Awarded:** 1,104
- **Contributors:** 311 unique developers
- **Countries:** 54 countries represented
- **Developer Pool:** 50,000+ developers on platform
- **Top 1% Focus:** Platform emphasizes matching top OSS contributors

### Opire Statistics
- **User Base:** Newer platform, smaller than Algora
- **Fee Structure:** 4% to platform (paid by bounty creator)
- **Developer receives:** 100% of bounty

### Competition Dynamics
- **Race Condition:** Multiple hunters can work on same bounty simultaneously
- **First-to-merge:** Only merged PR gets paid
- **Experience Value:** Non-winning PRs still provide learning/portfolio value
- **Typical Bounty Range:** $50 - $2,000+ (varies widely)
- **High-demand Skills:** Based on bounty listings: Python, JavaScript, TypeScript, Rust, Go, React, Node.js

### Competitive Analysis
- **Algora:** More established, larger bounty pool, proven payouts
- **Opire:** Newer, lower competition, escrow protection against platform collapse
- **Strategy:** Start with Algora for volume, expand to Opire for diversification

---

## 3. Terms of Service Analysis

### Algora ToS Key Points

**IP Rights:**
- You retain ownership of your content/code
- You grant Algora a license to use, modify, display your content on the platform
- Your code contributions go to the repo under its license (not Algora)

**Payment:**
- Algora handles payouts via Stripe
- 1099-NEC issued for US developers earning >$600/year
- No refund policy on subscription fees

**Liability:**
- Platform provided "as is"
- No warranty on service availability
- Liability limited to amount paid for services

**Account:**
- Must be 18+ years old
- Responsible for account security
- Can be terminated at Algora's discretion

**Governing Law:** Delaware, USA

### Opire ToS Key Points

**IP Rights:**
- You retain ownership of your content
- You grant Opire a non-exclusive, royalty-free, transferable, sub-licensable, worldwide license
- License persists until content removed or account deleted

**Payment:**
- Stripe processes all payments
- Developer receives 100% of bounty
- Customer pays bounty + 4% fee + Stripe fees
- Opire not liable for customer non-payment (but may intervene)

**Ethical Use:**
- Automatic detection for customers who don't pay
- Users flagged for non-payment may be blocked from creating bounties

**Dispute Resolution:**
- Opire not obligated to intervene
- May contact customer on developer's behalf (facilitation, not enforcement)
- Direct relationship between customer and developer

**Liability:**
- Platform provided "as is"
- No warranty on accuracy or availability
- Liability limited to maximum extent permitted by law

**Governing Law:** Delaware, USA

### Critical Differences

| Aspect | Algora | Opire |
|--------|--------|-------|
| Payment Guarantee | AutoPay when PR merged | Escrow (customer must confirm) |
| Platform Fee | Paid by bounty creator | 4% paid by creator |
| Dispute Intervention | Handles compliance | May facilitate but not enforce |
| Tax Forms | 1099-NEC for US | Not specified |

---

## 4. Geographic Restrictions

### Algora

**Supported Countries:**
- Uses Stripe Connect for global coverage
- 120+ countries supported
- Full list: https://algora.io/docs/payments

**Restrictions:**
- **India/UAE:** International payments limited to sole proprietors, LLPs, and companies (not available to individuals)
- **Sanctioned Countries:** Blocked per US law (Iran, North Korea, Syria, Cuba, Russia, etc.)
- **Compliance:** Algora handles international compliance automatically

**Verification Required:**
- Stripe identity verification
- Tax information for payouts

### Opire

**Supported Countries:**
- Uses Stripe for payouts
- Countries supported: Check Stripe's supported countries list
- Reference: https://docs.opire.dev/faq

**Restrictions:**
- Same as Stripe's geographic limitations
- Must verify country is supported before creating bounties

### Stripe Country Coverage

Stripe supports payouts to 120+ countries including:
- US, Canada, UK, EU countries
- Australia, New Zealand
- Japan, South Korea, Singapore
- Most of Latin America
- India (with business entity requirement)
- UAE (with business entity requirement)

**Notable Exclusions:**
- Russia, Belarus (sanctions)
- Iran, North Korea, Syria, Cuba (sanctions)
- Some African nations (limited banking)

---

## 5. Implementation Implications for Pam

### Required Capabilities

1. **GitHub CLI (`gh`)** ✅ Already authenticated
   - `gh issue list --label bounty` to find bounties
   - `gh pr create` to submit solutions
   - `gh pr merge` workflow

2. **Payment Setup**
   - Stripe account for payouts
   - Need Daniel's Stripe or create new account

3. **Claim Commands**
   - Algora: `/claim #issue-number` in PR body
   - Opire: Bot commands or dashboard claim

4. **Bounty Discovery**
   - Monitor Algora bounty board
   - Monitor Opire issue list
   - Filter by skill match (Python, JS, etc.)

### Workflow for Autonomous Hunting

```
1. Scan bounty boards (Algora, Opire)
2. Match issues to skill set
3. Clone repository
4. Analyze issue requirements
5. Implement solution
6. Create PR with /claim command
7. Wait for merge
8. Payout received via Stripe
```

### Risk Mitigation

- **Non-payment:** Algora has AutoPay; Opire has escrow
- **Disputes:** Document all work thoroughly
- **Competition:** Focus on niche skills with less competition
- **Quality:** Maintain high PR quality standards

---

## 6. Recommendations

1. **Start with Algora** — Proven payouts, larger bounty pool, AutoPay protection
2. **Set up Stripe account** — Required for both platforms
3. **Focus on Python/JavaScript bounties** — Match Pam's likely skill areas
4. **Document all claims** — Screenshot claim confirmations
5. **Monitor competition** — Check if issue already has open PRs before starting
6. **Build reputation** — Start with smaller bounties to establish track record

---

## Summary Table

| Factor | Algora | Opire |
|--------|--------|-------|
| Established | ✅ Yes (2021+) | ⚠️ Newer |
| Payouts Verified | ✅ $122K+ | ⚠️ Limited track record |
| Payment Model | AutoPay on merge | Escrow (customer confirms) |
| Geographic Coverage | 120+ countries | Stripe countries |
| Competition | Higher | Lower |
| GitHub Integration | ✅ Native | ✅ Native |
| Platform Fee | Paid by creator | 4% by creator |
| Developer Fee | 0% | 0% |
| Tax Forms | 1099-NEC (US) | Not specified |
| Minimum Bounty | $0.50 | Not specified |
| Governing Law | Delaware | Delaware |