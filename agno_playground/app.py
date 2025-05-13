"""
Main application module for the Agno playground.

This module creates and configures the Playground application with agents, teams,
and workflows defined in the respective packages.
"""

from agno.playground import Playground

# Import standalone agents - these agents will be directly exposed in the playground
from .agents import finance_agent, web_agent

# Import workflows
from .workflows import blog_workflow

# Import teams
from .teams import content_team, marketing_team

# Only include standalone agents in the playground
# We've decided NOT to expose workflow-specific agents directly in the playground
standalone_agents = [
    web_agent,      # General-purpose web agent
    finance_agent,  # General-purpose finance agent
    # We're excluding blog workflow agents as they're meant to be used within the workflow
]

# Create and configure the Playground application
app = Playground(
    agents=standalone_agents,  # Only expose standalone agents
    teams=[content_team, marketing_team],
    workflows=[blog_workflow]
).get_app()
