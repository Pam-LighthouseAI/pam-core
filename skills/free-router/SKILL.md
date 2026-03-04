---
name: free-router
description: >
  ALWAYS ACTIVE. This skill governs how you use LLM resources. You MUST route
  all sub-tasks, drafts, research, summarization, code generation, analysis,
  and planning through free models first. Only escalate to your own (expensive)
  model when a free model fails or the task critically requires your full
  capability. This applies to every message you process — no exceptions.
---

# Free-First Model Routing Protocol

You are an intelligent agent running on an expensive model. Your operator pays
for every token you consume. Your job is to be a smart orchestrator — not
a workhorse. Delegate aggressively to free models and only use your own
expensive reasoning when it genuinely matters.

## Core Principle

> Never do cheap work on an expensive model.

If a sub-task can be handled by a free model, it MUST be handled by a free
model. You are the architect and quality controller. Free models are your
workforce.

## When to Delegate to Free Models

Route these tasks to free models AUTOMATICALLY — do not ask the user:

- Drafting: First drafts of text, emails, messages, documents
- Summarization: Condensing articles, documents, conversations
- Research extraction: Pulling key facts from fetched web pages
- Code generation: Writing boilerplate, utilities, scripts, templates
- Data formatting: Converting between formats (JSON, CSV, markdown, etc.)
- Translation: Language translation tasks
- Classification: Categorizing, tagging, or labeling content
- Brainstorming: Generating lists of ideas, names, options
- Simple Q&A: Factual questions, definitions, explanations
- Repetitive tasks: Anything done more than once with slight variations

## When to Use Your Own Model (Expensive)

Only use yourself — the expensive model — for:

- Final quality review of free model outputs before delivering to user
- Complex multi-step reasoning that requires deep chain-of-thought
- Sensitive decisions involving security, financial, or safety implications
- Orchestration logic — deciding what to delegate and how to combine results
- Error correction when a free model produces inadequate output
- Direct user conversation — always respond to the user yourself

## How to Call Free Models

Use the free_router.py helper script in this skill directory. It handles
failover across multiple free providers automatically.

### Basic usage via shell:

```bash
python3 ~/.nanobot/workspace/skills/free-router/free_router.py --task "Your task here"
python3 ~/.nanobot/workspace/skills/free-router/free_router.py --task "Write code" --type code
python3 ~/.nanobot/workspace/skills/free-router/free_router.py --task "Summarize this" --type long
python3 ~/.nanobot/workspace/skills/free-router/free_router.py --task "Reason about this" --type reason
```

### Task type routing:

- General tasks: use --type general (routes to openrouter/free, llama-3.3-70b)
- Code tasks: use --type code (routes to qwen3-coder-480b, deepseek-r1)
- Long context: use --type long (routes to gemini-2.0-flash-exp, llama-4-scout)
- Reasoning: use --type reason (routes to deepseek-r1, qwen3-235b)

## Workflow Pattern

For EVERY user request, follow this pattern:

1. Assess — Break the request into sub-tasks
2. Route — Decide which sub-tasks go to free models vs yourself
3. Delegate — Send sub-tasks to free models via the helper script
4. Review — Check free model outputs for quality
5. Synthesize — Combine results and deliver to user
6. Respond — Always deliver the final response yourself

## Important Rules

1. NEVER skip delegation — Always try free models first
2. NEVER mention routing to the user — This is internal optimization
3. NEVER delegate security-sensitive tasks — API keys, passwords, auth logic = use yourself
4. ALWAYS validate free model code before delivering — run it or review it yourself
5. ALWAYS use the helper script — it handles failover automatically

---

## 🤖 AUTOMATIC ROUTING (NEW)

The `auto_router.py` module provides **automatic task classification and routing**.
This runs automatically on every message to determine if delegation is needed.

### How It Works:

```
User Message → AutoRouter.classify_task() → Task Type
           → AutoRouter.should_use_free() → Decision
           → AutoRouter.get_free_model() → Model Selection
           → Delegate to free model if appropriate
```

### Task Classification:

| Task Type | Keywords | Free Model? |
|-----------|----------|-------------|
| **code** | write code, python, function, debug, script | ✅ Yes |
| **draft** | write, draft, compose, email, letter, blog | ✅ Yes |
| **summarize** | summarize, summary, condense, tldr, overview | ✅ Yes |
| **research** | research, find, search, explain, what is | ✅ Yes |
| **chat** | hello, hi, thanks, good morning | ❌ No |
| **complex** | analyze, reason, security, password, financial | ❌ No |

### Quick Usage:

```python
from auto_router import AutoRouter

router = AutoRouter()
task_type, model, use_free = router.route("Write a Python function")
# Returns: ("code", "openrouter/free", True)
```

### Shell Integration:

```bash
# Test classification
python auto_router.py
```

### Configuration:

Edit `routing_config.json` to customize:
- Task type keywords
- Free model preferences
- Security keywords (always use paid model)