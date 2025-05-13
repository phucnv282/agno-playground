"""
Content team module.

Defines the content team composed of content-focused agents working together.
"""

from textwrap import dedent

from agno.storage.sqlite import SqliteStorage
from agno.team import Team

from ..agents.content import (
    content_strategist, 
    content_writer, 
    seo_specialist, 
    social_media_manager
)
from ..config.settings import agent_storage

content_team = Team(
    name="Content Team",
    description=dedent("""\
    A specialized team of content professionals who collaborate to create, 
    optimize, and distribute high-quality content across various channels.
    """),
    members=[
        content_strategist,
        content_writer,
        social_media_manager,
        seo_specialist
    ],
    instructions=[
        "Collaboratively develop content that aligns with business goals",
        "Ensure consistent messaging and brand voice across all content",
        "Optimize content for both user experience and search engines",
        "Create content that drives engagement and conversions",
        "Adapt content strategies based on performance data"
    ],
    storage=SqliteStorage(table_name="content_team", db_file=agent_storage),
)
