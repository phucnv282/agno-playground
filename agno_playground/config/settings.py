"""
Application settings for the Agno playground application.
Contains configuration variables and paths used throughout the application.
"""

from pathlib import Path

# Path to agent storage database
agent_storage: str = "tmp/agents.db"

# Base directory (optional, for future expansion)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
