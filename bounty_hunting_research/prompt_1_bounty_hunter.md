# Bounty Hunter Skill - Prompt for Claude Code

*Copy this entire prompt and paste into Claude Code*

---

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