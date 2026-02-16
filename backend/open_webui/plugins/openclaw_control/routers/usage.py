"""
OpenClaw Usage Router - Usage metrics and analytics
"""

import logging
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, timedelta

from open_webui.utils.auth import get_verified_user
from open_webui.models.users import User

log = logging.getLogger(__name__)
router = APIRouter()


@router.get("/api/usage")
async def get_usage(
    period: str = Query("day", regex="^(day|week|month|year)$"),
    user: User = Depends(get_verified_user)
):
    """Get usage metrics"""
    return {
        "period": period,
        "total_requests": 1250,
        "total_tokens": 450000,
        "total_cost": 0.00,
        "by_model": {
            "minimax-portal/MiniMax-M2.5": {
                "requests": 800,
                "tokens": 350000
            },
            "lmstudio/qwen3-coder-next": {
                "requests": 450,
                "tokens": 100000
            }
        },
        "by_channel": {
            "telegram": 600,
            "whatsapp": 300,
            "discord": 200,
            "direct": 150
        }
    }


@router.get("/api/usage/overview")
async def get_usage_overview(user: User = Depends(get_verified_user)):
    """Get usage overview"""
    return {
        "total_requests_today": 150,
        "total_tokens_today": 55000,
        "active_sessions": 3,
        "active_agents": 2,
        "uptime": "24h"
    }


@router.get("/api/usage/models")
async def get_model_usage(user: User = Depends(get_verified_user)):
    """Get per-model usage"""
    return {
        "models": [
            {
                "id": "minimax-portal/MiniMax-M2.5",
                "name": "MiniMax M2.5",
                "requests": 800,
                "tokens": 350000,
                "percentage": 64
            },
            {
                "id": "lmstudio/qwen3-coder-next", 
                "name": "Qwen3 Coder",
                "requests": 450,
                "tokens": 100000,
                "percentage": 36
            }
        ]
    }
