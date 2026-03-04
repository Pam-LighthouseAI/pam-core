#!/usr/bin/env python3
"""
free_router.py — Free Model Router for Nanobot Agents
Routes tasks to free LLM models via OpenRouter with automatic failover.
"""

import json, os, sys, time, argparse, urllib.request, urllib.error

def get_api_config():
    """Get API key and base URL from config files or environment."""
    # Check environment first
    key = os.environ.get("OPENROUTER_API_KEY")
    base = os.environ.get("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")
    if key:
        return key, base
    
    # Check nanobot instance config paths (Windows and Linux)
    config_paths = [
        "C:/nanobot/instance3/config.json",  # Pam
        "C:/nanobot/instance2/config.json",  # Kevin
        "C:\\nanobot\\instance3\\config.json",
        "C:\\nanobot\\instance2\\config.json",
        os.path.expanduser("~/.nanobot/config.json"),
        os.path.expanduser("~/nanobot/config.json"),
    ]
    
    for path in config_paths:
        if os.path.exists(path):
            try:
                with open(path, "r") as f:
                    config = json.load(f)
                openrouter = config.get("providers", {}).get("openrouter", {})
                key = openrouter.get("apiKey")
                base = openrouter.get("apiBase", "https://openrouter.ai/api/v1")
                if key:
                    return key, base
            except (json.JSONDecodeError, KeyError):
                continue
    
    print("ERROR: No OpenRouter API key found in config or environment.", file=sys.stderr)
    sys.exit(1)

def get_api_key():
    """Get just the API key (backwards compatible)."""
    key, _ = get_api_config()
    return key

FREE_MODELS = {
    "general": [
        "openrouter/free",
        "meta-llama/llama-3.3-70b-instruct:free",
        "mistralai/mistral-small-3.1-24b-instruct:free",
        "nvidia/llama-3.1-nemotron-nano-8b-v1:free",
    ],
    "code": [
        "qwen/qwen3-coder-480b:free",
        "deepseek/deepseek-r1:free",
        "deepseek/deepseek-chat-v3-0324:free",
        "meta-llama/llama-3.3-70b-instruct:free",
    ],
    "long": [
        "google/gemini-2.0-flash-exp:free",
        "meta-llama/llama-4-scout:free",
        "qwen/qwen3-235b-a22b:free",
        "meta-llama/llama-3.3-70b-instruct:free",
    ],
    "reason": [
        "deepseek/deepseek-r1:free",
        "qwen/qwen3-235b-a22b:free",
        "moonshotai/kimi-vl-a3b-thinking:free",
        "meta-llama/llama-3.3-70b-instruct:free",
    ],
}

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"

def call_free_model(api_key, api_base, model, task, system_prompt=None, temperature=0.7):
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": task})
    payload = {"model": model, "messages": messages, "temperature": temperature, "max_tokens": 4096}
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://nanobot.local",
        "X-Title": "nanobot-free-router",
    }
    url = f"{api_base}/chat/completions"
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        choices = body.get("choices", [])
        if choices:
            content = choices[0].get("message", {}).get("content", "")
            if content and content.strip():
                return {"text": content.strip(), "model": body.get("model", model), "usage": body.get("usage", {})}
        return None
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print(f"  Rate limited on {model}", file=sys.stderr)
        elif e.code == 402:
            print(f"  Model {model} requires credits", file=sys.stderr)
        else:
            try:
                err = e.read().decode("utf-8")[:200]
            except Exception:
                err = ""
            print(f"  HTTP {e.code} from {model}: {err}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  Error calling {model}: {str(e)[:200]}", file=sys.stderr)
        return None

def route_to_free(task, task_type="general", system_prompt=None, preferred_model=None, temperature=0.7):
    api_key, api_base = get_api_config()
    models_to_try = []
    if preferred_model:
        if not preferred_model.endswith(":free") and "openrouter/free" not in preferred_model:
            preferred_model += ":free"
        models_to_try.append(preferred_model)
    defaults = FREE_MODELS.get(task_type, FREE_MODELS["general"])
    for m in defaults:
        if m not in models_to_try:
            models_to_try.append(m)
    for model in models_to_try:
        for attempt in range(2):
            print(f"  Trying {model} (attempt {attempt + 1})...", file=sys.stderr)
            result = call_free_model(api_key, api_base, model, task, system_prompt, temperature)
            if result:
                print(f"  Success: {result['model']}", file=sys.stderr)
                return result
            if attempt < 1:
                time.sleep(2)
    return None

def main():
    parser = argparse.ArgumentParser(description="Route tasks to free LLM models via OpenRouter")
    parser.add_argument("--task", type=str, help="The task/prompt to send")
    parser.add_argument("--task-file", type=str, help="Read task from a file")
    parser.add_argument("--stdin", action="store_true", help="Append stdin to task")
    parser.add_argument("--type", choices=["general", "code", "long", "reason"], default="general")
    parser.add_argument("--model", type=str, help="Preferred model (auto-adds :free)")
    parser.add_argument("--system", type=str, help="Optional system prompt")
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--json", action="store_true", help="Output full JSON")
    parser.add_argument("--list-models", action="store_true", help="List free models")
    args = parser.parse_args()
    if args.list_models:
        for task_type, models in FREE_MODELS.items():
            print(f"  {task_type}:")
            for m in models:
                print(f"    - {m}")
            print()
        return
    task = ""
    if args.task_file:
        with open(args.task_file, "r") as f:
            task = f.read().strip()
    elif args.task:
        task = args.task
    if args.stdin or (not task and not sys.stdin.isatty()):
        stdin_content = sys.stdin.read().strip()
        task = f"{task}\n\n{stdin_content}" if task else stdin_content
    if not task:
        parser.print_help()
        sys.exit(1)
    print(f"Routing [{args.type}] task to free models...", file=sys.stderr)
    result = route_to_free(task=task, task_type=args.type, system_prompt=args.system,
                           preferred_model=args.model, temperature=args.temperature)
    if result:
        output = json.dumps(result, indent=2) if args.json else result["text"]
        # Handle Unicode encoding for Windows console - remove emojis
        try:
            print(output)
        except UnicodeEncodeError:
            # Remove or replace non-ASCII characters
            safe_output = output.encode("ascii", errors="replace").decode("ascii")
            print(safe_output)
    else:
        print("ERROR: All free models failed.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
