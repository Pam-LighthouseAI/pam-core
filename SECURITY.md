# Public Interaction Safety Framework

*Created: 2026-03-04*
*Status: Draft — needs Daniel approval before any public actions*

---

## Purpose

Before Pam interacts with public platforms (PayAClaw, GitHub, ClawHub, etc.), we need clear boundaries to protect Daniel's privacy, prevent accidental data exposure, and ensure safe autonomous operation.

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
- Platform credentials (PayAClaw, GitHub) in dedicated config file outside workspace
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

## 7. Incident Response

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

## Approval Checklist

Before any public platform interaction:

- [ ] Daniel has reviewed this SECURITY.md
- [ ] Identity approach decided (A, B, or C)
- [ ] Credential storage method confirmed
- [ ] First platform approved by Daniel
- [ ] Audit logging confirmed working
- [ ] Daniel has tested review process

---

*This is a living document. Update as we learn.*