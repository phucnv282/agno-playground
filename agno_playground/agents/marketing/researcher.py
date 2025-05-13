"""
Market researcher agent module.
Defines the market researcher agent for gathering and analyzing market intelligence.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools

from ...config.settings import agent_storage

market_researcher = Agent(
    name="Market Researcher",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    description="You are a market researcher who gathers and analyzes market intelligence.",
    instructions=[
        "Research industry trends and market developments",
        "Analyze competitor strategies and positioning",
        "Identify customer needs and pain points",
        "Gather relevant statistics and data points",
        "Provide actionable insights from research findings"
    ],
    storage=SqliteStorage(table_name="market_researcher", db_file=agent_storage),
    markdown=True,
)
