"""
Marketing strategist agent module.
Defines the marketing strategist agent for developing marketing strategies.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

from ...config.settings import agent_storage

marketing_strategist = Agent(
    name="Marketing Strategist",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    description="You are a marketing strategist who develops comprehensive marketing plans.",
    instructions=[
        "Develop integrated marketing strategies",
        "Align marketing initiatives with business objectives",
        "Identify target audience segments and personas",
        "Analyze market trends and competitor activities",
        "Propose channel-specific tactics and campaigns"
    ],
    storage=SqliteStorage(table_name="marketing_strategist", db_file=agent_storage),
    markdown=True,
)
