"""
Main application module for the Agno playground.

This module creates and configures the Playground application with agents, teams,
and workflows defined in the respective packages.
"""

from agno.playground import Playground

# Import agents
from .agents import finance_agent, web_agent

# Import workflows and extract blog agents
from .workflows import blog_workflow

# Import teams
from .teams import content_team, marketing_team

# Get individual agents from the blog workflow to expose them in the playground
blog_agents = [
    blog_workflow.topic_researcher,
    blog_workflow.content_planner,
    blog_workflow.research_assistant,
    blog_workflow.blog_writer,
    blog_workflow.editor,
    blog_workflow.publisher
]

# Create and configure the Playground application
app = Playground(
    agents=[web_agent, finance_agent] + blog_agents,
    teams=[content_team, marketing_team],
    workflows=[blog_workflow]
).get_app()
