"""
OpenClaw Compatibility Layer

This module provides compatibility between OpenWebUI and OpenClaw,
routing API calls through the OpenClaw gateway when configured.
"""

import os
import logging
from typing import Optional, Dict, Any, List

log = logging.getLogger(__name__)

# Configuration
OPENCLAW_ENABLED = os.environ.get("OPENCLAW_ENABLED", "true").lower() == "true"
OPENCLAW_GATEWAY_URL = os.environ.get("OPENCLAW_GATEWAY_URL", "http://localhost:18789")
OPENCLAW_GATEWAY_KEY = os.environ.get("OPENCLAW_GATEWAY_KEY", "")

# Model provider mappings
PROVIDER_MAPPINGS = {
    # OpenAI-compatible models
    "gpt-4": "openai",
    "gpt-4-turbo": "openai",
    "gpt-4o": "openai",
    "gpt-3.5-turbo": "openai",
    "gpt-4o-mini": "openai",
    # Anthropic
    "claude-3-opus": "anthropic",
    "claude-3-sonnet": "anthropic",
    "claude-3-5-sonnet": "anthropic",
    "claude-3-haiku": "anthropic",
    # Google
    "gemini-pro": "google",
    "gemini-1.5-pro": "google",
    "gemini-flash": "google",
    # xAI
    "grok-beta": "xai",
    "grok-2": "xai",
    # Mistral
    "mistral-large": "mistral",
    "mistral-small": "mistral",
    # Cohere
    "command-r": "cohere",
    "command-r-plus": "cohere",
}


def get_provider_for_model(model: str) -> str:
    """Get the provider name for a given model"""
    model_lower = model.lower()
    for model_prefix, provider in PROVIDER_MAPPINGS.items():
        if model_prefix in model_lower:
            return provider
    return "openai"  # Default


def is_openclaw_enabled() -> bool:
    """Check if OpenClaw integration is enabled"""
    return OPENCLAW_ENABLED


def get_gateway_url() -> str:
    """Get the OpenClaw gateway URL"""
    return OPENCLAW_GATEWAY_URL


def get_gateway_key() -> str:
    """Get the OpenClaw gateway API key"""
    return OPENCLAW_GATEWAY_KEY


def get_model_url(model: str) -> str:
    """Get the appropriate URL for a model"""
    provider = get_provider_for_model(model)
    
    # If OpenClaw is enabled, route through gateway
    if OPENCLAW_ENABLED:
        return f"{OPENCLAW_GATEWAY_URL}/v1"
    
    # Otherwise use default endpoints
    if provider == "openai":
        return "https://api.openai.com/v1"
    elif provider == "anthropic":
        return "https://api.anthropic.com/v1"
    elif provider == "google":
        return "https://generativelanguage.googleapis.com/v1"
    elif provider == "xai":
        return "https://api.x.ai/v1"
    elif provider == "mistral":
        return "https://api.mistral.ai/v1"
    elif provider == "cohere":
        return "https://api.cohere.ai/v1"
    else:
        return "https://api.openai.com/v1"


def get_headers(api_key: str = None) -> Dict[str, str]:
    """Get headers for API requests"""
    headers = {}
    
    # Use OpenClaw key if enabled, otherwise use provided key
    key = OPENCLAW_GATEWAY_KEY or api_key or ""
    
    if key:
        headers["Authorization"] = f"Bearer {key}"
    
    return headers


def get_openai_compatible_headers() -> Dict[str, str]:
    """Get headers for OpenAI-compatible API calls"""
    headers = {}
    
    if OPENCLAW_GATEWAY_KEY:
        headers["Authorization"] = f"Bearer {OPENCLAW_GATEWAY_KEY}"
    elif OPENCLAW_ENABLED:
        # Use default OpenClaw auth
        headers["Authorization"] = f"Bearer {OPENCLAW_GATEWAY_KEY}"
    
    return headers


def should_route_through_openclaw(model: str) -> bool:
    """Determine if a model request should be routed through OpenClaw"""
    if not OPENCLAW_ENABLED:
        return False
    
    # Route all models through OpenClaw when enabled
    return True


def get_chat_completion_url() -> str:
    """Get the chat completion endpoint URL"""
    if OPENCLAW_ENABLED:
        return f"{OPENCLAW_GATEWAY_URL}/v1/chat/completions"
    return "https://api.openai.com/v1/chat/completions"


def get_models_url() -> str:
    """Get the models list endpoint URL"""
    if OPENCLAW_ENABLED:
        return f"{OPENCLAW_GATEWAY_URL}/v1/models"
    return "https://api.openai.com/v1/models"


def get_embeddings_url() -> str:
    """Get the embeddings endpoint URL"""
    if OPENCLAW_ENABLED:
        return f"{OPENCLAW_GATEWAY_URL}/v1/embeddings"
    return "https://api.openai.com/v1/embeddings"


def get_images_url() -> str:
    """Get the images generation endpoint URL"""
    if OPENCLAW_ENABLED:
        return f"{OPENCLAW_GATEWAY_URL}/v1/images/generations"
    return "https://api.openai.com/v1/images/generations"


def get_audio_url() -> str:
    """Get the audio endpoint URL"""
    if OPENCLAW_ENABLED:
        return f"{OPENCLAW_GATEWAY_URL}/v1/audio"
    return "https://api.openai.com/v1/audio"


# Export compatibility functions
__all__ = [
    "is_openclaw_enabled",
    "get_gateway_url",
    "get_gateway_key",
    "get_model_url",
    "get_provider_for_model",
    "get_headers",
    "get_openai_compatible_headers",
    "should_route_through_openclaw",
    "get_chat_completion_url",
    "get_models_url",
    "get_embeddings_url",
    "get_images_url",
    "get_audio_url",
    "PROVIDER_MAPPINGS",
]
