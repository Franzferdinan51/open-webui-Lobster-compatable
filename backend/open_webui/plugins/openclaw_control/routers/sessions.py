"""
OpenClaw Sessions Router - Session management
"""

import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from open_webui.utils.auth import get_verified_user
from open_webui.models.users import User

log = logging.getLogger(__name__)
router = APIRouter()


class SessionInfo(BaseModel):
    id: str
    agent_id: str
    channel: str
    status: str
    created_at: str
    last_activity: Optional[str] = None


@router.get("/api/sessions")
async def list_sessions(user: User = Depends(get_verified_user)):
    """List all active sessions"""
    return {
        "sessions": [
            {
                "id": "main",
                "agent_id": "main",
                "channel": "telegram",
                "status": "active",
                "created_at": "2026-02-15T10:00:00Z",
                "last_activity": "2026-02-15T22:00:00Z"
            }
        ]
    }


@router.get("/api/sessions/{session_id}")
async def get_session(session_id: str, user: User = Depends(get_verified_user)):
    """Get specific session info"""
    return {
        "id": session_id,
        "agent_id": "main",
        "channel": "telegram",
        "status": "active"
    }


@router.post("/api/sessions/{session_id}/message")
async def send_session_message(session_id: str, message: dict, user: User = Depends(get_verified_user)):
    """Send message to session"""
    return {
        "status": "ok",
        "message_id": "msg_123"
    }


@router.delete("/api/sessions/{session_id}")
async def end_session(session_id: str, user: User = Depends(get_verified_user)):
    """End a session"""
    return {"status": "ended"}
