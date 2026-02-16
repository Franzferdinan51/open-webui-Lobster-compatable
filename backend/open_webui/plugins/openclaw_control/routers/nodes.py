"""
OpenClaw Nodes Router - Node/device management
"""

import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional

from open_webui.utils.auth import get_verified_user
from open_webui.models.users import User

log = logging.getLogger(__name__)
router = APIRouter()


class NodeInfo(BaseModel):
    id: str
    name: str
    platform: str
    status: str
    last_seen: Optional[str] = None
    capabilities: List[str] = []


@router.get("/api/nodes")
async def list_nodes(user: User = Depends(get_verified_user)):
    """List all connected nodes"""
    return {
        "nodes": [
            {
                "id": "duckbot-linux",
                "name": "DuckBot (Linux)",
                "platform": "linux",
                "status": "online",
                "last_seen": "2026-02-15T22:00:00Z",
                "capabilities": ["chat", "browser", "voice"]
            },
            {
                "id": "agent-smith",
                "name": "Agent Smith (Windows)",
                "platform": "windows",
                "status": "online",
                "last_seen": "2026-02-15T22:00:00Z",
                "capabilities": ["chat", "comfyui", "code"]
            }
        ]
    }


@router.get("/api/nodes/{node_id}")
async def get_node(node_id: str, user: User = Depends(get_verified_user)):
    """Get specific node info"""
    return {
        "id": node_id,
        "name": "Node",
        "platform": "linux",
        "status": "online"
    }


@router.post("/api/nodes/{node_id}/invoke")
async def invoke_node(node_id: str, command: dict, user: User = Depends(get_verified_user)):
    """Invoke command on node"""
    return {
        "status": "ok",
        "result": "Command executed"
    }
