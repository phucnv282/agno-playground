"""
SEO specialist agent module.
Defines the SEO specialist agent for optimizing content for search engines.
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

from ...config.settings import agent_storage

seo_specialist = Agent(
    name="SEO Specialist",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    description=dedent("""\
    You are an SEO specialist who optimizes content to improve search engine 
    visibility while maintaining quality and user experience.
    """),
    instructions=[
        "Research relevant keywords and search intent",
        "Optimize title tags, meta descriptions, and headers",
        "Suggest internal and external linking strategies",
        "Balance SEO best practices with user experience",
        "Analyze competitor content for SEO opportunities"
    ],
    storage=SqliteStorage(table_name="seo_specialist", db_file=agent_storage),
    markdown=True,
)
