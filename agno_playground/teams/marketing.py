"""
Marketing team module.

Defines the marketing team composed of marketing-focused agents working together.
"""

from agno.storage.sqlite import SqliteStorage
from agno.team import Team

from ..agents.content import social_media_manager, seo_specialist
from ..agents.marketing import marketing_strategist, market_researcher
from ..config.settings import agent_storage

marketing_team = Team(
    name="Marketing Team",
    description="A collaborative team of marketing professionals who develop and execute marketing strategies.",
    members=[
        marketing_strategist,
        market_researcher,
        social_media_manager,  # Reusing from Content Team
        seo_specialist,  # Reusing from Content Team
    ],
    instructions=[
        "Develop marketing strategies aligned with business goals",
        "Create data-driven marketing campaigns",
        "Ensure consistent brand messaging across all channels",
        "Optimize marketing activities for maximum ROI",
        "Adapt strategies based on market feedback and performance"
    ],
    storage=SqliteStorage(table_name="marketing_team", db_file=agent_storage),
)
