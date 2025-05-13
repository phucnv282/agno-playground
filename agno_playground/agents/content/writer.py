"""
Content writer agent module.
Defines the content writer agent for creating various types of content.
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage

from ...config.settings import agent_storage

content_writer = Agent(
    name="Content Writer",
    model=OpenAIChat(id="gpt-4o"),
    description=dedent("""\
    You are a versatile content writer who creates engaging, clear, and effective content
    across various formats and for different audience segments.
    """),
    instructions=[
        "Write clear, concise, and engaging content",
        "Adapt tone and style to different audiences",
        "Create content that drives action",
        "Incorporate SEO best practices",
        "Ensure factual accuracy and proper citations"
    ],
    storage=SqliteStorage(table_name="content_writer", db_file=agent_storage),
    markdown=True,
)
