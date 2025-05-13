"""
Agents package.

This package exports all agent instances used in the application, but distinguishes
between standalone agents and team/workflow-specific agents.
"""

# =========================================================
# Standalone agents - directly exposed in the playground UI
# =========================================================
from .generic import web_agent, finance_agent

# ======================================================
# Team/workflow-specific agents - not directly exposed
# ======================================================

# Content agents - used by the Content Team
from .content.strategist import content_strategist
from .content.writer import content_writer
from .content.seo import seo_specialist
from .content.social import social_media_manager

# Marketing agents - used by the Marketing Team
from .marketing.strategist import marketing_strategist
from .marketing.researcher import market_researcher

# Export only standalone agents to be directly exposed in the playground
__all__ = [
    # Standalone agents
    "web_agent",
    "finance_agent",
]

# These are explicitly NOT included in __all__ since they shouldn't be imported directly by app.py
# They're still imported here to make them available to teams and workflows
# 
# Content agents: content_strategist, content_writer, seo_specialist, social_media_manager
# Marketing agents: marketing_strategist, market_researcher