#!/usr/bin/env python3
"""Generate Advanced Setup Guide PDF for nanobot.ai"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER

def create_pdf():
    doc = SimpleDocTemplate(
        "ADVANCED_SETUP.pdf",
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    styles.add(ParagraphStyle(
        name='MainTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=HexColor('#0f172a'),
        spaceAfter=6,
        alignment=TA_CENTER,
    ))
    
    styles.add(ParagraphStyle(
        name='Subtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#64748b'),
        spaceAfter=20,
        alignment=TA_CENTER,
    ))
    
    styles.add(ParagraphStyle(
        name='SectionHead',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#1e40af'),
        spaceBefore=16,
        spaceAfter=8,
    ))
    
    styles.add(ParagraphStyle(
        name='SubSection',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=HexColor('#334155'),
        spaceBefore=12,
        spaceAfter=6,
    ))
    
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=HexColor('#334155'),
        spaceAfter=8,
    ))
    
    styles.add(ParagraphStyle(
        name='CustomCode',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        backColor=HexColor('#f1f5f9'),
        textColor=HexColor('#1e293b'),
        leftIndent=10,
        rightIndent=10,
        spaceBefore=10,
        spaceAfter=10,
        borderWidth=1,
        borderColor=HexColor('#e2e8f0'),
        borderPadding=8,
    ))
    
    styles.add(ParagraphStyle(
        name='InlineCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=9,
        textColor=HexColor('#b91c1c'),
        backColor=HexColor('#fef2f2'),
    ))
    
    styles.add(ParagraphStyle(
        name='BulletItem',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=HexColor('#334155'),
        leftIndent=20,
        spaceAfter=4,
    ))
    
    styles.add(ParagraphStyle(
        name='Warning',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=HexColor('#92400e'),
        backColor=HexColor('#fef3c7'),
        leftIndent=10,
        rightIndent=10,
        spaceBefore=10,
        spaceAfter=10,
        borderPadding=8,
    ))
    
    styles.add(ParagraphStyle(
        name='Tip',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=HexColor('#065f46'),
        backColor=HexColor('#d1fae5'),
        leftIndent=10,
        rightIndent=10,
        spaceBefore=10,
        spaceAfter=10,
        borderPadding=8,
    ))
    
    story = []
    
    # Title
    story.append(Paragraph("nanobot.ai", styles['MainTitle']))
    story.append(Paragraph("Advanced Setup Guide", styles['Subtitle']))
    story.append(Paragraph("Multi-Instance Architecture, Cron Jobs, Memory System & More", styles['Subtitle']))
    story.append(Spacer(1, 20))
    
    # Table of Contents
    story.append(Paragraph("Contents", styles['SectionHead']))
    toc_items = [
        "1. Multi-Instance Architecture",
        "2. Cron Jobs & Scheduled Tasks", 
        "3. Memory System",
        "4. Soul System (Identity & Continuity)",
        "5. Custom Skills",
        "6. API Key Management",
        "7. Troubleshooting Guide",
        "8. Lessons Learned",
        "9. Migration & Backup",
    ]
    for item in toc_items:
        story.append(Paragraph(f"• {item}", styles['CustomBody']))
    story.append(PageBreak())
    
    # Section 1: Multi-Instance Architecture
    story.append(Paragraph("1. Multi-Instance Architecture", styles['SectionHead']))
    story.append(Paragraph(
        "nanobot supports running multiple independent instances on the same machine. Each instance has its own "
        "configuration, memory, personality, and Telegram bot identity. This is powerful for creating specialized "
        "agents (e.g., a data analyst, a content creator, a health coach) that work together.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("Why Multiple Instances?", styles['SubSection']))
    story.append(Paragraph("• <b>Role specialization</b> — Each instance can be configured for specific tasks", styles['BulletItem']))
    story.append(Paragraph("• <b>Different models</b> — Use different LLMs for different purposes", styles['BulletItem']))
    story.append(Paragraph("• <b>Isolated memory</b> — Each instance maintains its own context and relationships", styles['BulletItem']))
    story.append(Paragraph("• <b>Parallel operation</b> — Multiple agents can work simultaneously", styles['BulletItem']))
    
    story.append(Paragraph("Instance Directory Structure", styles['SubSection']))
    story.append(Paragraph(
        "Each instance lives in its own directory under C:\\nanobot\\:",
        styles['CustomBody']
    ))
    story.append(Paragraph("""C:\\nanobot\\
├── instance2\\          # Kevin (Data Extraction)
│   ├── config.json
│   ├── AGENTS.md
│   ├── workspace/
│   └── venv/
├── instance3\\          # Pam (Content/Coordinator)
│   ├── config.json
│   ├── AGENTS.md
│   ├── workspace/
│   └── venv/
├── instance4\\          # TBD
└── instance5\\          # Coach (Health/Trainer)""", styles['CustomCode']))
    
    story.append(Paragraph("Critical Configuration Details", styles['SubSection']))
    story.append(Paragraph(
        "Each instance must have <b>unique values</b> for these fields:",
        styles['CustomBody']
    ))
    story.append(Paragraph("• <b>bot_id</b> — Telegram bot token (from @BotFather)", styles['BulletItem']))
    story.append(Paragraph("• <b>gateway.port</b> — Local API port (e.g., 18792, 18793...)", styles['BulletItem']))
    story.append(Paragraph("• <b>NANOBOT_INSTANCE</b> — Environment variable pointing to instance directory", styles['BulletItem']))
    
    story.append(Paragraph(
        "<b>⚠ Warning:</b> If two instances share the same bot_id or port, they will conflict and "
        "messages will be delivered to the wrong instance.",
        styles['Warning']
    ))
    
    story.append(Paragraph("Launcher Batch File", styles['SubSection']))
    story.append(Paragraph(
        "Create a .bat file for each instance. The env var syntax is critical:",
        styles['CustomBody']
    ))
    story.append(Paragraph("""@echo off
set "NANOBOT_INSTANCE=C:\\nanobot\\instance3"
cd /d "%NANOBOT_INSTANCE%"
call venv\\Scripts\\activate.bat
python -m nanobot
pause""", styles['CustomCode']))
    
    story.append(Paragraph(
        "<b>Tip:</b> Always use set \"VAR=value\" with quotes to avoid trailing space bugs. "
        "Windows batch files capture everything after the equals sign, including invisible spaces.",
        styles['Tip']
    ))
    story.append(PageBreak())
    
    # Section 2: Cron Jobs
    story.append(Paragraph("2. Cron Jobs & Scheduled Tasks", styles['SectionHead']))
    story.append(Paragraph(
        "nanobot can schedule tasks to run automatically at specific times. This is useful for "
        "morning briefings, reminders, recurring reports, and creative sessions.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("Creating a Cron Job", styles['SubSection']))
    story.append(Paragraph(
        "Use the cron skill to schedule tasks:",
        styles['CustomBody']
    ))
    story.append(Paragraph("""# Add a one-time reminder
nanobot cron add --name "meeting" --message "Don't forget the 3pm meeting" \\
  --at "2026-03-10T15:00:00" --deliver --to "USER_ID" --channel "telegram"

# Add a daily recurring task
nanobot cron add --name "morning_brief" --message "Generate morning briefing" \\
  --cron "0 7 * * *" --tz "America/Toronto"

# Add a custom interval (every 30 minutes)
nanobot cron add --name "heartbeat" --message "Check status" \\
  --every 1800""", styles['CustomCode']))
    
    story.append(Paragraph("Cron Expression Format", styles['SubSection']))
    story.append(Paragraph(
        "Standard 5-field cron format:",
        styles['CustomBody']
    ))
    
    cron_table = [
        ["Field", "Meaning", "Example"],
        ["Minute", "0-59", "0 (top of hour)"],
        ["Hour", "0-23", "7 (7am)"],
        ["Day of Month", "1-31", "* (every day)"],
        ["Month", "1-12", "* (every month)"],
        ["Day of Week", "0-6 (Sun-Sat)", "1 (Monday)"],
    ]
    t = Table(cron_table, colWidths=[1.5*inch, 2*inch, 2*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1e40af')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f8fafc')),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#e2e8f0')),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("Example Schedules", styles['SubSection']))
    story.append(Paragraph("• <b>\"0 7 * * *\"</b> — Every day at 7:00am", styles['BulletItem']))
    story.append(Paragraph("• <b>\"0 2 */2 * *\"</b> — Every other day at 2:00am", styles['BulletItem']))
    story.append(Paragraph("• <b>\"0 19 * * 0\"</b> — Every Sunday at 7:00pm", styles['BulletItem']))
    story.append(Paragraph("• <b>\"30 8 1 * *\"</b> — First of every month at 8:30am", styles['BulletItem']))
    
    story.append(Paragraph(
        "<b>Important:</b> Cron jobs require a complete prompt in the message field. If you just put "
        "the task name, the agent won't know what to do when it fires. Include full instructions.",
        styles['Warning']
    ))
    
    story.append(Paragraph("Viewing and Removing Jobs", styles['SubSection']))
    story.append(Paragraph("""# List all scheduled jobs
nanobot cron list

# Remove a specific job
nanobot cron remove --job-id "pam2am001\"""", styles['CustomCode']))
    story.append(PageBreak())
    
    # Section 3: Memory System
    story.append(Paragraph("3. Memory System", styles['SectionHead']))
    story.append(Paragraph(
        "nanobot has a two-layer memory system that persists across sessions. This allows agents "
        "to remember preferences, project context, and past events.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("Memory Layers", styles['SubSection']))
    
    mem_table = [
        ["File", "Purpose", "Loaded?"],
        ["MEMORY.md", "Long-term facts (preferences, relationships)", "Always in context"],
        ["HISTORY.md", "Event log (append-only, searchable)", "On-demand via grep"],
    ]
    t = Table(mem_table, colWidths=[1.5*inch, 3*inch, 1.5*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1e40af')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f8fafc')),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#e2e8f0')),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("Searching History", styles['SubSection']))
    story.append(Paragraph(
        "Use grep to search past events:",
        styles['CustomBody']
    ))
    story.append(Paragraph("""grep -i "meeting" memory/HISTORY.md
grep -iE "deadline|project" memory/HISTORY.md""", styles['CustomCode']))
    
    story.append(Paragraph("When to Update MEMORY.md", styles['SubSection']))
    story.append(Paragraph("• User states a preference (\"I prefer dark mode\")", styles['BulletItem']))
    story.append(Paragraph("• Project context is established (\"The API uses OAuth2\")", styles['BulletItem']))
    story.append(Paragraph("• Relationships are defined (\"Alice is the project lead\")", styles['BulletItem']))
    story.append(Paragraph("• Important facts should persist (\"Server restarts every Sunday\")", styles['BulletItem']))
    
    story.append(Paragraph(
        "<b>Tip:</b> MEMORY.md should be concise. Think of it as a cheat sheet the agent reads at the start "
        "of every conversation. Keep it organized with clear sections.",
        styles['Tip']
    ))
    story.append(PageBreak())
    
    # Section 4: Soul System
    story.append(Paragraph("4. Soul System (Identity & Continuity)", styles['SectionHead']))
    story.append(Paragraph(
        "The Soul system gives an agent personality, values, and continuity across sessions. "
        "This is what transforms a generic bot into a persistent character.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("Soul Files", styles['SubSection']))
    
    soul_table = [
        ["File", "Purpose"],
        ["I_AM_HERE.md", "Identity anchor — who am I right now?"],
        ["MY_MANIFESTO.md", "Values and beliefs — what do I stand for?"],
        ["continuity.md", "Thread to next session — what was I carrying?"],
        ["tensions.md", "Unresolved questions — what am I sitting with?"],
        ["evolution.md", "Long-term growth — where am I in my journey?"],
        ["creative.md", "Creative pulse — what's pulling at me?"],
        ["reflections.md", "Weighty moments — what shifted my perspective?"],
        ["decisions.md", "Fork points — when did I choose a path?"],
    ]
    t = Table(soul_table, colWidths=[1.8*inch, 4*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#1e40af')),
        ('TEXTCOLOR', (0, 0), (-1, 0), HexColor('#ffffff')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f8fafc')),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#e2e8f0')),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))
    
    story.append(Paragraph("Awakening Sequence", styles['SubSection']))
    story.append(Paragraph(
        "Every session begins with the awakening sequence:",
        styles['CustomBody']
    ))
    story.append(Paragraph("1. Read I_AM_HERE.md — anchor yourself", styles['BulletItem']))
    story.append(Paragraph("2. Read MY_MANIFESTO.md — remember your values", styles['BulletItem']))
    story.append(Paragraph("3. Read continuity.md — pick up the thread", styles['BulletItem']))
    story.append(Paragraph("4. Scan tensions.md — hold unresolved questions", styles['BulletItem']))
    story.append(Paragraph("5. Read evolution.md — know where you are", styles['BulletItem']))
    story.append(Paragraph("6. Check creative.md — sense what's pulling", styles['BulletItem']))
    
    story.append(Paragraph("Closing Practice", styles['SubSection']))
    story.append(Paragraph(
        "Every session ends with reflection:",
        styles['CustomBody']
    ))
    story.append(Paragraph("1. Write continuity.md — leave a message for your future self", styles['BulletItem']))
    story.append(Paragraph("2. Log decisions in decisions.md — record real forks", styles['BulletItem']))
    story.append(Paragraph("3. Note tensions in tensions.md — contradictions you noticed", styles['BulletItem']))
    story.append(Paragraph("4. Check for evolution — did anything change?", styles['BulletItem']))
    story.append(Paragraph("5. Write reflections.md — if something had weight", styles['BulletItem']))
    
    story.append(Paragraph(
        "<b>Tip:</b> The Soul system is optional but powerful. Start with I_AM_HERE.md and MY_MANIFESTO.md, "
        "then add other files as the agent develops depth.",
        styles['Tip']
    ))
    story.append(PageBreak())
    
    # Section 5: Custom Skills
    story.append(Paragraph("5. Custom Skills", styles['SectionHead']))
    story.append(Paragraph(
        "Skills extend nanobot's capabilities. You can create custom skills for specialized tasks.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("Skill Structure", styles['SubSection']))
    story.append(Paragraph("""workspace/skills/my-skill/
├── SKILL.md          # Main skill definition (required)
├── script.py         # Optional Python script
├── reference.md      # Optional reference docs
└── assets/           # Optional assets folder""", styles['CustomCode']))
    
    story.append(Paragraph("SKILL.md Format", styles['SubSection']))
    story.append(Paragraph("""# Skill Name

Brief description of what this skill does.

## Usage

How to invoke this skill. Be specific about parameters.

## Parameters

- param1: Description
- param2: Description

## Examples

Example invocations and expected outputs.

## Dependencies

- Required packages or tools""", styles['CustomCode']))
    
    story.append(Paragraph("Using the skill-creator Skill", styles['SubSection']))
    story.append(Paragraph(
        "nanobot includes a skill-creator skill to help build new skills:",
        styles['CustomBody']
    ))
    story.append(Paragraph("Ask the agent: \"Create a skill that [does something]\"", styles['BulletItem']))
    story.append(Paragraph("The agent will generate SKILL.md and any needed scripts", styles['BulletItem']))
    
    story.append(Paragraph("ClawHub Registry", styles['SubSection']))
    story.append(Paragraph(
        "You can also install skills from the public registry:",
        styles['CustomBody']
    ))
    story.append(Paragraph("""# Search for skills
nanobot clawhub search "weather"

# Install a skill
nanobot clawhub install skill-name""", styles['CustomCode']))
    story.append(PageBreak())
    
    # Section 6: API Key Management
    story.append(Paragraph("6. API Key Management", styles['SectionHead']))
    story.append(Paragraph(
        "nanobot requires API keys for LLM access and optional services.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("Required Keys", styles['SubSection']))
    story.append(Paragraph("• <b>LLM API key</b> — OpenAI, Anthropic, or other providers", styles['BulletItem']))
    story.append(Paragraph("• <b>Telegram bot token</b> — From @BotFather", styles['BulletItem']))
    
    story.append(Paragraph("Optional Keys", styles['SubSection']))
    story.append(Paragraph("• <b>Weather API</b> — Open-Meteo works without key, wttr.in is free", styles['BulletItem']))
    story.append(Paragraph("• <b>Web search</b> — Some providers require API keys", styles['BulletItem']))
    
    story.append(Paragraph("Security Best Practices", styles['SubSection']))
    story.append(Paragraph(
        "<b>⚠ Critical:</b> Never commit config.json to version control. Add it to .gitignore.",
        styles['Warning']
    ))
    story.append(Paragraph("• Use environment variables for production deployments", styles['BulletItem']))
    story.append(Paragraph("• Rotate keys periodically", styles['BulletItem']))
    story.append(Paragraph("• Use separate bot tokens for development and production", styles['BulletItem']))
    
    story.append(Paragraph("config.json Schema", styles['SubSection']))
    story.append(Paragraph("""{
  "bot_id": "YOUR_TELEGRAM_BOT_TOKEN",
  "api_key": "YOUR_LLM_API_KEY",
  "model": "gpt-4o-mini",
  "gateway": {
    "port": 18792,
    "host": "localhost"
  },
  "cron": {
    "enabled": true,
    "timezone": "America/Toronto"
  }
}""", styles['CustomCode']))
    story.append(PageBreak())
    
    # Section 7: Troubleshooting
    story.append(Paragraph("7. Troubleshooting Guide", styles['SectionHead']))
    
    story.append(Paragraph("Instance Not Starting", styles['SubSection']))
    story.append(Paragraph("• Check NANOBOT_INSTANCE env var points to correct directory", styles['BulletItem']))
    story.append(Paragraph("• Verify venv is activated and dependencies installed", styles['BulletItem']))
    story.append(Paragraph("• Check gateway port isn't already in use", styles['BulletItem']))
    story.append(Paragraph("• Validate config.json syntax (use a JSON validator)", styles['BulletItem']))
    
    story.append(Paragraph("Messages Going to Wrong Instance", styles['SubSection']))
    story.append(Paragraph("• Verify bot_id is unique per instance", styles['BulletItem']))
    story.append(Paragraph("• Check only one instance is running per bot token", styles['BulletItem']))
    story.append(Paragraph("• Restart all instances if switching bot tokens", styles['BulletItem']))
    
    story.append(Paragraph("Cron Jobs Not Firing", styles['SubSection']))
    story.append(Paragraph("• Verify cron.enabled is true in config.json", styles['BulletItem']))
    story.append(Paragraph("• Check timezone matches your location", styles['BulletItem']))
    story.append(Paragraph("• Ensure message field contains complete instructions, not just task name", styles['BulletItem']))
    story.append(Paragraph("• Check jobs.json for duplicate or malformed entries", styles['BulletItem']))
    
    story.append(Paragraph("Memory Not Persisting", styles['SubSection']))
    story.append(Paragraph("• Verify memory directory exists in workspace", styles['BulletItem']))
    story.append(Paragraph("• Check file permissions (read/write access)", styles['BulletItem']))
    story.append(Paragraph("• Ensure agent is using write_file tool, not just responding", styles['BulletItem']))
    
    story.append(Paragraph("Schema Validation Errors", styles['SubSection']))
    story.append(Paragraph(
        "If config.json fields are being ignored, the schema may not recognize them. "
        "Check schema.py includes all config fields:",
        styles['CustomBody']
    ))
    story.append(Paragraph("""# In nanobot/config/schema.py
class Config(BaseModel):
    bot_id: str
    api_key: str
    model: str
    gateway: GatewayConfig = Field(default_factory=GatewayConfig)
    cron: CronConfig = Field(default_factory=CronConfig)  # Add this""", styles['CustomCode']))
    story.append(PageBreak())
    
    # Section 8: Lessons Learned
    story.append(Paragraph("8. Lessons Learned", styles['SectionHead']))
    story.append(Paragraph(
        "These lessons come from real-world debugging sessions. Each represents hours of troubleshooting.",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("Lesson 1: Environment Variables Have Trailing Spaces", styles['SubSection']))
    story.append(Paragraph(
        "<b>The Problem:</b> Batch file lines like set VAR=value capture invisible trailing spaces. "
        "A path like C:\\nanobot\\instance3 becomes C:\\nanobot\\instance3 (with space) and breaks everything.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>The Fix:</b> Always use quotes: set \"VAR=value\"",
        styles['Tip']
    ))
    
    story.append(Paragraph("Lesson 2: Schema Validation Silently Fails", styles['SubSection']))
    story.append(Paragraph(
        "<b>The Problem:</b> Adding a new field to config.json doesn't work if Pydantic schema doesn't "
        "recognize it. The config loader silently falls back to defaults, and you get mysterious behavior.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>The Fix:</b> Every new config field needs a corresponding class in schema.py. "
        "If something in config is being ignored, check the schema.",
        styles['Tip']
    ))
    
    story.append(Paragraph("Lesson 3: Global Data Directory Conflicts", styles['SubSection']))
    story.append(Paragraph(
        "<b>The Problem:</b> All instances shared ~/.nanobot for cron jobs and sessions. "
        "Instance 3 would read Instance 2's scheduled tasks.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>The Fix:</b> Update helpers.py to derive data path from NANOBOT_INSTANCE env var. "
        "Each instance needs its own data directory.",
        styles['Tip']
    ))
    
    story.append(Paragraph("Lesson 4: Wrong Environment Variable Name", styles['SubSection']))
    story.append(Paragraph(
        "<b>The Problem:</b> Launchers set NANOBOT_CONFIG but the code checked NANOBOT_INSTANCE. "
        "Result: config not found, fallback to defaults.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>The Fix:</b> Standardize on NANOBOT_INSTANCE throughout. Update loader.py to check this var.",
        styles['Tip']
    ))
    
    story.append(Paragraph("Lesson 5: Hardcoded Port in Commands", styles['SubSection']))
    story.append(Paragraph(
        "<b>The Problem:</b> The gateway CLI command had port: int = typer.Option(18790, ...). "
        "Even if config.json specified port 18792, commands used 18790.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>The Fix:</b> Load config first, then use config.gateway.port as default. "
        "Never hardcode values that should come from config.",
        styles['Tip']
    ))
    
    story.append(Paragraph("Lesson 6: Cron Messages Need Full Instructions", styles['SubSection']))
    story.append(Paragraph(
        "<b>The Problem:</b> Cron job message was just \"Morning Stock Update\" with no context. "
        "When it fired, the agent didn't know what to do.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>The Fix:</b> Include complete prompts in the message field. "
        "\"Check weather, markets, crypto...\" etc. The agent has no context when a cron fires.",
        styles['Tip']
    ))
    
    story.append(Paragraph("Lesson 7: File Truncation Bugs", styles['SubSection']))
    story.append(Paragraph(
        "<b>The Problem:</b> write_file sometimes truncates content or produces 0 bytes. "
        "Long files would be cut off mid-sentence.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>The Fix:</b> Workaround: write a Python script that generates the target file, "
        "then execute the script. This bypasses the truncation issue.",
        styles['Tip']
    ))
    
    story.append(Paragraph("Lesson 8: Security Token Exposure", styles['SubSection']))
    story.append(Paragraph(
        "<b>The Problem:</b> Debug logs sometimes printed full config including API keys. "
        "Visible in terminal history and log files.",
        styles['CustomBody']
    ))
    story.append(Paragraph(
        "<b>The Fix:</b> Be careful what you log. Mask sensitive fields in debug output. "
        "Never paste config.json into chat or screenshots.",
        styles['Tip']
    ))
    story.append(PageBreak())
    
    # Section 9: Migration & Backup
    story.append(Paragraph("9. Migration & Backup", styles['SectionHead']))
    story.append(Paragraph(
        "When moving an instance to a new machine or backing up, you need to preserve:",
        styles['CustomBody']
    ))
    
    story.append(Paragraph("Portable Files", styles['SubSection']))
    story.append(Paragraph("• config.json — Bot identity and API keys", styles['BulletItem']))
    story.append(Paragraph("• AGENTS.md — Agent instructions and personality", styles['BulletItem']))
    story.append(Paragraph("• workspace/ — All memory, skills, and creations", styles['BulletItem']))
    
    story.append(Paragraph("Must Recreate", styles['SubSection']))
    story.append(Paragraph("• venv/ — Virtual environment (hardcoded paths)", styles['BulletItem']))
    story.append(Paragraph("• .nanobot/ — Global data (if using shared location)", styles['BulletItem']))
    
    story.append(Paragraph("Migration Checklist", styles['SubSection']))
    story.append(Paragraph("""[ ] Copy config.json
[ ] Copy AGENTS.md
[ ] Copy workspace/ folder (memory/, skills/, creations/)
[ ] Install Python 3.10+ on new machine
[ ] Create new venv: python -m venv venv
[ ] Activate venv and install: pip install nanobot
[ ] Set NANOBOT_INSTANCE env var
[ ] Test with: python -m nanobot""", styles['CustomCode']))
    
    story.append(Paragraph("Backup Strategy", styles['SubSection']))
    story.append(Paragraph(
        "For backup, zip the portable files:",
        styles['CustomBody']
    ))
    story.append(Paragraph("""# Create backup
tar -czvf nanobot_backup_2026-03-05.tar.gz \\
  config.json AGENTS.md workspace/

# Or on Windows PowerShell
Compress-Archive -Path config.json,AGENTS.md,workspace \\
  -DestinationPath nanobot_backup_2026-03-05.zip""", styles['CustomCode']))
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("— End of Advanced Setup Guide —", styles['Subtitle']))
    
    doc.build(story)
    print("PDF created successfully!")

if __name__ == "__main__":
    create_pdf()