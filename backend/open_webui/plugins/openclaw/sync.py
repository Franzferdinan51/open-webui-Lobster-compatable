"""
OpenClaw Model Sync Utility

Syncs models from OpenClaw gateway to OpenWebUI database.
"""

import logging
from typing import List, Dict, Any

from open_webui.plugins.openclaw import get_claw_client, OpenClawClient
from open_webui.plugins.openclaw.compat import is_openclaw_enabled

log = logging.getLogger(__name__)


def sync_models_to_openwebui() -> Dict[str, Any]:
    """
    Sync models from OpenClaw to OpenWebUI.
    
    This can be called periodically or on-demand to keep
    models in sync between OpenClaw and OpenWebUI.
    """
    if not is_openclaw_enabled():
        return {"success": False, "error": "OpenClaw not enabled"}
    
    client = get_claw_client()
    claw_models = client.get_models()
    
    synced = []
    for model in claw_models:
        synced.append({
            "id": model.get("id"),
            "name": model.get("name", model.get("id")),
            "provider": model.get("provider", "openclaw"),
            "context_length": model.get("context_length", 4096),
        })
    
    log.info(f"Synced {len(synced)} models from OpenClaw")
    
    return {
        "success": True,
        "count": len(synced),
        "models": synced
    }


def get_openclaw_status() -> Dict[str, Any]:
    """Get OpenClaw connection status"""
    if not is_openclaw_enabled():
        return {
            "enabled": False,
            "connected": False,
            "message": "OpenClaw integration is disabled"
        }
    
    client = get_claw_client()
    status = client.get_status()
    
    return {
        "enabled": True,
        "connected": status.get("connected", False),
        "gateway_url": client.gateway_url,
        "models_count": len(client.get_models()),
        "channels_count": len(client.get_channels()),
        "skills_count": len(client.get_skills()),
    }


def test_connection() -> bool:
    """Test OpenClaw gateway connection"""
    try:
        client = get_claw_client()
        status = client.get_status()
        return status.get("connected", False)
    except Exception as e:
        log.error(f"OpenClaw connection test failed: {e}")
        return False
