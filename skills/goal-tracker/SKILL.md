# Goal Tracker Skill

Decompose high-level goals into measurable sub-goals, track progress, measure outcomes, and automatically adjust strategy based on results.

## Usage

```python
from goal_tracker import GoalTracker, MetricDirection

tracker = GoalTracker()

# Create a goal
goal = tracker.create_goal(
    "Complete OCF Grant Application",
    deadline_days=14,
    priority=9
)

# Add metrics
goal.add_metric("sections_complete", MetricDirection.MAXIMIZE, target=8)
goal.add_metric("word_count", MetricDirection.TARGET, target=2500, unit="words")

# Record progress
tracker.update("sections_complete", 3)
tracker.update("word_count", 850)

# Get report
tracker.report()
```

## Key Features

- **Metrics**: Track progress toward targets (maximize, minimize, or target)
- **Strategies**: Test different approaches, track success rates
- **Milestones**: Mark important checkpoints
- **Sub-goals**: Break large goals into smaller pieces
- **Auto-adjust**: Get suggestions based on progress trends

## When to Use

- Grant applications with deadlines
- Project tracking
- Business goals (revenue, clients, etc.)
- Any measurable objective
