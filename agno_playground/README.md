# Agno Playground Application

This repository contains a modular Agno application demonstrating best practices for organizing agents, teams, and workflows.

## Directory Structure

```
agno_playground/
├── agents/                   # All agent definitions
│   ├── __init__.py           # Exports agent instances
│   ├── generic.py            # Generic multi-purpose agents
│   ├── content/              # Content-related agents
│   │   ├── __init__.py
│   │   ├── strategist.py
│   │   ├── writer.py
│   │   ├── seo.py
│   │   └── social.py
│   ├── marketing/            # Marketing-related agents
│   │   ├── __init__.py
│   │   ├── strategist.py
│   │   └── researcher.py
├── teams/                    # Team definitions
│   ├── __init__.py
│   ├── content.py
│   └── marketing.py
├── workflows/                # Workflow definitions
│   ├── __init__.py
│   └── blog.py
├── config/                   # Configuration
│   ├── __init__.py
│   └── settings.py
└── app.py                    # Main application entry point
```

## Agent Categories

1. **Generic Agents**: General-purpose agents like web search and finance agents
2. **Content Agents**: Specialists in content strategy, writing, SEO, and social media
3. **Marketing Agents**: Experts in marketing strategy and market research

## Teams

1. **Content Team**: Collaborates to create high-quality content
2. **Marketing Team**: Works together on marketing strategies and campaigns

## Workflows

1. **Blog Workflow**: Orchestrates multiple agents to create complete blog posts

## Getting Started

To run the application:

```bash
cd /path/to/workspace/agno
source .venv/bin/activate  # Activate the virtual environment
python main.py
```

The application will be accessible at http://localhost:7777.

## Best Practices

- Keep agent definitions modular and focused on a single responsibility
- Group related agents in domain-specific packages
- Use relative imports within the package
- Define clear interfaces between components
- Define teams in a separate package
- Define workflows in a separate package
- Keep configuration centralized
