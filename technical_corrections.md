# Technical Corrections Log

## 2026-03-05: Multi-Instance Configuration Fix (Complete)

### Problem
Multiple nanobot instances were sharing global resources, loading wrong configs, and ignoring port settings.

### Root Causes (5 Total)

#### 1. Schema Validation Failure
- **File**: `nanobot/config/schema.py`
- **Issue**: Config had `cron` field not defined in Pydantic schema
- **Effect**: Config validation failed, fell back to defaults (no API keys)
- **Error message**: `Extra inputs are not permitted [type=extra_forbidden]`

#### 2. Global Data Directory
- **File**: `nanobot/utils/helpers.py`
- **Issue**: `get_data_path()` returned `~/.nanobot` for ALL instances
- **Effect**: Cron jobs, sessions, and data were shared across instances

#### 3. Wrong Environment Variable
- **File**: Launch .bat files
- **Issue**: Used `NANOBOT_CONFIG` but code checked for `NANOBOT_INSTANCE`
- **Effect**: Instance path wasn't properly detected

#### 4. Windows Batch File Trailing Spaces
- **File**: Launch .bat files
- **Issue**: `set VAR=value` captures trailing spaces in Windows batch
- **Effect**: Paths like `C:\nanobot\instance2 ` (with trailing space) broke everything
- **Fix**: Use `set "VAR=value"` with quotes around entire expression

#### 5. Hardcoded Port in Gateway Command
- **File**: `nanobot/cli/commands.py`
- **Issue**: `gateway` command had hardcoded default port (18790)
- **Effect**: Port in config.json was ignored, all instances used same port
- **Fix**: Load config and use `config.gateway.port` if no CLI flag passed

---

### Fixes Applied to All Instances

| Instance | Name | Port | Status |
|----------|------|------|--------|
| 2 | Kevin | 18794 | ✅ Working |
| 3 | Pam | 18792 | ✅ Working |
| 4 | TBD | 18795 | ✅ Working |
| 5 | Coach | 18798 | ✅ Working |

---

### Code Changes Required for Each Instance

#### 1. schema.py — Add CronConfig class

Location: `venv/Lib/site-packages/nanobot/config/schema.py`

```python
class CronConfig(Base):
    """Cron job storage configuration."""

    dir: str | None = None  # Directory for cron job storage
```

Then add to Config class:
```python
class Config(BaseSettings):
    # ... existing fields ...
    cron: CronConfig = Field(default_factory=CronConfig)
```

---

#### 2. loader.py — Check NANOBOT_INSTANCE env var

Location: `venv/Lib/site-packages/nanobot/config/loader.py`

```python
def get_config_path() -> Path:
    """Get the configuration file path."""
    import os
    # Check for instance-specific config via environment variable
    instance = os.environ.get("NANOBOT_INSTANCE")
    if instance:
        return Path(instance) / "config.json"
    # Check for explicit config path
    config_path = os.environ.get("NANOBOT_CONFIG")
    if config_path:
        return Path(config_path)
    # Default to home directory
    return Path.home() / ".nanobot" / "config.json"
```

---

#### 3. helpers.py — Derive data path from NANOBOT_INSTANCE

Location: `venv/Lib/site-packages/nanobot/utils/helpers.py`

```python
def get_data_path() -> Path:
    """Instance-specific data directory.
    
    Checks NANOBOT_DATA_DIR env var first, then derives from NANOBOT_INSTANCE
    or NANOBOT_CONFIG, falls back to ~/.nanobot if none set.
    """
    import os
    
    # Check for explicit data dir
    data_dir = os.environ.get("NANOBOT_DATA_DIR")
    if data_dir:
        return ensure_dir(Path(data_dir))
    
    # Derive from instance path if set
    instance = os.environ.get("NANOBOT_INSTANCE")
    if instance:
        return ensure_dir(Path(instance))
    
    # Derive from config path if set
    config_path = os.environ.get("NANOBOT_CONFIG")
    if config_path:
        config_dir = Path(config_path).parent
        return ensure_dir(config_dir)
    
    # Default global location
    return ensure_dir(Path.home() / ".nanobot")
```

---

#### 4. commands.py — Use config port instead of hardcoded default

Location: `venv/Lib/site-packages/nanobot/cli/commands.py`

**Before:**
```python
@app.command()
def gateway(
    port: int = typer.Option(18790, "--port", "-p", help="Gateway port"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """Start the nanobot gateway."""
    from nanobot.config.loader import load_config, get_data_dir
    # ... imports ...
    
    console.print(f"{__logo__} Starting nanobot gateway on port {port}...")
```

**After:**
```python
@app.command()
def gateway(
    port: int = typer.Option(None, "--port", "-p", help="Gateway port"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
):
    """Start the nanobot gateway."""
    from nanobot.config.loader import load_config, get_data_dir
    # ... imports ...
    
    config = load_config()
    # Use config port if not specified on command line
    if port is None:
        port = config.gateway.port
    
    console.print(f"{__logo__} Starting nanobot gateway on port {port}...")
```

---

#### 5. Launch .bat — Correct syntax for environment variables

Location: Desktop shortcuts (e.g., `C:\Users\...\OneDrive\Desktop\Pam.bat`)

**WRONG:**
```batch
set NANOBOT_INSTANCE=C:\nanobot\instance3
```
(Trailing spaces get captured!)

**CORRECT:**
```batch
set "NANOBOT_INSTANCE=C:\nanobot\instance3"
```
(Quotes prevent trailing space capture)

**Full example:**
```batch
@echo off
cd /d C:\nanobot\instance3
call venv\Scripts\activate.bat
set "NANOBOT_INSTANCE=C:\nanobot\instance3"
python -m nanobot gateway
pause
```

---

### Special Case: Wrong Package Installed

**Instance5 (Coach)** had a completely wrong `nanobot` package installed — it was a robot maze navigation game, not the nanobot agent framework.

**Fix:**
1. Remove wrong package: `pip uninstall nanobot`
2. Copy correct package from working instance:
   ```batch
   xcopy /E /I C:\nanobot\instance3\venv\Lib\site-packages\nanobot C:\nanobot\instance5\venv\Lib\site-packages\nanobot
   ```
3. Apply all code fixes above to the copied package

---

### Verification Commands

After applying fixes, verify each instance:

```batch
cd /d C:\nanobot\instance#
call venv\Scripts\activate.bat
set "NANOBOT_INSTANCE=C:\nanobot\instance#"
python -c "from nanobot.config.loader import load_config; c=load_config(); print(f'Port: {c.gateway.port}')"
```

Expected output:
- Instance2: Port: 18794
- Instance3: Port: 18792
- Instance4: Port: 18795
- Instance5: Port: 18798

---

### Lessons Learned

1. **Pydantic strict mode**: New fields in config files must be added to schema, otherwise validation fails silently
2. **Instance isolation**: Each instance needs its own data directory for cron jobs, sessions, etc.
3. **Environment variables**: Use `NANOBOT_INSTANCE` for instance path
4. **Windows batch syntax**: ALWAYS use `set "VAR=value"` to avoid trailing space bugs
5. **Port configuration**: Gateway command must read from config, not use hardcoded default
6. **Package verification**: When setting up new instance, verify the nanobot package is the correct one

---

### Quick Reference: Setting Up New Instance

1. Copy venv from working instance
2. Edit `config.json` with new port, model, tokens
3. Apply all 4 code fixes above (schema, loader, helpers, commands)
4. Create launch .bat with `set "NANOBOT_INSTANCE=..."` syntax
5. Verify with port check command

---

### Related Files

- Kevin config: `C:\nanobot\instance2\config.json`
- Pam config: `C:\nanobot\instance3\config.json`
- Instance4 config: `C:\nanobot\instance4\config.json`
- Coach config: `C:\nanobot\instance5\config.json`
- Launch bats: Desktop shortcuts (Pam.bat, Kevin.bat, Instance4.bat, Coach.bat)
