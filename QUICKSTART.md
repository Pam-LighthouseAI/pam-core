# nanobot Quick Start Guide

**Get a working AI assistant in 15 minutes.**

---

## What You'll Need

| Item | Where to Get It |
|------|-----------------|
| Python 3.10+ | [python.org](https://python.org) |
| Telegram account | [telegram.org](https://telegram.org) |
| LLM API key | [openrouter.ai](https://openrouter.ai) (recommended) or other provider |

---

## Step 1: Create a Telegram Bot (2 minutes)

1. Open Telegram and search for **@BotFather**
2. Send `/newbot`
3. Follow the prompts (name, username)
4. **Copy the token** — you'll need it in Step 4

Example token format: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

---

## Step 2: Install nanobot (1 minute)

Open Command Prompt and run:

```cmd
pip install nanobot
```

---

## Step 3: Create Your Instance Folder (1 minute)

```cmd
mkdir C:\nanobot\mybot
cd C:\nanobot\mybot
```

Create the virtual environment:

```cmd
python -m venv venv
venv\Scripts\activate
pip install nanobot
```

---

## Step 4: Create config.json (3 minutes)

Create a file called `config.json` in your instance folder:

```json
{
  "name": "MyBot",
  "model": "openrouter/google/gemini-2.0-flash-001",
  "port": 18790,
  "telegram": {
    "token": "YOUR_BOT_TOKEN_HERE",
    "allowed_users": [YOUR_TELEGRAM_USER_ID]
  },
  "api_keys": {
    "openrouter": "YOUR_OPENROUTER_API_KEY_HERE"
  },
  "workspace": "C:\\nanobot\\mybot\\workspace",
  "gateway": {
    "port": 18790
  }
}
```

### How to Get Your Telegram User ID:

1. Message **@userinfobot** on Telegram
2. It will reply with your numeric ID
3. Replace `YOUR_TELEGRAM_USER_ID` with that number (no quotes)

### Replace the placeholders:

| Placeholder | Replace With |
|-------------|--------------|
| `YOUR_BOT_TOKEN_HERE` | Token from @BotFather |
| `YOUR_OPENROUTER_API_KEY_HERE` | Your OpenRouter API key |
| `YOUR_TELEGRAM_USER_ID` | Your numeric Telegram ID |

---

## Step 5: Create the Launcher (1 minute)

Create a file called `start.bat` in your instance folder:

```batch
@echo off
set "NANOBOT_INSTANCE=C:\nanobot\mybot"
cd /d "%NANOBOT_INSTANCE%"
call venv\Scripts\activate
python -m nanobot
pause
```

**Important:** Use `set "VAR=value"` with quotes to avoid trailing space issues.

---

## Step 6: Create Workspace Folder (30 seconds)

```cmd
mkdir C:\nanobot\mybot\workspace
mkdir C:\nanobot\mybot\workspace\memory
```

Create a basic memory file:

```cmd
echo # Memory > C:\nanobot\mybot\workspace\memory\MEMORY.md
```

---

## Step 7: Launch and Test (2 minutes)

Double-click `start.bat` or run:

```cmd
cd C:\nanobot\mybot
start.bat
```

You should see:
```
Starting nanobot gateway on port 18790...
Telegram bot started!
```

**Test it:**
1. Open Telegram
2. Find your bot (search for the username you created)
3. Send `/start`
4. It should reply!

---

## Troubleshooting

### "Token not found" or bot doesn't respond

- Check that the token in `config.json` matches exactly what @BotFather gave you
- Make sure there are no extra spaces or quotes around the token

### "API key invalid"

- Verify your OpenRouter key at [openrouter.ai/keys](https://openrouter.ai/keys)
- Ensure you have credits or a free tier available

### "Port already in use"

- Change the port in `config.json` to something else (e.g., 18791, 18792)
- Also update the `gateway.port` value

### "Module not found: nanobot"

- Make sure you activated the venv: `venv\Scripts\activate`
- Run `pip install nanobot` again

### Bot starts but doesn't respond to me

- Check `allowed_users` in config.json has your correct Telegram user ID
- Message @userinfobot to verify your ID

---

## Recommended Free Models (OpenRouter)

| Model | Best For | Notes |
|-------|----------|-------|
| `google/gemini-2.0-flash-001` | Fast, general use | Free tier available |
| `meta-llama/llama-3.1-8b-instruct:free` | Local-style, no cost | Completely free |
| `qwen/qwen-2.5-7b-instruct:free` | Reasoning, analysis | Completely free |

---

## Next Steps

Once you're running:

1. **Customize memory** — Edit `workspace/memory/MEMORY.md` with facts about yourself
2. **Add skills** — Explore available skills with `/skills` command
3. **Set up cron jobs** — Schedule reminders and automated tasks
4. **Read the docs** — Full documentation at [nanobot.ai](https://nanobot.ai)

---

## Getting Help

- **GitHub Issues:** [github.com/nanobot-ai/nanobot/issues](https://github.com/nanobot-ai/nanobot/issues)
- **Telegram Community:** Search for nanobot community groups

---

*Last updated: 2026-03-05*
*Based on real setup experiences and troubleshooting sessions.*
