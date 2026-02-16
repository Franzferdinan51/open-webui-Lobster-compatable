"""
OpenClaw Logs Router - Log viewing
"""

import logging
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from open_webui.utils.auth import get_verified_user
from open_webui.models.users import User

log = logging.getLogger(__name__)
router = APIRouter()


class LogEntry(BaseModel):
    timestamp: str
    level: str
    source: str
    message: str


@router.get("/api/logs")
async def get_logs(
    limit: int = Query(100, le=1000),
    level: Optional[str] = None,
    source: Optional[str] = None,
    user: User = Depends(get_verified_user)
):
    """Get logs with optional filtering"""
    # Return sample logs
    logs = [
        {
            "timestamp": datetime.now().isoformat(),
            "level": "info",
            "source": "gateway",
            "message": "Gateway started"
        },
        {
            "timestamp": datetime.now().isoformat(),
            "level": "info",
            "source": "channel:telegram",
            "message": "Telegram channel connected"
        }
    ]
    
    if level:
        logs = [l for l in logs if l["level"] == level]
    if source:
        logs = [l for l in logs if source in l["source"]]
    
    return {"logs": logs[:limit]}


@router.get("/api/logs/sources")
async def get_log_sources(user: User = Depends(get_verified_user)):
    """Get available log sources"""
    return {
        "sources": ["gateway", "channel:telegram", "channel:discord", "agent", "tools", "scheduler"]
    }
