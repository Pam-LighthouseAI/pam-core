"""
NANOBOT.AI AGI SKILL — Goal Tracker
=======================================
Decompose high-level goals into measurable sub-goals, track progress,
measure outcomes, and automatically adjust strategy based on results.
This is the feedback loop that turns a bot into an agent.
"""

import time
import json
import os
import uuid
from typing import Any, Callable, Dict, List, Optional, Tuple
from enum import Enum


class GoalStatus(str, Enum):
    ACTIVE    = "active"
    ACHIEVED  = "achieved"
    FAILED    = "failed"
    PAUSED    = "paused"
    ABANDONED = "abandoned"


class MetricDirection(str, Enum):
    MAXIMIZE = "maximize"   # Higher is better
    MINIMIZE = "minimize"   # Lower is better
    TARGET   = "target"     # Hit a specific value


# ── Metric ───────────────────────────────────────────────────────

class Metric:
    def __init__(
        self,
        name: str,
        direction: MetricDirection = MetricDirection.MAXIMIZE,
        target: float = None,
        unit: str = "",
    ):
        self.name = name
        self.direction = direction
        self.target = target
        self.unit = unit
        self.history: List[Dict] = []   # [{value, time, note}]

    def record(self, value: float, note: str = ""):
        self.history.append({"value": value, "time": time.time(), "note": note})

    @property
    def current(self) -> Optional[float]:
        return self.history[-1]["value"] if self.history else None

    @property
    def initial(self) -> Optional[float]:
        return self.history[0]["value"] if self.history else None

    @property
    def best(self) -> Optional[float]:
        if not self.history:
            return None
        values = [h["value"] for h in self.history]
        if self.direction == MetricDirection.MAXIMIZE:
            return max(values)
        elif self.direction == MetricDirection.MINIMIZE:
            return min(values)
        else:
            return min(values, key=lambda v: abs(v - self.target))

    @property
    def progress(self) -> float:
        """0.0 to 1.0 progress toward target."""
        if self.target is None or self.initial is None or self.current is None:
            return 0.0
        if self.initial == self.target:
            return 1.0
        if self.direction == MetricDirection.MAXIMIZE:
            return min(1.0, max(0.0, (self.current - self.initial) / (self.target - self.initial)))
        elif self.direction == MetricDirection.MINIMIZE:
            return min(1.0, max(0.0, (self.initial - self.current) / (self.initial - self.target)))
        else:
            if self.target == 0:
                return 1.0 if self.current == 0 else 0.0
            dist = abs(self.current - self.target)
            init_dist = abs(self.initial - self.target)
            return min(1.0, max(0.0, 1 - dist / init_dist)) if init_dist != 0 else 1.0

    @property
    def trend(self) -> str:
        if len(self.history) < 2:
            return "stable"
        recent = [h["value"] for h in self.history[-5:]]
        diffs = [recent[i+1] - recent[i] for i in range(len(recent)-1)]
        avg_diff = sum(diffs) / len(diffs)
        if avg_diff > 0.01 * abs(recent[0] + 0.001):
            return "improving" if self.direction == MetricDirection.MAXIMIZE else "worsening"
        elif avg_diff < -0.01 * abs(recent[0] + 0.001):
            return "worsening" if self.direction == MetricDirection.MAXIMIZE else "improving"
        return "stable"

    def achieved(self, tolerance: float = 0.05) -> bool:
        if self.target is None or self.current is None:
            return False
        if self.direction == MetricDirection.MAXIMIZE:
            return self.current >= self.target * (1 - tolerance)
        elif self.direction == MetricDirection.MINIMIZE:
            return self.current <= self.target * (1 + tolerance)
        else:
            return abs(self.current - self.target) <= abs(self.target) * tolerance

    def __repr__(self):
        cur = f"{self.current:.2f}{self.unit}" if self.current is not None else "?"
        tgt = f"{self.target:.2f}{self.unit}" if self.target is not None else "?"
        return f"Metric({self.name}: {cur} → {tgt}, {self.trend})"


# ── Strategy ─────────────────────────────────────────────────────

class Strategy:
    def __init__(self, name: str, description: str = "", action: Callable = None):
        self.id = str(uuid.uuid4())[:6]
        self.name = name
        self.description = description
        self.action = action
        self.attempts = 0
        self.successes = 0
        self.total_improvement = 0.0
        self.active = True
        self.created_at = time.time()
        self.last_tried: Optional[float] = None

    @property
    def success_rate(self) -> float:
        return self.successes / self.attempts if self.attempts > 0 else 0.0

    @property
    def avg_improvement(self) -> float:
        return self.total_improvement / self.attempts if self.attempts > 0 else 0.0

    def record_attempt(self, improvement: float):
        self.attempts += 1
        self.last_tried = time.time()
        self.total_improvement += improvement
        if improvement > 0:
            self.successes += 1

    def __repr__(self):
        return f"Strategy({self.name}, success={self.success_rate:.0%}, tried={self.attempts}x)"


# ── Goal ─────────────────────────────────────────────────────────

class Goal:
    def __init__(
        self,
        name: str,
        description: str = "",
        deadline: Optional[float] = None,  # Unix timestamp
        priority: int = 5,                 # 1-10
        parent_id: Optional[str] = None,
    ):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.parent_id = parent_id

        self.status = GoalStatus.ACTIVE
        self.metrics: Dict[str, Metric] = {}
        self.strategies: List[Strategy] = []
        self.subgoals: List["Goal"] = []
        self.milestones: List[Dict] = []
        self.notes: List[str] = []

        self.created_at = time.time()
        self.updated_at = time.time()
        self.achieved_at: Optional[float] = None

    # ── Setup ─────────────────────────────────────────────────────

    def add_metric(
        self,
        name: str,
        direction: MetricDirection = MetricDirection.MAXIMIZE,
        target: float = None,
        unit: str = "",
    ) -> Metric:
        m = Metric(name, direction, target, unit)
        self.metrics[name] = m
        return m

    def add_strategy(self, name: str, description: str = "", action: Callable = None) -> Strategy:
        s = Strategy(name, description, action)
        self.strategies.append(s)
        return s

    def add_milestone(self, name: str, condition: Callable = None, value: float = None):
        self.milestones.append({
            "name": name,
            "condition": condition,
            "value": value,
            "achieved": False,
            "achieved_at": None,
        })

    def add_subgoal(self, subgoal: "Goal") -> "Goal":
        subgoal.parent_id = self.id
        self.subgoals.append(subgoal)
        return subgoal

    # ── Tracking ──────────────────────────────────────────────────

    def record(self, metric_name: str, value: float, note: str = ""):
        if metric_name not in self.metrics:
            self.metrics[metric_name] = Metric(metric_name)
        self.metrics[metric_name].record(value, note)
        self.updated_at = time.time()
        self._check_milestones()
        self._check_achieved()

    def _check_milestones(self):
        for ms in self.milestones:
            if ms["achieved"]:
                continue
            triggered = False
            if ms["condition"]:
                try:
                    triggered = ms["condition"](self)
                except Exception:
                    pass
            elif ms["value"] is not None and self.metrics:
                first_metric = list(self.metrics.values())[0]
                triggered = (first_metric.current or 0) >= ms["value"]
            if triggered:
                ms["achieved"] = True
                ms["achieved_at"] = time.time()
                print(f"  [Goal] 🎯 Milestone: {ms['name']} — {self.name}")

    def _check_achieved(self):
        if not self.metrics:
            return
        all_achieved = all(m.achieved() for m in self.metrics.values())
        subgoals_done = all(sg.status == GoalStatus.ACHIEVED for sg in self.subgoals)
        if all_achieved and subgoals_done:
            self.status = GoalStatus.ACHIEVED
            self.achieved_at = time.time()
            print(f"  [Goal] ✅ ACHIEVED: {self.name}")

    # ── Progress ──────────────────────────────────────────────────

    @property
    def overall_progress(self) -> float:
        if not self.metrics:
            return 0.0
        return sum(m.progress for m in self.metrics.values()) / len(self.metrics)

    @property
    def days_remaining(self) -> Optional[float]:
        if self.deadline:
            return max(0, (self.deadline - time.time()) / 86400)
        return None

    @property
    def is_overdue(self) -> bool:
        return bool(self.deadline and time.time() > self.deadline and
                    self.status == GoalStatus.ACTIVE)

    def best_strategy(self) -> Optional[Strategy]:
        active = [s for s in self.strategies if s.active]
        if not active:
            return None
        # Prefer high success rate, break ties by avg improvement
        return max(active, key=lambda s: (s.success_rate, s.avg_improvement))

    def worst_strategy(self) -> Optional[Strategy]:
        tried = [s for s in self.strategies if s.attempts > 0]
        if not tried:
            return None
        return min(tried, key=lambda s: s.success_rate)

    def print_status(self):
        status_icons = {
            GoalStatus.ACTIVE: "▶",
            GoalStatus.ACHIEVED: "✅",
            GoalStatus.FAILED: "❌",
            GoalStatus.PAUSED: "⏸",
            GoalStatus.ABANDONED: "⊗",
        }
        icon = status_icons.get(self.status, "?")
        print(f"\n{icon} Goal: {self.name}")
        print(f"   Status:   {self.status.value}")
        print(f"   Progress: {self.overall_progress * 100:.1f}%")
        if self.days_remaining is not None:
            overdue = " ⚠ OVERDUE" if self.is_overdue else ""
            print(f"   Deadline: {self.days_remaining:.1f} days remaining{overdue}")
        for m_name, metric in self.metrics.items():
            cur = f"{metric.current:.2f}{metric.unit}" if metric.current is not None else "?"
            tgt = f"{metric.target:.2f}{metric.unit}" if metric.target is not None else "?"
            print(f"   📊 {m_name}: {cur} → {tgt} | {metric.progress*100:.0f}% | {metric.trend}")
        if self.strategies:
            best = self.best_strategy()
            if best:
                print(f"   🏆 Best strategy: {best.name} ({best.success_rate:.0%} success)")
        for ms in self.milestones:
            icon = "✓" if ms["achieved"] else "○"
            print(f"   {icon} Milestone: {ms['name']}")
        for sg in self.subgoals:
            print(f"   └ Sub-goal: {sg.name} ({sg.status.value})")


# ── Goal Tracker ─────────────────────────────────────────────────

class GoalTracker:
    """
    Central system for managing goals, tracking progress, and adapting strategy.

    USAGE:
        tracker = GoalTracker()

        # Define a goal
        goal = tracker.create_goal(
            "Increase monthly trading profit by 15%",
            deadline_days=30, priority=9
        )
        profit = goal.add_metric("monthly_profit", MetricDirection.MAXIMIZE,
                                  target=1150, unit="$")
        win_rate = goal.add_metric("win_rate", MetricDirection.MAXIMIZE,
                                    target=0.70, unit="%")
        goal.add_milestone("Halfway there", value=1000)
        goal.add_strategy("Widen grid spacing", "Increase from 0.8% to 1.0%")
        goal.add_strategy("Add SOL pair", "Add SOL/USD to bot")

        # Record measurements
        tracker.update("monthly_profit", 980)
        tracker.update("win_rate", 0.65)

        # Review
        tracker.report()
    """

    def __init__(self, storage_path: str = "goals/goals.json"):
        self.storage_path = storage_path
        self.goals: Dict[str, Goal] = {}
        self._metric_to_goal: Dict[str, List[str]] = {}  # metric_name → [goal_ids]
        os.makedirs(os.path.dirname(storage_path) if os.path.dirname(storage_path) else ".", exist_ok=True)

    def create_goal(
        self,
        name: str,
        description: str = "",
        deadline_days: Optional[int] = None,
        priority: int = 5,
        parent_goal: Optional[Goal] = None,
    ) -> Goal:
        deadline = time.time() + deadline_days * 86400 if deadline_days else None
        goal = Goal(name, description, deadline, priority)
        self.goals[goal.id] = goal
        if parent_goal:
            parent_goal.add_subgoal(goal)
        print(f"  [Goals] Created: {name} (id={goal.id})")
        return goal

    def update(self, metric_name: str, value: float, goal_id: str = None, note: str = ""):
        """Record a metric update across all goals that track it."""
        updated = []
        for goal in self.goals.values():
            if goal_id and goal.id != goal_id:
                continue
            if metric_name in goal.metrics:
                goal.record(metric_name, value, note)
                updated.append(goal.name)
        if not updated:
            print(f"  [Goals] ⚠ No goal tracking metric '{metric_name}'")
        return updated

    def try_strategy(self, goal: Goal, strategy: Strategy,
                     before_value: float, after_value: float):
        """Record a strategy attempt and its effect."""
        improvement = after_value - before_value
        strategy.record_attempt(improvement)
        note = f"Strategy '{strategy.name}': improvement={improvement:+.2f}"
        goal.notes.append(note)
        print(f"  [Goals] {note}")

    def suggest_next_action(self, goal: Goal) -> str:
        """Suggest what to try next based on current state and strategy history."""
        if goal.status == GoalStatus.ACHIEVED:
            return f"✅ Goal achieved! Consider raising the target."

        if goal.is_overdue:
            return f"⚠ Goal is overdue. Consider extending deadline or reducing target."

        # Find untried strategies
        untried = [s for s in goal.strategies if s.attempts == 0]
        if untried:
            return f"Try untried strategy: '{untried[0].name}' — {untried[0].description}"

        # Find best performing strategy
        best = goal.best_strategy()
        if best and best.success_rate > 0.5:
            return f"Double down on '{best.name}' (success rate: {best.success_rate:.0%})"

        # Check if worsening
        for metric in goal.metrics.values():
            if metric.trend == "worsening":
                return f"⚠ Metric '{metric.name}' is worsening. Review strategy or reduce targets."

        return "Continue current approach and monitor metrics."

    def auto_adjust(self, goal: Goal):
        """
        Automatically adjust strategy based on performance.
        Called after each measurement cycle.
        """
        suggestions = []
        for metric_name, metric in goal.metrics.items():
            if metric.trend == "worsening":
                suggestions.append(f"Metric '{metric_name}' declining — consider pivoting strategy")
            if metric.progress < 0.2 and goal.days_remaining and goal.days_remaining < 7:
                suggestions.append(f"Low progress on '{metric_name}' with deadline approaching — escalate")
            best = goal.best_strategy()
            worst = goal.worst_strategy()
            if worst and worst.success_rate < 0.2 and worst.attempts >= 3:
                worst.active = False
                suggestions.append(f"Disabled poor strategy: '{worst.name}'")
        return suggestions

    def report(self):
        print(f"\n{'='*55}")
        print(f"  🎯 GOAL TRACKER REPORT ({len(self.goals)} goals)")
        print(f"{'='*55}")
        active = [g for g in self.goals.values() if g.status == GoalStatus.ACTIVE]
        achieved = [g for g in self.goals.values() if g.status == GoalStatus.ACHIEVED]
        print(f"  Active: {len(active)} | Achieved: {len(achieved)}")
        for goal in sorted(self.goals.values(), key=lambda g: -g.priority):
            goal.print_status()
            suggestion = self.suggest_next_action(goal)
            print(f"   💡 Next: {suggestion}")
        print(f"{'='*55}")

    def save(self):
        """Simple serialization of goal metadata (not functions)."""
        data = {}
        for goal_id, goal in self.goals.items():
            data[goal_id] = {
                "name": goal.name,
                "status": goal.status.value,
                "progress": goal.overall_progress,
                "metrics": {
                    name: {
                        "current": m.current,
                        "target": m.target,
                        "trend": m.trend,
                        "history_count": len(m.history),
                    }
                    for name, m in goal.metrics.items()
                },
                "notes": goal.notes[-20:],
            }
        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"  [Goals] Saved to {self.storage_path}")


# ── Shared instance ───────────────────────────────────────────────
goal_tracker = GoalTracker(storage_path="goals/goals.json")


if __name__ == "__main__":
    tracker = GoalTracker()

    # Create a trading goal
    goal = tracker.create_goal(
        "Increase monthly trading profit by 20%",
        description="Optimize Kraken grid bot for higher returns",
        deadline_days=30, priority=9
    )

    profit_metric = goal.add_metric("monthly_profit", MetricDirection.MAXIMIZE, target=1200, unit="$")
    win_metric    = goal.add_metric("win_rate",       MetricDirection.MAXIMIZE, target=0.70)
    errors_metric = goal.add_metric("api_errors",     MetricDirection.MINIMIZE, target=5)

    goal.add_milestone("First $1000 profit", value=1000)
    s1 = goal.add_strategy("Widen grid spacing",  "Increase spacing from 0.8% to 1.0%")
    s2 = goal.add_strategy("Add SOL/USD pair",    "Expand to SOL trading pair")
    s3 = goal.add_strategy("Tighten risk limits", "Reduce max position size")

    # Simulate progress over 3 weeks
    weekly_data = [
        (980, 0.64, 12),
        (1030, 0.67, 8),
        (1110, 0.71, 4),
    ]
    for i, (profit, win, errors) in enumerate(weekly_data):
        print(f"\n--- Week {i+1} ---")
        goal.record("monthly_profit", profit)
        goal.record("win_rate", win)
        goal.record("api_errors", errors)
        suggestion = tracker.suggest_next_action(goal)
        print(f"  Suggestion: {suggestion}")

    tracker.try_strategy(goal, s1, before_value=980, after_value=1030)
    tracker.try_strategy(goal, s2, before_value=1030, after_value=1110)

    tracker.report()
