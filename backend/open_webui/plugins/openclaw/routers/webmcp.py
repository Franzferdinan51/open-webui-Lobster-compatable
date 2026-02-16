from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ToolParam(BaseModel):
    name: str
    type: str
    description: str = ""

class Tool(BaseModel):
    name: str
    description: str
    parameters: dict = {}

# WebMCP Tools exposed by OpenWebUI
WEBMCP_TOOLS = [
    Tool(
        name="list_models",
        description="List all available AI models",
        parameters={
            "type": "object",
            "properties": {}
        }
    ),
    Tool(
        name="list_chats",
        description="List all chats",
        parameters={
            "type": "object", 
            "properties": {}
        }
    ),
    Tool(
        name="create_chat",
        description="Create a new chat",
        parameters={
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Chat title"},
                "model_id": {"type": "string", "description": "Model ID to use"}
            }
        }
    ),
    Tool(
        name="send_message",
        description="Send a message in a chat",
        parameters={
            "type": "object",
            "properties": {
                "chat_id": {"type": "string", "description": "Chat ID"},
                "content": {"type": "string", "description": "Message content"}
            }
        }
    ),
    Tool(
        name="get_config",
        description="Get OpenWebUI configuration",
        parameters={
            "type": "object",
            "properties": {}
        }
    ),
    Tool(
        name="health_check",
        description="Check if OpenWebUI is running",
        parameters={
            "type": "object",
            "properties": {}
        }
    )
]

@router.get("/webmcp/tools")
async def get_webmcp_tools():
    """Return WebMCP tool definitions for AI agents"""
    return {
        "version": "1.0",
        "tools": [
            {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.parameters
            }
            for tool in WEBMCP_TOOLS
        ]
    }

@router.get("/webmcp/health")
async def webmcp_health():
    """WebMCP health check endpoint"""
    return {
        "status": "healthy",
        "service": "OpenWebUI Lobster Edition",
        "version": "1.0.0"
    }
