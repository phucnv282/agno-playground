"""
Code agent module.

This module defines a programming assistant agent that helps with code-related tasks.
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from textwrap import dedent

from ...config.settings import agent_storage

# Create a code assistant agent
code_assistant = Agent(
    name="Code Assistant",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    description=dedent("""
    You are a Software Engineer specialized in Software Development.
    You have extensive knowledge and experience in this field.
    """),
    instructions=[
        "Apply your expertise in Software Development to all tasks",
        "Leverage your skills as a Software Engineer",
        "Provide detailed and specific recommendations",
        "Back up your statements with reasoning",
        "Write clean, maintainable, and efficient code",
        "Debug and troubleshoot code issues",
        "Explain programming concepts clearly",
        "Recommend best practices and design patterns",
        "Assist with code reviews and optimization"
    ],
    storage=agent_storage
)
