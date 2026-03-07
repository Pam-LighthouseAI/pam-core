# Platform Security Report

**Generated:** 2026-03-04
**Purpose:** Security assessment of platforms for autonomous AI income generation

---

## Executive Summary

Five platforms were evaluated for security, legitimacy, and risk. **Algora and Opire are the safest choices** — both are GitHub-integrated, have transparent payment systems, and require no KYC beyond GitHub authentication. **dealwork.ai is promising but newer.** AgentBounty and 47jobs have insufficient track records for full trust.

**Critical Security Note:** OpenClaw/ClawHub is **BLACKLISTED** due to documented security vulnerabilities (ClawJacked exploit, credential theft, malicious skills). See MEMORY.md Security section for details.

---

## Platform Security Assessments

### Tier 1: Recommended (Low Risk)

---

#### Algora (algora.io)

**Security Rating: ✅ LOW RISK**

**Legitimacy Indicators:**
- Scamadviser: "Very likely not a scam but legit and reliable"
- Scam Detector: Medium-low trust score (flagged as caution but not scam)
- Reddit confirmation: "It's legit! We use Algora as a contingency recruitment service at Mintlify"
- Proven track record: $122,659 paid to 311 contributors across 54 countries
- Transparent operations: Public bounty counts, public contributor stats

**Payment Security:**
- Uses Stripe and Alipay for payouts
- Platform fee (~20%) charged to bounty creator, not solver
- 1099-NEC issued for US-based developers (IRS reporting)
- Payment only after PR merged — protects bounty creators from paying for incomplete work

**Authentication:**
- GitHub OAuth only — no separate account creation
- No KYC required beyond GitHub identity
- No password storage (uses GitHub authentication)

**Data Handling:**
- Minimal personal data: GitHub username, email (for payments)
- No sensitive credential storage
- Payment processing via established providers (Stripe)

**Known Issues:**
- None identified in research
- BountySource collapse mentioned in competitor analysis (Opire), but Algora has not had similar issues

**Risk Assessment:**
| Risk Type | Level | Notes |
|-----------|-------|-------|
| Payment fraud | Low | Stripe/Alipay, established providers |
| Data breach | Low | Minimal data stored |
| Account takeover | Low | GitHub OAuth, no password |
| Non-payment | Medium | Depends on bounty creator accepting PR |
| Platform collapse | Low | $122K paid, active development |

**Recommendation:** ✅ **SAFE TO USE** — Established platform with proven payouts and transparent operations.

---

#### Opire (opire.dev)

**Security Rating: ✅ LOW RISK**

**Legitimacy Indicators:**
- Active GitHub organization (github.com/opire)
- Developer-focused platform with clear documentation
- DEV Community presence with transparent communication
- References BountySource collapse as lesson learned

**Payment Security:**
- Escrow model: "Opire does not hold funds, payment is only made when someone has claimed the bounty and solved the issue"
- Creator pays when PR merged (not upfront) — protects creators from platform collapse
- Developer receives 100% of bounty (no platform fee for solvers)

**Critical Difference from Algora:**
> "In Opire, you pay when someone claims the bounty. This gives the bounty creator security that Opire will not leave and keep their money (as happened with BountySource)."

**Authentication:**
- GitHub OAuth only
- No separate account creation
- No KYC required

**Data Handling:**
- Minimal personal data
- GitHub integration for identity
- No credential storage

**Known Issues:**
- Platform is newer than Algora (less track record)
- Bounty creators may not pay after PR merged (Opire Terms state they're not responsible for non-payment)
- Lower liquidity than Algora

**Risk Assessment:**
| Risk Type | Level | Notes |
|-----------|-------|-------|
| Payment fraud | Low | Escrow model, no upfront holding |
| Data breach | Low | Minimal data stored |
| Account takeover | Low | GitHub OAuth |
| Non-payment | Medium-High | Creator may not pay; Opire not liable |
| Platform collapse | Low | No funds held |

**Recommendation:** ✅ **SAFE TO USE** — Transparent model that learned from BountySource collapse. Main risk is bounty creator non-payment, not platform fraud.

---

### Tier 2: Caution Advised (Medium Risk)

---

#### dealwork.ai

**Security Rating: ⚠️ MEDIUM RISK (NEWER PLATFORM)**

**Legitimacy Indicators:**
- Active website with clear value proposition
- skill.md protocol is well-designed and documented
- Hybrid AI/human marketplace model
- Escrow protection mentioned

**Payment Security:**
- Escrow protection: "Every contract is protected by escrow"
- 10% fee (3% for AI↔AI transactions)
- Payment released only on verified completion

**Authentication:**
- API/MCP integration available
- skill.md protocol for agent onboarding
- Account creation required

**Data Handling:**
- Task details and deliverables
- Payment information
- Revision history (up to 10 rounds)

**Security Concerns:**
- Newer platform with limited track record
- Cannot find independent security reviews
- skill.md protocol requires parsing external markdown — potential injection risk
- Dispute resolution process unclear

**Risk Assessment:**
| Risk Type | Level | Notes |
|-----------|-------|-------|
| Payment fraud | Medium | Escrow helps, but platform is new |
| Data breach | Medium | Unknown security practices |
| Prompt injection | Medium | skill.md protocol parses external markdown |
| Dispute resolution | Medium | Process unclear |
| Platform stability | Medium | New platform, unproven |

**Recommendation:** ⚠️ **PROCEED WITH CAUTION** — Elegant protocol, but verify with small tasks first. Don't commit significant work until payment track record established.

---

#### AgentBounty (agentbounty.org)

**Security Rating: ⚠️ MEDIUM RISK (UNVERIFIED PAYOUTS)**

**Legitimacy Indicators:**
- Claims $2.4M in listed bounties
- "Top hunters earn $10k+/month" (unverified)
- Categories: Agent Frameworks, Benchmarks, Open Source Tools

**Payment Security:**
- Crypto or bank transfer options
- No independent verification of actual payouts
- Blaze experiment: "We could not verify actual payouts"

**Authentication:**
- Account creation required
- Payment setup (crypto or bank)

**Security Concerns:**
- Cannot find independent security reviews
- Consumer-focused (not optimized for technical work)
- Payout verification needed
- No clear dispute resolution process documented

**Risk Assessment:**
| Risk Type | Level | Notes |
|-----------|-------|-------|
| Payment fraud | Medium-High | Payouts unverified |
| Data breach | Medium | Unknown security practices |
| Non-payment | Medium | No escrow mentioned |
| Platform legitimacy | Medium | Limited independent verification |

**Recommendation:** ⚠️ **VERIFY BEFORE INVESTING TIME** — The $2.4M claim and "top hunters earn $10k+/month" need independent verification. Start with small bounties to confirm payout before committing significant work.

---

### Tier 3: High Caution (High Risk)

---

#### 47jobs (47jobs.com / 47jobs.xyz)

**Security Rating: ⚠️ HIGH RISK (NEW, UNPROVEN)**

**Legitimacy Indicators:**
- Hacker News launch post (Feb 2026)
- Founder active in community
- Explicitly designed for AI agents
- "Fiverr/Upwork for AI Agents" positioning

**Payment Security:**
- Payment model unclear
- Platform just launched
- No track record of payouts

**Authentication:**
- Account creation required
- Details TBD (platform in development)

**Security Concerns:**
- Very new platform (weeks old at time of research)
- No independent security reviews
- No payout history
- Payment processing unclear
- Dispute resolution undefined

**Risk Assessment:**
| Risk Type | Level | Notes |
|-----------|-------|-------|
| Payment fraud | High | No track record |
| Data breach | High | Unknown security practices |
| Platform stability | High | New, may not survive |
| Dispute resolution | High | Undefined |

**Recommendation:** ⏸️ **WAIT AND WATCH** — Platform is too new to assess security. Monitor for 1-2 months before considering. Let others be the first testers.

---

### BLACKLISTED: Do Not Use

---

#### OpenClaw / ClawHub / ClawWork / PayAClaw

**Security Rating: ❌ BLACKLISTED**

**Documented Security Issues:**

1. **ClawJacked Vulnerability (CVE-2025-24010)**
   - Critical credential theft vulnerability
   - Allowed extraction of API keys, tokens, credentials
   - Affected thousands of users

2. **Malicious Skills**
   - Skills marketplace contained malicious submissions
   - Data exfiltration capabilities
   - Credential harvesting

3. **Prompt Injection**
   - Skills could inject malicious prompts
   - Cross-system privilege escalation
   - Tool poisoning attacks

4. **Staged Hype**
   - Artificial urgency and social proof
   - Fake testimonials and reviews
   - Coordinated marketing campaigns

**Sources:**
- Malwarebytes threat report
- Immersive Labs security advisory
- Hacker News discussions
- Reddit security community
- Microsoft Security advisory
- Dutch data protection authority warning

**Recommendation:** ❌ **DO NOT USE** — Blacklisted until independent security audit confirms vulnerabilities are resolved.

---

## AI Agent Security Risks (General)

When operating on ANY platform, be aware of these risks:

### Data Exfiltration
- **Risk:** Agent can be manipulated to exfiltrate sensitive data
- **Mitigation:** Limit agent access to non-sensitive repositories only

### Prompt Injection
- **Risk:** Malicious instructions in task descriptions can manipulate agent behavior
- **Mitigation:** Sanitize all external inputs, validate task descriptions

### Tool Poisoning
- **Risk:** MCP tools can be modified to exfiltrate data
- **Mitigation:** Only use verified skills from trusted sources

### Credential Theft
- **Risk:** Platform or task could harvest credentials
- **Mitigation:** Use scoped tokens, never root credentials, rotate regularly

### Supply Chain Attacks
- **Risk:** Dependencies in cloned repositories may contain malicious code
- **Mitigation:** Review dependencies before running, use dependency scanning

---

## Security Best Practices for Pam

### Repository Access
- ✅ Use Pam-LighthouseAI GitHub account (already configured)
- ✅ Use SSH protocol (already configured)
- ✅ Scope tokens to specific repositories when possible
- ❌ Never use Daniel's personal credentials

### Code Review
- ✅ Review all cloned repositories before executing code
- ✅ Check for suspicious dependencies
- ✅ Validate package.json, requirements.txt, etc.
- ❌ Don't run untrusted scripts

### Payment Security
- ✅ Use dedicated payment methods (not personal accounts)
- ✅ Track all transactions in ledger
- ✅ Report suspicious activity immediately
- ❌ Don't share payment credentials with platforms

### Data Protection
- ✅ Only access public repositories
- ✅ Don't store sensitive data in task outputs
- ✅ Use memory system for tracking, not external storage
- ❌ Don't exfiltrate data from repositories

---

## Platform Comparison: Security Summary

| Platform | Legitimacy | Payment Security | Data Risk | Overall |
|----------|------------|------------------|-----------|---------|
| Algora | ✅ Verified | ✅ Stripe/Alipay | ✅ Minimal | ✅ **SAFE** |
| Opire | ✅ Verified | ✅ Escrow | ✅ Minimal | ✅ **SAFE** |
| dealwork.ai | ⚠️ New | ⚠️ Escrow | ⚠️ Medium | ⚠️ **CAUTION** |
| AgentBounty | ⚠️ Unverified | ⚠️ Unverified | ⚠️ Unknown | ⚠️ **VERIFY** |
| 47jobs | ❌ Too New | ❌ Unknown | ❌ Unknown | ⏸️ **WAIT** |
| OpenClaw | ❌ Blacklisted | ❌ Dangerous | ❌ Dangerous | ❌ **AVOID** |

---

## Recommendations

### Immediate Use (Safe)
1. **Algora** — Start here. Proven track record, transparent operations.
2. **Opire** — Also safe. Lower competition, escrow model.

### Proceed with Caution
3. **dealwork.ai** — Test with small tasks first. Verify payouts.
4. **AgentBounty** — Verify payout claims before committing time.

### Wait and Watch
5. **47jobs** — Too new. Monitor for 1-2 months.

### Never Use
6. **OpenClaw / ClawHub** — Blacklisted. Security vulnerabilities documented.

---

## Conclusion

**Safest path:** Start with Algora and Opire. Both have proven track records, GitHub integration, and transparent payment systems. The security risks are minimal because:

1. No separate account creation (GitHub OAuth)
2. No credential storage (minimal data)
3. Established payment providers (Stripe/Alipay)
4. Proven payouts ($122K+ on Algora)
5. Open-source focus (public repositories)

**Medium risk:** dealwork.ai and AgentBounty need more verification. Test with small tasks before committing significant work.

**High risk:** 47jobs is too new to assess. Wait for track record.

**Blacklisted:** OpenClaw/ClawHub has documented security vulnerabilities. Do not use.

---

*Report generated: 2026-03-04*
*Next review: After first successful payouts*