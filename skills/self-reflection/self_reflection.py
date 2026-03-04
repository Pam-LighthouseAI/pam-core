"""
NANOBOT.AI AGI SKILL — Self-Reflection Engine
===============================================
The bot evaluates its own outputs, scores confidence, catches mistakes,
and knows when to escalate vs. proceed autonomously.

No LLM required — uses rule-based + statistical heuristics.
"""

import re
import math
import time
from typing import Any, Callable, Dict, List, Optional, Tuple


# ── Confidence Levels ─────────────────────────────────────────────

class Confidence:
    CERTAIN   = (0.90, 1.00)  # Proceed without verification
    HIGH      = (0.75, 0.90)  # Proceed, log for review
    MEDIUM    = (0.55, 0.75)  # Verify before acting
    LOW       = (0.35, 0.55)  # Seek more information
    VERY_LOW  = (0.00, 0.35)  # Escalate to human

    @staticmethod
    def label(score: float) -> str:
        if score >= 0.90:   return "CERTAIN"
        if score >= 0.75:   return "HIGH"
        if score >= 0.55:   return "MEDIUM"
        if score >= 0.35:   return "LOW"
        return "VERY_LOW"

    @staticmethod
    def should_escalate(score: float) -> bool:
        return score < 0.55

    @staticmethod
    def should_verify(score: float) -> bool:
        return score < 0.75


# ── Reflection Result ─────────────────────────────────────────────

class ReflectionResult:
    def __init__(self):
        self.confidence_score: float = 0.5
        self.quality_score: float = 0.5
        self.issues: List[str] = []
        self.warnings: List[str] = []
        self.suggestions: List[str] = []
        self.passed_checks: List[str] = []
        self.should_escalate: bool = False
        self.should_retry: bool = False
        self.verdict: str = "UNKNOWN"    # PASS, WARN, FAIL, ESCALATE
        self.metadata: Dict = {}

    @property
    def overall_score(self) -> float:
        return (self.confidence_score + self.quality_score) / 2

    def add_issue(self, issue: str, severity: str = "error"):
        self.issues.append(f"[{severity.upper()}] {issue}")
        if severity in ("error", "critical"):
            self.confidence_score *= 0.7
            self.quality_score -= 0.15

    def add_warning(self, warning: str):
        self.warnings.append(warning)
        self.confidence_score *= 0.9
        self.quality_score -= 0.05

    def add_check_passed(self, check: str):
        self.passed_checks.append(check)
        self.confidence_score = min(1.0, self.confidence_score + 0.03)

    def finalize(self):
        self.confidence_score = max(0.0, min(1.0, self.confidence_score))
        self.quality_score    = max(0.0, min(1.0, self.quality_score))
        self.should_escalate  = Confidence.should_escalate(self.confidence_score)
        self.should_retry     = len(self.issues) > 0 and not self.should_escalate

        if self.issues:
            self.verdict = "ESCALATE" if self.should_escalate else "FAIL"
        elif self.warnings:
            self.verdict = "WARN"
        else:
            self.verdict = "PASS"

    def report(self, verbose: bool = True):
        icons = {"PASS": "✅", "WARN": "⚠️", "FAIL": "❌", "ESCALATE": "🚨"}
        print(f"\n{'='*50}")
        print(f"  {icons.get(self.verdict, '?')} REFLECTION: {self.verdict}")
        print(f"  Confidence : {self.confidence_score:.2f} ({Confidence.label(self.confidence_score)})")
        print(f"  Quality    : {self.quality_score:.2f}")
        print(f"  Overall    : {self.overall_score:.2f}")
        if verbose:
            if self.passed_checks:
                print(f"\n  ✓ Passed ({len(self.passed_checks)}):")
                for c in self.passed_checks[:5]:
                    print(f"    • {c}")
            if self.warnings:
                print(f"\n  ⚠ Warnings ({len(self.warnings)}):")
                for w in self.warnings:
                    print(f"    • {w}")
            if self.issues:
                print(f"\n  ✗ Issues ({len(self.issues)}):")
                for i in self.issues:
                    print(f"    • {i}")
            if self.suggestions:
                print(f"\n  💡 Suggestions:")
                for s in self.suggestions:
                    print(f"    • {s}")
        print(f"{'='*50}")


# ── Checkers ─────────────────────────────────────────────────────

class OutputChecker:
    """Individual check that can be applied to outputs."""

    def __init__(self, name: str, check_fn: Callable, weight: float = 1.0, critical: bool = False):
        self.name = name
        self.check_fn = check_fn
        self.weight = weight
        self.critical = critical

    def run(self, output: Any, context: Dict = None) -> Tuple[bool, str]:
        """Returns (passed, message)."""
        try:
            result = self.check_fn(output, context or {})
            if isinstance(result, tuple):
                return result
            return (bool(result), "OK" if result else "Check failed")
        except Exception as e:
            return (False, f"Check error: {e}")


# ── Self-Reflection Engine ────────────────────────────────────────

class SelfReflectionEngine:
    """
    Evaluate bot outputs and decisions before acting on them.

    USAGE:
        reflect = SelfReflectionEngine()

        # Add domain-specific checks
        reflect.add_check("positive_profit",
            lambda output, ctx: output.get("profit", 0) > 0,
            critical=False)

        # Reflect on a trading decision
        result = reflect.evaluate(
            output={"action": "BUY", "pair": "DOGE/USD", "amount": 500, "profit": 12.5},
            context={"balance": 200, "max_trade": 100},
            description="Grid bot buy order decision"
        )
        result.report()

        if result.should_escalate:
            alert_human(result)
        elif result.verdict == "PASS":
            execute_action()
    """

    def __init__(self):
        self._checks: List[OutputChecker] = []
        self._history: List[Dict] = []
        self._load_default_checks()

    # ── Check Management ──────────────────────────────────────────

    def add_check(
        self,
        name: str,
        check_fn: Callable,
        weight: float = 1.0,
        critical: bool = False,
    ):
        """
        Add a custom check.
        check_fn(output, context) → bool or (bool, message)
        """
        self._checks.append(OutputChecker(name, check_fn, weight, critical))

    def remove_check(self, name: str):
        self._checks = [c for c in self._checks if c.name != name]

    # ── Evaluation ────────────────────────────────────────────────

    def evaluate(
        self,
        output: Any,
        context: Dict = None,
        description: str = "",
        expected_type: type = None,
        required_keys: List[str] = None,
        value_ranges: Dict[str, Tuple[float, float]] = None,
    ) -> ReflectionResult:
        """
        Run all checks against an output and return a ReflectionResult.

        Args:
            output: The bot's output to evaluate
            context: The context in which the output was generated
            expected_type: If set, checks output is this type
            required_keys: If output is dict, checks these keys exist
            value_ranges: {key: (min, max)} — validates numeric ranges
        """
        r = ReflectionResult()
        r.confidence_score = 0.5
        r.quality_score = 0.7
        ctx = context or {}

        print(f"  [Reflect] Evaluating: {description or type(output).__name__}")

        # ── Built-in checks ───────────────────────────────────────

        # Type check
        if expected_type is not None:
            if isinstance(output, expected_type):
                r.add_check_passed(f"Type is {expected_type.__name__}")
            else:
                r.add_issue(f"Expected {expected_type.__name__}, got {type(output).__name__}", "error")

        # Null / empty check
        if output is None:
            r.add_issue("Output is None", "critical")
        elif output == "" or output == [] or output == {}:
            r.add_issue("Output is empty", "error")
        else:
            r.add_check_passed("Output is not empty")

        # Required keys
        if required_keys and isinstance(output, dict):
            missing = [k for k in required_keys if k not in output]
            if missing:
                r.add_issue(f"Missing required keys: {missing}", "error")
            else:
                r.add_check_passed(f"All required keys present: {required_keys}")

        # Value ranges
        if value_ranges and isinstance(output, dict):
            for key, (min_val, max_val) in value_ranges.items():
                val = output.get(key)
                if val is not None:
                    try:
                        fval = float(val)
                        if min_val <= fval <= max_val:
                            r.add_check_passed(f"{key}={fval:.2f} in range [{min_val}, {max_val}]")
                        else:
                            r.add_issue(f"{key}={fval:.2f} out of range [{min_val}, {max_val}]", "error")
                    except (TypeError, ValueError):
                        r.add_warning(f"Could not validate range for {key}: {val}")

        # ── Custom checks ─────────────────────────────────────────
        for checker in self._checks:
            passed, msg = checker.run(output, ctx)
            if passed:
                r.add_check_passed(f"{checker.name}: {msg}")
            else:
                if checker.critical:
                    r.add_issue(f"{checker.name}: {msg}", "critical")
                else:
                    r.add_issue(f"{checker.name}: {msg}", "error")

        r.finalize()

        self._history.append({
            "time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "description": description,
            "verdict": r.verdict,
            "confidence": r.confidence_score,
            "quality": r.quality_score,
            "issues": len(r.issues),
        })

        return r

    # ── Specialized evaluators ────────────────────────────────────

    def evaluate_text(self, text: str, min_length: int = 1, max_length: int = None,
                      forbidden_phrases: List[str] = None, required_phrases: List[str] = None,
                      description: str = "text output") -> ReflectionResult:
        """Evaluate a text output."""
        r = self.evaluate(text, description=description, expected_type=str)

        if isinstance(text, str):
            if len(text) < min_length:
                r.add_issue(f"Text too short: {len(text)} < {min_length}")
            else:
                r.add_check_passed(f"Length OK: {len(text)} chars")

            if max_length and len(text) > max_length:
                r.add_warning(f"Text very long: {len(text)} > {max_length}")

            # Check for error indicators
            error_patterns = [r"error:", r"exception:", r"traceback", r"null", r"undefined"]
            for pat in error_patterns:
                if re.search(pat, text, re.IGNORECASE):
                    r.add_warning(f"Text contains error indicator: '{pat}'")

            if forbidden_phrases:
                for phrase in forbidden_phrases:
                    if phrase.lower() in text.lower():
                        r.add_issue(f"Forbidden phrase found: '{phrase}'", "error")

            if required_phrases:
                missing = [p for p in required_phrases if p.lower() not in text.lower()]
                if missing:
                    r.add_issue(f"Required phrases missing: {missing}")
                else:
                    r.add_check_passed(f"All required phrases present")

        r.finalize()
        return r

    def evaluate_trade_decision(self, decision: Dict, balance: float) -> ReflectionResult:
        """Specialized check for trading bot decisions."""
        r = ReflectionResult()
        r.confidence_score = 0.7
        r.quality_score = 0.7

        amount = decision.get("amount", 0)
        action = decision.get("action", "")
        pair = decision.get("pair", "")

        if not action:
            r.add_issue("No action specified", "critical")
        else:
            r.add_check_passed(f"Action specified: {action}")

        if not pair:
            r.add_issue("No trading pair specified", "critical")
        else:
            r.add_check_passed(f"Pair specified: {pair}")

        if amount <= 0:
            r.add_issue(f"Invalid amount: {amount}", "critical")
        elif amount > balance:
            r.add_issue(f"Insufficient funds: amount {amount} > balance {balance}", "critical")
        elif amount > balance * 0.5:
            r.add_warning(f"Large position: {amount} is {amount/balance*100:.1f}% of balance")
        else:
            r.add_check_passed(f"Amount {amount} within safe limits")

        r.suggestions.append("Always verify balance before placing orders")
        if amount > balance * 0.25:
            r.suggestions.append("Consider reducing position size for risk management")

        r.finalize()
        return r

    # ── Uncertainty Estimation ────────────────────────────────────

    def estimate_uncertainty(self, values: List[float]) -> Dict[str, float]:
        """
        Statistical uncertainty estimation for numeric outputs.
        Returns confidence intervals and anomaly detection.
        """
        if not values:
            return {"uncertainty": 1.0, "confidence": 0.0}

        n = len(values)
        mean = sum(values) / n
        variance = sum((v - mean) ** 2 for v in values) / n if n > 1 else 0
        std = math.sqrt(variance)
        cv = (std / abs(mean)) if mean != 0 else 1.0  # Coefficient of variation

        confidence = max(0.0, min(1.0, 1.0 - min(cv, 1.0)))
        return {
            "mean": round(mean, 4),
            "std": round(std, 4),
            "cv": round(cv, 4),
            "confidence": round(confidence, 4),
            "uncertainty": round(1.0 - confidence, 4),
            "n_samples": n,
        }

    # ── Contradiction Detection ───────────────────────────────────

    def detect_contradictions(self, statements: List[str]) -> List[Tuple[str, str]]:
        """
        Detect contradictory statements in a list.
        Returns pairs of (statement_a, statement_b) that contradict.
        """
        contradictions = []
        negation_words = {"not", "no", "never", "none", "without", "cannot", "won't", "doesn't"}

        for i, a in enumerate(statements):
            for b in statements[i+1:]:
                a_words = set(a.lower().split())
                b_words = set(b.lower().split())
                shared = a_words & b_words - {"the", "a", "is", "in", "at", "to"}
                a_neg = bool(a_words & negation_words)
                b_neg = bool(b_words & negation_words)
                if shared and (a_neg != b_neg):  # One negates, other doesn't
                    contradictions.append((a, b))

        return contradictions

    # ── History ───────────────────────────────────────────────────

    def reflection_summary(self):
        if not self._history:
            print("  [Reflect] No evaluations yet")
            return
        total = len(self._history)
        passed = sum(1 for r in self._history if r["verdict"] == "PASS")
        failed = sum(1 for r in self._history if r["verdict"] in ("FAIL", "ESCALATE"))
        avg_conf = sum(r["confidence"] for r in self._history) / total

        print(f"\n=== REFLECTION SUMMARY ===")
        print(f"  Evaluations : {total}")
        print(f"  Passed      : {passed} ({passed/total*100:.0f}%)")
        print(f"  Failed      : {failed}")
        print(f"  Avg Confidence: {avg_conf:.2f}")

    # ── Default checks ────────────────────────────────────────────

    def _load_default_checks(self):
        # Check: no Python tracebacks
        self.add_check("no_traceback",
            lambda o, c: ("Traceback" not in str(o) and "Error:" not in str(o),
                          "Traceback detected in output" if "Traceback" in str(o) else "OK"))

        # Check: output is deterministic-ish (not random garbage)
        self.add_check("not_random",
            lambda o, c: (len(str(o)) < 100000, "Output suspiciously large"))


# ── Shared instance ───────────────────────────────────────────────
reflector = SelfReflectionEngine()


if __name__ == "__main__":
    r = reflector

    # Test trade decision evaluation
    print("\n--- Trade Decision Evaluation ---")
    result = r.evaluate_trade_decision(
        {"action": "BUY", "pair": "DOGE/USD", "amount": 85},
        balance=200
    )
    result.report()

    # Test text evaluation
    print("\n--- Text Output Evaluation ---")
    result = r.evaluate_text(
        "Bot processed 142 orders successfully with 68% win rate",
        min_length=10,
        required_phrases=["orders"],
        description="Bot status text"
    )
    result.report()

    # Uncertainty estimation
    print("\n--- Uncertainty Estimation ---")
    stats = r.estimate_uncertainty([0.082, 0.083, 0.081, 0.085, 0.079, 0.12])
    print(f"  Stats: {stats}")

    r.reflection_summary()
