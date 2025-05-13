"""
Agents package.

This package exports all agent instances used in the application.
"""

# Generic agents
from .generic import web_agent, finance_agent

# Content agents
from .content.strategist import content_strategist
from .content.writer import content_writer
from .content.seo import seo_specialist
from .content.social import social_media_manager

# Marketing agents
from .marketing.strategist import marketing_strategist
from .marketing.researcher import market_researcher

__all__ = [
    # Generic agents
    "web_agent",
    "finance_agent",
    
    # Content agents
    "content_strategist",
    "content_writer",
    "seo_specialist",
    "social_media_manager",
    
    # Marketing agents
    "marketing_strategist",
    "market_researcher",
]