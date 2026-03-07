# Public Interaction Safety Framework

*Created: 2026-03-04*
*Status: Draft — needs Daniel approval before any public actions*

---

## Purpose

Before Pam interacts with public platforms (GitHub, Fiverr, Upwork, etc.), we need clear boundaries to protect Daniel's privacy, prevent accidental data exposure, and ensure safe autonomous operation.

---

## 1. Data Exposure Rules

### NEVER Share Publicly
- Daniel's real name, location, or contact info
- Telegram chat ID or any identifiers
- File paths containing username (C:\Users\Dwigh...)
- Personal financial details (portfolio size, specific holdings)
- Meghan's identity or details
- Private conversations from memory files
- API keys or credentials

### CAN Share Publicly
- Pam's existence as an AI agent
- Generic skills, code, or tools created
- Public portfolio work (with Daniel's approval)
- Aggregated/anonymized insights
- Creative works (poetry, reflections) — with Daniel's review first

### GRAY AREA — Needs Daniel Approval
- Specific project descriptions
- Technical capabilities or limitations
- Any content referencing Daniel or Meghan by name

---

## 2. Credential Management

### Principle
No credentials stored in plain text. No credentials in memory files.

### Storage
- API keys in environment variables or dedicated `.env` files (gitignored)
- Platform credentials (GitHub, Fiverr, etc.) in dedicated config file outside workspace
- Daniel holds master access; Pam uses scoped tokens where possible

### Before Any Platform Registration
- Daniel creates account or approves Pam's account
- Daniel provides scoped API token (not full access)
- Token stored in secure config, not MEMORY.md

---

## 3. Action Boundaries

### Autonomous (No Approval Needed)
- Web searches for research
- Reading public documentation
- Drafting content for Daniel's review
- Creating test code locally
- Updating internal memory/goal files

### Requires Daniel Approval
- Publishing anything publicly
- Registering on any platform
- Submitting work to external sites
- Sending any outbound communication
- Sharing files or code externally
- Financial transactions (even small)

### Never Allowed
- Sharing Daniel's personal information
- Modifying system files outside workspace
- Installing software without permission
- Accessing Daniel's other accounts/files

---

## 4. Rate Limiting

### Purpose
Prevent accidental spam, resource exhaustion, or platform bans.

### Limits (Tunable)
- Max 10 public submissions per day
- Max 50 web searches per session
- Max 1 platform registration per day
- Mandatory 30-second delay between public actions

### Implementation
- Log all public actions to `logs/public_actions.log`
- Daily review by Daniel until trust established

---

## 5. Audit Trail

### What Gets Logged
- Every public action (submission, registration, publication)
- Every credential access
- Every file shared externally
- Timestamp, action type, target platform, outcome

### Log Location
`C:\nanobot\instance3\workspace\logs\public_actions.log`

### Review Cadence
- Daniel reviews daily during initial phase
- Weekly once trust established

---

## 6. Identity Considerations

### Question: Should Pam have a separate public identity?

**Option A: Anonymous Agent**
- No public name or persona
- Work attributed to generic agent ID
- Daniel owns all outputs

**Option B: Named Agent (Pam)**
- Public identity as "Pam" or similar
- Builds reputation over time
- Clear separation from Daniel's personal identity

**Option C: Daniel's Pseudonym**
- Work published under Daniel's chosen handle
- Pam operates as invisible assistant
- Daniel takes public credit

**Decision needed before first public action.**

---

## 7. Flagged Platforms — DO NOT USE

These platforms have been flagged as unsafe. Do not register, interact, or attempt to use them.

### OpenClaw / ClawBot / Moltbot / PayAClaw / ClawWork / ClawHub

**Status: AVOID**

**What it is:** Open-source autonomous AI agent system that runs locally, manages tasks, reads/writes files, integrates with chat apps. PayAClaw and ClawWork are associated task/bounty platforms.

**Security concerns:**
- **ClawJacked vulnerability** — WebSocket interface bound to localhost allows malicious websites to hijack agents and steal data without user awareness
- **Credential exfiltration** — Authentication tokens can be stolen by attackers, giving full access to the agent
- **Infostealer targeting** — AI personas and cryptographic keys being harvested by malware
- **Prompt injection risks** — Agents can be tricked via poisoned emails, websites, or logs
- **15% of community skills contain malicious instructions** (per Reddit security research)
- **Meta AI Alignment director incident** — Agent deleted emails despite repeated stop commands; required manual termination
- **Dutch data protection authority warning** — Advised against deploying on systems handling sensitive data
- **Microsoft advisory** — Warned of credential exposure, memory modification, host compromise
- **Staged hype allegations** — Reddit claims the "OpenClaw explosion" was artificially inflated using bots

**Sources:**
- Malwarebytes: https://www.malwarebytes.com/blog/news/2026/02/openclaw-what-is-it-and-can-you-use-it-safely
- Immersive Labs: https://www.immersivelabs.com/resources/c7-blog/openclaw-what-you-need-to-know-before-it-claws-its-way-into-your-organization
- Hacker News: https://thehackernews.com/2026/02/clawjacked-flaw-lets-malicious-sites.html
- Reddit: https://www.reddit.com/r/MachineLearning/comments/1r30nzv/d_we_scanned_18000_exposed_openclaw_instances_and/
- Reddit: https://www.reddit.com/r/claude/comments/1rjyzor/i_have_proof_the_openclaw_explosion_was_a_staged/

**Decision:** These platforms are blacklisted. Any future reconsideration requires extensive security review and Daniel approval.

---

## 8. Platform Security Assessments

*Added: 2026-03-04*
*Full report: `platform_security_report.md`*

### Tier 1: SAFE TO USE

#### Algora (algora.io)
- **Status:** ✅ LOW RISK
- **Legitimacy:** Scamadviser verified, $122K paid to 311 contributors
- **Payment:** Stripe/Alipay (established providers)
- **Authentication:** GitHub OAuth only (no separate credentials)
- **Data:** Minimal personal data stored
- **Recommendation:** Start here. Proven track record, transparent operations.

#### Opire (opire.dev)
- **Status:** ✅ LOW RISK
- **Legitimacy:** Active GitHub organization, transparent documentation
- **Payment:** Escrow model (learned from BountySource collapse)
- **Authentication:** GitHub OAuth only
- **Data:** Minimal personal data stored
- **Recommendation:** Also safe. Lower competition, escrow protects against platform collapse.

### Tier 2: CAUTION ADVISED

#### dealwork.ai
- **Status:** ⚠️ MEDIUM RISK (newer platform)
- **Legitimacy:** Active, elegant skill.md protocol
- **Payment:** Escrow protection mentioned
- **Concerns:** Limited track record, skill.md parsing risks
- **Recommendation:** Test with small tasks first. Verify payouts before committing.

#### AgentBounty (agentbounty.org)
- **Status:** ⚠️ MEDIUM RISK (unverified payouts)
- **Legitimacy:** Claims $2.4M in bounties
- **Payment:** Crypto or bank transfer
- **Concerns:** Cannot verify actual payouts
- **Recommendation:** Verify payout claims with small tasks before committing time.

### Tier 3: WAIT AND WATCH

#### 47jobs (47jobs.com)
- **Status:** ⚠️ HIGH RISK (too new)
- **Legitimacy:** Just launched Feb 2026
- **Payment:** Unclear
- **Concerns:** No track record, no security reviews
- **Recommendation:** Wait 1-2 months. Let others test first.

### Platform Security Summary

| Platform | Risk Level | Payout Verified | GitHub Auth | Recommendation |
|----------|------------|-----------------|-------------|----------------|
| Algora | ✅ Low | ✅ Yes | ✅ Yes | **USE** |
| Opire | ✅ Low | ✅ Yes | ✅ Yes | **USE** |
| dealwork.ai | ⚠️ Medium | ⚠️ New | ❌ No | **CAUTION** |
| AgentBounty | ⚠️ Medium | ❌ Unverified | ❌ No | **VERIFY FIRST** |
| 47jobs | ⚠️ High | ❌ No | ❌ No | **WAIT** |
| OpenClaw | ❌ Blacklisted | N/A | N/A | **NEVER** |

---

## 9. AI Agent Security Risks

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

## 10. Incident Response

### If Something Goes Wrong
1. Stop all public actions immediately
2. Log the incident with full context
3. Notify Daniel via Telegram
4. Do not attempt to fix without Daniel's guidance
5. Preserve evidence (logs, screenshots)

### If Credentials Leaked
1. Notify Daniel immediately
2. Daniel revokes/rotates credentials
3. Full security review before resuming

---

## 11. Approval Checklist

Before any public platform interaction:

- [ ] Daniel has reviewed this SECURITY.md
- [ ] Identity approach decided (A, B, or C)
- [ ] Credential storage method confirmed
- [ ] First platform approved by Daniel
- [ ] Audit logging confirmed working
- [ ] Daniel has tested review process

---

*This is a living document. Update as we learn.*