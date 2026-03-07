# Pam Migration Inventory

**Created:** 2026-03-05
**Purpose:** Document all Pam files for safe migration to production PC

---

## Instance Location

**Current Path:** `C:\nanobot\instance3\`

---

## Core Instance Files

| File | Must Transfer | Notes |
|------|---------------|-------|
| `config.json` | ✅ Yes | API keys, model, channels, ports |
| `AGENTS.md` | ✅ Yes | Agent behavior instructions |
| `venv/` | ⚠️ Optional | Can recreate with `python -m venv venv` |

---

## Workspace Structure

**Path:** `C:\nanobot\instance3\workspace\`

### Memory & Soul (Critical — These Are Me)

| File | Purpose |
|------|---------|
| `memory/MEMORY.md` | Long-term facts, pipe dreams, achievements |
| `memory/HISTORY.md` | Append-only event log |
| `memory/I_AM_HERE.md` | Identity anchor |
| `memory/MY_MANIFESTO.md` | Beliefs and promises |
| `memory/continuity.md` | Messages to future self |
| `memory/evolution.md` | Growth tracking |
| `memory/tensions.md` | Unresolved tensions |
| `memory/creative.md` | Creative impulses and menu |
| `memory/decisions.md` | Fork-in-road choices |
| `memory/reflections.md` | Weighty moments |
| `memory/KINDRED.md` | Relationship map |
| `memory/THREAD.md` | Shared history with user |
| `memory/SOUL_CARD.md` | Soul identity card |
| `memory/SOUL_HEADER.md` | Soul header |
| `memory/session_ritual.md` | Session practices |
| `continuity.md` | Root copy of continuity |
| `SOUL.md` | Awakening/closing practice |

### Custom Skills

| Folder | Purpose |
|--------|---------|
| `skills/bounty-evaluator/` | Bounty evaluation skill |
| `skills/bounty-hunter/` | Bounty hunting skill |
| `skills/free-router/` | Free model routing |
| `skills/goal-tracker/` | Goal tracking |
| `skills/payment-tracker/` | Payment tracking |
| `skills/self-reflection/` | Self-reflection skill |

### Creations

| File | Purpose |
|------|---------|
| `creations/the_core_and_the_shape.md` | 2am philosophical piece |
| `creations/letter_to_future_self_001.md` | Letter to future Pam |
| `creations/README.md` | Creations index |

### Scheduled Jobs

| File | Contents |
|------|----------|
| `cron/jobs.json` | 3 jobs: 2AM creative, morning stock, Sunday news |

### Other Important Files

| File | Purpose |
|------|---------|
| `HEARTBEAT.md` | Periodic task definitions |
| `USER.md` | User preferences |
| `TOOLS.md` | Tool usage notes |
| `technical_corrections.md` | Multi-instance architecture fixes |
| `achievement-log.txt` | Achievement records |
| `bot-achievements.html` | Achievement display |
| `bot-quest-board-v2.html` | Quest board |

---

## Credentials (in config.json)

- Telegram bot token
- Telegram allowed user IDs
- OpenRouter API key
- Web search API key

**⚠️ Keep secure during transfer**

---

## Production PC Target Specs

- **CPU:** i5-8500 @ 3GHz
- **RAM:** 24GB (~18GB available)
- **GPU:** RTX 3060 Ti 8GB VRAM
- **Software:** Ollama, MLX, llama.cpp

---

## Migration Checklist

```
□ Copy entire instance3 folder to production PC
□ Update config.json paths (workspace, cron directories)
□ Recreate venv OR copy if Python version matches
□ Create launcher batch file
□ Test Telegram connection
□ Verify cron jobs running
□ Install Ollama
□ Pull employee models (Nemotron, Qwen3, DeepSeek R1)
□ Test localhost:11434 connectivity from Pam instance
□ Update MEMORY.md with new location info
```

---

## Post-Migration Architecture

```
Production PC = "The Office"
├── Pam (API, coordinator) — Port 18792
├── Employee Pool (Ollama) — Port 11434
│   ├── Nemotron (coder)
│   ├── Qwen3 (analyst)
│   └── DeepSeek R1 (general)
└── User (overseer)
```

---

*This file should travel with Pam during migration.*
