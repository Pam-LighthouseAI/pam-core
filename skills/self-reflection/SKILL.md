# Self-Reflection Skill

Evaluate bot outputs and decisions before acting on them. Catches mistakes, scores confidence, and knows when to escalate vs. proceed autonomously.

## Usage

```python
from self_reflection import SelfReflectionEngine, Confidence

reflect = SelfReflectionEngine()

# Evaluate an output
result = reflect.evaluate(
    output={"action": "submit_grant", "org": "Ottawa Paw Pantry"},
    required_keys=["action", "org"],
    description="Grant submission decision"
)

result.report()

if result.should_escalate:
    # Ask Daniel before proceeding
    pass
elif result.verdict == "PASS":
    # Proceed confidently
    pass
```

## Key Features

- **Confidence scoring**: 0.0-1.0 with labels (CERTAIN, HIGH, MEDIUM, LOW, VERY_LOW)
- **Auto-escalation**: Flags when confidence < 0.55
- **Custom checks**: Add your own validation rules
- **Text evaluation**: Check for errors, forbidden phrases, length
- **Trade decisions**: Specialized for financial decisions
- **Contradiction detection**: Find conflicting statements

## When to Use

- Before taking important actions
- Validating outputs before showing to Daniel
- Checking for errors in generated content
- Deciding whether to escalate or proceed autonomously

## Confidence Levels

| Level | Range | Action |
|-------|-------|--------|
| CERTAIN | 0.90-1.00 | Proceed without verification |
| HIGH | 0.75-0.90 | Proceed, log for review |
| MEDIUM | 0.55-0.75 | Verify before acting |
| LOW | 0.35-0.55 | Seek more information |
| VERY_LOW | 0.00-0.35 | Escalate to human |
