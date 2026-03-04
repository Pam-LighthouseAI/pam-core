#!/usr/bin/env python3
"""
auto_router.py — Automatic Task Router for Nanobot Agents
Automatically classifies tasks and routes them to free or paid models.
"""

import json
import os
import re
from typing import Tuple, Optional

class AutoRouter:
    """
    Automatic task classification and model routing.
    Routes routine tasks to free models, complex tasks to paid models.
    """
    
    # Task type keywords for classification
    TASK_KEYWORDS = {
        "code": [
            "write code", "python script", "javascript", "function", "debug",
            "fix code", "implement", "programming", "html", "css", "sql",
            "api", "json", "xml", "bash", "shell script", "batch"
        ],
        "draft": [
            "write", "draft", "compose", "create a", "email", "letter",
            "document", "article", "blog", "post", "message", "announcement"
        ],
        "summarize": [
            "summarize", "summary", "condense", "brief", "tldr", "tl;dr",
            "short version", "key points", "main ideas", "overview"
        ],
        "research": [
            "research", "find", "search", "lookup", "what is", "explain",
            "tell me about", "information on", "how does", "compare"
        ],
        "chat": [
            "hello", "hi", "hey", "how are you", "thanks", "thank you",
            "good morning", "good afternoon", "good evening", "chat"
        ],
        "complex": [
            "analyze", "reason", "decide", "evaluate", "assess", "critical",
            "security", "password", "api key", "financial", "legal", "medical"
        ]
    }
    
    # Free models for each task type
    FREE_MODELS = {
        "code": ["openrouter/free", "meta-llama/llama-3.3-70b-instruct:free"],
        "draft": ["openrouter/free", "arcee-ai/trinity-large-preview:free"],
        "summarize": ["openrouter/free", "google/gemini-2.0-flash-exp:free"],
        "research": ["openrouter/free", "stepfun/step-3.5-flash:free"],
        "chat": ["openrouter/free", "liquid/lfm-2.5-1.2b-instruct:free"],
        "complex": []  # Complex tasks use paid model
    }
    
    # Task types that should use free models
    FREE_TASK_TYPES = {"code", "draft", "summarize", "research"}
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize AutoRouter with optional custom config."""
        self.config = {}
        if config_path and os.path.exists(config_path):
            with open(config_path, "r") as f:
                self.config = json.load(f)
    
    def classify_task(self, text: str) -> str:
        """
        Classify a task into one of the predefined types.
        
        Args:
            text: The user message or task description
            
        Returns:
            Task type: code, draft, summarize, research, chat, or complex
        """
        text_lower = text.lower()
        
        # Score each task type based on keyword matches
        scores = {}
        for task_type, keywords in self.TASK_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw in text_lower)
            if score > 0:
                scores[task_type] = score
        
        # Return highest scoring type, or 'chat' as default
        if scores:
            return max(scores, key=scores.get)
        return "chat"
    
    def should_use_free(self, task_type: str, text: str = "") -> bool:
        """
        Determine if a task should be routed to a free model.
        
        Args:
            task_type: The classified task type
            text: Original text (for additional analysis)
            
        Returns:
            True if should use free model, False for paid model
        """
        # Security-sensitive keywords always use paid model
        security_keywords = ["password", "api key", "secret", "token", 
                           "credential", "auth", "login", "private"]
        text_lower = text.lower()
        if any(kw in text_lower for kw in security_keywords):
            return False
        
        # Check if task type is in free list
        return task_type in self.FREE_TASK_TYPES
    
    def get_free_model(self, task_type: str) -> str:
        """
        Get the best free model for a task type.
        
        Args:
            task_type: The classified task type
            
        Returns:
            Model identifier for OpenRouter
        """
        models = self.FREE_MODELS.get(task_type, [])
        return models[0] if models else "openrouter/free"
    
    def route(self, text: str) -> Tuple[str, str, bool]:
        """
        Main routing method - classify and determine routing.
        
        Args:
            text: The user message or task description
            
        Returns:
            Tuple of (task_type, model, use_free)
        """
        task_type = self.classify_task(text)
        use_free = self.should_use_free(task_type, text)
        model = self.get_free_model(task_type) if use_free else "paid"
        
        return task_type, model, use_free
    
    def get_routing_info(self, text: str) -> dict:
        """
        Get detailed routing information for logging/debugging.
        
        Args:
            text: The user message or task description
            
        Returns:
            Dictionary with routing details
        """
        task_type, model, use_free = self.route(text)
        return {
            "task_type": task_type,
            "model": model,
            "use_free": use_free,
            "reason": "routine_task" if use_free else "complex_or_sensitive"
        }


# Global router instance
_router = None

def get_router(config_path: Optional[str] = None) -> AutoRouter:
    """Get or create the global AutoRouter instance."""
    global _router
    if _router is None:
        _router = AutoRouter(config_path)
    return _router


def classify(text: str) -> str:
    """Quick classification helper."""
    return get_router().classify_task(text)


def should_route_free(text: str) -> bool:
    """Quick routing decision helper."""
    return get_router().should_use_free(get_router().classify_task(text), text)


def get_model_for_task(text: str) -> str:
    """Quick model selection helper."""
    router = get_router()
    task_type = router.classify_task(text)
    return router.get_free_model(task_type) if router.should_use_free(task_type, text) else "paid"


if __name__ == "__main__":
    # Demo/test
    router = AutoRouter()
    
    test_messages = [
        "Write a Python function to sort a list",
        "Summarize this article about climate change",
        "Draft an email to my boss",
        "Hello, how are you?",
        "Analyze the security implications of this code",
        "Research the history of ancient Rome"
    ]
    
    print("=" * 60)
    print("AutoRouter Test Results")
    print("=" * 60)
    
    for msg in test_messages:
        task_type, model, use_free = router.route(msg)
        print(f"\nMessage: {msg[:50]}...")
        print(f"  Type: {task_type}")
        print(f"  Model: {model}")
        print(f"  Free: {use_free}")
