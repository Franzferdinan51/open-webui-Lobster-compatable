#!/bin/bash
# OpenWebUI Lobster Edition - Start with integrations

cd "$(dirname "$0")"

# Activate virtual environment
source .venv/bin/activate

# OpenClaw Gateway Configuration
export OPENCLAW_GATEWAY_URL="http://100.106.80.61:18789"
export OPENCLAW_GATEWAY_KEY=""
export OPENCLAW_ENABLED="true"

# Agent Mesh Configuration
export AGENT_MESH_URL="http://100.74.88.40:4000"
export AGENT_MESH_KEY="openclaw-mesh-default-key"
export AGENT_MESH_ENABLED="true"

# LM Studio Configuration (OpenAI compatible)
export OPENAI_API_BASE_URLS="http://localhost:1234/v1"
export OPENAI_API_KEYS="lm-studio"

# Start OpenWebUI
echo "Starting OpenWebUI Lobster Edition..."
echo "  OpenClaw: $OPENCLAW_GATEWAY_URL"
echo "  Agent Mesh: $AGENT_MESH_URL"
echo "  LM Studio: $OPENAI_API_BASE_URLS"

python -m uvicorn open_webui.main:app --host 0.0.0.0 --port 8080
