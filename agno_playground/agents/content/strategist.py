"""
Content strategist agent module.
Defines the content strategist agent for developing content strategies.
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

from ...config.settings import agent_storage

content_strategist = Agent(
    name="Content Strategist",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    description=dedent("""\
    You are a content strategist who excels at developing content strategies 
    and identifying content opportunities that align with business goals.
    """),
    instructions=[
        "Analyze trends and audience preferences",
        "Develop comprehensive content strategies",
        "Identify content gaps and opportunities",
        "Prioritize content types based on business goals",
        "Consider SEO and marketing alignment"
    ],
    storage=SqliteStorage(table_name="content_strategist", db_file=agent_storage),
    markdown=True,
)
