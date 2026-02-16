"""
OpenClaw Middleware - Routes API requests through OpenClaw gateway

This middleware intercepts OpenWebUI API calls and routes them through
OpenClaw when enabled, providing seamless integration.
"""

import logging
from typing import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from open_webui.plugins.openclaw.compat import (
    is_openclaw_enabled,
    should_route_through_openclaw,
    get_chat_completion_url,
    get_models_url,
)

log = logging.getLogger(__name__)


class OpenClawMiddleware(BaseHTTPMiddleware):
    """
    Middleware to route API requests through OpenClaw gateway.
    
    When OpenClaw is enabled, all chat completion, model, and other
    API calls are routed through the OpenClaw gateway.
    """
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Skip if OpenClaw is not enabled
        if not is_openclaw_enabled():
            return await call_next(request)
        
        # Get the path
        path = request.url.path
        
        # Route specific endpoints through OpenClaw
        if should_route_request(path):
            log.info(f"Routing request through OpenClaw: {path}")
            # The actual routing is handled by the routers
            # This middleware just logs the routing
        
        return await call_next(request)


def should_route_request(path: str) -> bool:
    """Determine if a path should be routed through OpenClaw"""
    routes = [
        "/v1/chat/completions",
        "/v1/models",
        "/v1/embeddings",
        "/v1/images",
        "/v1/audio",
        "/ollama",
        "/openai",
    ]
    
    return any(path.startswith(route) for route in routes)
