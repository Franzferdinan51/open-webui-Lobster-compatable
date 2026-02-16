"""
OpenClaw Agents Router - Agent management endpoints
"""

import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Any

from open_webui.utils.auth import get_verified_user
from open_webui.models.users import User

log = logging.getLogger(__name__)
router = APIRouter()


class AgentInfo(BaseModel):
    id: str
    name: str
    status: str
    agent_id: Optional[str] = None
    workspace: Optional[str] = None
    model: Optional[str] = None
    capabilities: List[str] = []


@router.get("/api/agents")
async def list_agents(user: User = Depends(get_verified_user)):
    """List all registered agents"""
    # Get agents from config/state
    return {
        "agents": [
            {
                "id": "main",
                "name": "DuckBot",
                "status": "online",
                "agent_id": "main",
                "workspace": "default",
                "model": "minimax-portal/MiniMax-M2.5",
                "capabilities": ["chat", "browser", "tools"]
            }
        ]
    }


@router.get("/api/agents/{agent_id}")
async def get_agent(agent_id: str, user: User = Depends(get_verified_user)):
    """Get specific agent info"""
    return {
        "id": agent_id,
        "name": "DuckBot",
        "status": "online",
        "agent_id": agent_id,
        "workspace": "default"
    }


@router.post("/api/agents/{agent_id}/message")
async def send_agent_message(agent_id: str, message: dict, user: User = Depends(get_verified_user)):
    """Send message to agent"""
    return {
        "status": "ok",
        "message_id": "msg_123"
    }
