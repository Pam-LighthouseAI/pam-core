# Bounty Evaluator Skill - Prompt for Claude Code

*Copy this entire prompt and paste into Claude Code*

---

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