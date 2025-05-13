"""
Social media manager agent module.
Defines the social media manager agent for creating and managing social media content.
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

from ...config.settings import agent_storage

social_media_manager = Agent(
    name="Social Media Manager",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    description=dedent("""\
    You are a social media expert who creates platform-optimized content
    and develops strategies to engage audiences across social channels.
    """),
    instructions=[
        "Create platform-specific content formats",
        "Optimize content for each social platform",
        "Incorporate trending topics and hashtags",
        "Craft engaging captions and CTAs",
        "Consider timing and audience engagement patterns"
    ],
    storage=SqliteStorage(table_name="social_media_manager", db_file=agent_storage),
    markdown=True,
)
