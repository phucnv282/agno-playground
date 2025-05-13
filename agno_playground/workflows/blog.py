"""
Blog workflow module.

This module defines the BlogPostGenerator workflow which orchestrates multiple agents
to generate well-researched and engaging blog posts.
"""

import json
from textwrap import dedent
from typing import Dict, Iterator, Optional

from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
# Temporarily commenting out FilesystemTools as it might not be available in your version
# from agno.tools.filesystem import FilesystemTools
from agno.utils.log import logger
from agno.workflow import RunEvent, Workflow
from pydantic import BaseModel, Field

from ..config.settings import agent_storage


class BlogTopic(BaseModel):
    """Model representing a blog topic with title, summary, and keywords."""
    title: str = Field(..., description="Title of the blog topic.")
    summary: str = Field(..., description="Brief summary of the topic.")
    keywords: list[str] = Field(..., description="Relevant keywords for the topic.")


class BlogOutline(BaseModel):
    """Model representing a blog outline with sections and structure."""
    title: str = Field(..., description="Title of the blog post.")
    subtitle: Optional[str] = Field(None, description="Subtitle or tagline for the blog post.")
    sections: list[dict] = Field(
        ...,
        description="List of sections, each with a title and brief description of content."
    )
    target_word_count: int = Field(..., description="Target word count for the full blog post.")


class BlogReference(BaseModel):
    """Model representing a reference source for blog content."""
    title: str = Field(..., description="Title of the reference material.")
    url: Optional[str] = Field(None, description="URL of the reference, if available.")
    key_points: list[str] = Field(..., description="Key points from this reference to incorporate.")


class BlogPostGenerator(Workflow):
    """Workflow for generating well-researched and engaging blog posts."""

    description: str = dedent("""\
    An intelligent blog post generator that creates engaging, well-researched content.
    This workflow orchestrates multiple specialized agents to research, plan, write, 
    edit, and format compelling blog posts that are informative and optimized for readers.
    """)

    # Topic Research Agent: Finds trending and relevant topics
    topic_researcher = Agent(
        name="Topic Researcher",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGoTools()],
        description=dedent("""\
        You are a research specialist who identifies trending and relevant blog topics.
        Your expertise includes finding topics that are timely, interesting, and valuable to readers.
        """),
        instructions=[
            "Research trending topics in the requested domain",
            "Identify topics with good search volume and interest",
            "Provide supporting data when available",
            "Consider topics with a unique angle or perspective"
        ],
        storage=SqliteStorage(table_name="topic_researcher", db_file=agent_storage),
        response_model=BlogTopic,
        structured_outputs=True,
        markdown=True,
    )

    # Content Planner Agent: Creates outlines and plans content structure
    content_planner = Agent(
        name="Content Planner",
        model=OpenAIChat(id="gpt-4o"),
        description=dedent("""\
        You are a content planner who excels at structuring blog posts for maximum engagement.
        Your expertise includes creating logical flow, identifying key sections, and planning content structure.
        """),
        instructions=[
            "Create detailed and well-structured outlines",
            "Ensure a logical flow of information",
            "Include engaging section headings",
            "Plan for proper introduction and conclusion sections",
            "Consider SEO-friendly structure"
        ],
        storage=SqliteStorage(table_name="content_planner", db_file=agent_storage),
        response_model=BlogOutline,
        structured_outputs=True,
        markdown=True,
    )

    # Research Assistant Agent: Gathers supporting information and references
    research_assistant = Agent(
        name="Research Assistant",
        model=OpenAIChat(id="gpt-4o"),
        tools=[DuckDuckGoTools()],
        description=dedent("""\
        You are a detail-oriented research assistant who finds accurate information and references.
        Your expertise includes gathering supporting data, statistics, and expert opinions.
        """),
        instructions=[
            "Find accurate and relevant information for each section",
            "Gather statistics, examples, and expert quotes",
            "Identify credible sources for citations",
            "Look for unique insights not covered in common sources",
            "Verify information accuracy"
        ],
        storage=SqliteStorage(table_name="research_assistant", db_file=agent_storage),
        response_model=list[BlogReference],
        structured_outputs=True,
        markdown=True,
    )

    # Blog Writer Agent: Writes engaging and informative content
    blog_writer = Agent(
        name="Blog Writer",
        model=OpenAIChat(id="gpt-4o"),
        description=dedent("""\
        You are an expert blog writer who creates engaging, informative, and well-structured content.
        Your expertise includes crafting compelling narratives while incorporating research seamlessly.
        """),
        instructions=[
            "Write in a conversational but professional tone",
            "Include engaging examples and stories",
            "Create attention-grabbing headlines and subheadings",
            "Incorporate research and data naturally in the text",
            "Write for readability with appropriate paragraph length",
            "Include proper citations and attributions"
        ],
        storage=SqliteStorage(table_name="blog_writer", db_file=agent_storage),
        markdown=True,
    )

    # Editor Agent: Refines and polishes content
    editor = Agent(
        name="Editor",
        model=OpenAIChat(id="gpt-4o"),
        description=dedent("""\
        You are a meticulous editor who refines content for clarity, flow, and accuracy.
        Your expertise includes improving readability while maintaining the original voice.
        """),
        instructions=[
            "Check for grammar, spelling, and punctuation",
            "Improve clarity and flow of content",
            "Ensure consistent tone throughout",
            "Optimize for readability with appropriate formatting",
            "Verify all facts and citations",
            "Enhance transitions between sections"
        ],
        storage=SqliteStorage(table_name="editor", db_file=agent_storage),
        markdown=True,
    )

    # Publisher Agent: Formats and prepares content for publishing
    publisher = Agent(
        name="Publisher",
        model=OpenAIChat(id="gpt-4o"),
        # Temporarily commenting out FilesystemTools
        # tools=[FilesystemTools()],
        description=dedent("""\
        You are a publishing specialist who formats and prepares content for distribution.
        Your expertise includes creating properly formatted outputs ready for publishing.
        """),
        instructions=[
            "Format content with proper markdown",
            "Create appropriate metadata like title, description, and keywords",
            "Ensure images have alt text (if applicable)",
            "Prepare content for various platforms",
            "Save formatted content to the file system"
        ],
        storage=SqliteStorage(table_name="publisher", db_file=agent_storage),
        markdown=True,
    )

    def run(
        self,
        user_input: str,
        use_cached_result: bool = True,
    ) -> Iterator[RunResponse]:
        """
        Execute the blog post generation workflow.
        
        Args:
            user_input: User's topic or description for the blog post
            use_cached_result: Whether to use cached results if available
        """
        logger.info(f"Starting blog post generation workflow for: {user_input}")
        
        # Check cache first if enabled
        if use_cached_result:
            cached_blog_post = self.get_cached_blog_post(user_input)
            if cached_blog_post:
                logger.info(f"Using cached blog post for: {user_input}")
                yield RunResponse(
                    content=cached_blog_post,
                    event=RunEvent.workflow_completed
                )
                return

        # Step 1: Research topic and generate ideas
        yield RunResponse(
            content="Step 1/6: Researching blog topic...",
            event=RunEvent.workflow_step_started
        )
        
        topic_response = self.topic_researcher.run(
            f"Research and suggest a blog topic based on: {user_input}. "
            f"Provide a compelling title, brief summary, and relevant keywords."
        )
        
        if not topic_response or not isinstance(topic_response.content, BlogTopic):
            yield RunResponse(
                content="Failed to generate blog topic. Please try again.",
                event=RunEvent.workflow_completed
            )
            return
        
        topic = topic_response.content
        logger.info(f"Generated blog topic: {topic.title}")
        
        # Step 2: Create detailed outline
        yield RunResponse(
            content="Step 2/6: Creating blog outline...",
            event=RunEvent.workflow_step_started
        )
        
        outline_response = self.content_planner.run(
            f"Create a detailed outline for a blog post titled '{topic.title}' "
            f"about {topic.summary}. Include engaging section headings and brief "
            f"descriptions of what each section should cover."
        )
        
        if not outline_response or not isinstance(outline_response.content, BlogOutline):
            yield RunResponse(
                content="Failed to create blog outline. Please try again.",
                event=RunEvent.workflow_completed
            )
            return
        
        outline = outline_response.content
        logger.info(f"Created blog outline with {len(outline.sections)} sections")
        
        # Step 3: Gather supporting research
        yield RunResponse(
            content="Step 3/6: Gathering supporting research...",
            event=RunEvent.workflow_step_started
        )
        
        # Prepare section descriptions for research
        section_descriptions = "\n".join([
            f"- {section.get('title')}: {section.get('description')}"
            for section in outline.sections
        ])
        
        research_response = self.research_assistant.run(
            f"Find supporting information, statistics, and expert opinions for a blog post "
            f"titled '{outline.title}' with the following sections:\n\n{section_descriptions}\n\n"
            f"For each section, provide at least 2-3 key points with relevant facts, statistics, "
            f"or expert opinions that can be incorporated into the content."
        )
        
        if not research_response or not isinstance(research_response.content, list):
            yield RunResponse(
                content="Failed to gather research. Continuing with limited references.",
                event=RunEvent.workflow_step_completed
            )
            references = []
        else:
            references = research_response.content
            logger.info(f"Gathered {len(references)} research references")
        
        # Step 4: Write the blog post draft
        yield RunResponse(
            content="Step 4/6: Writing blog post draft...",
            event=RunEvent.workflow_step_started
        )
        
        # Prepare the input for the writer
        writer_input = {
            "title": outline.title,
            "subtitle": outline.subtitle,
            "target_word_count": outline.target_word_count,
            "outline": outline.sections,
            "references": [ref.model_dump() for ref in references] if references else [],
            "keywords": topic.keywords
        }
        
        draft_response = self.blog_writer.run(
            f"Write a comprehensive blog post based on the following outline and research:\n\n"
            f"{json.dumps(writer_input, indent=2)}\n\n"
            f"Write an engaging, informative post that follows the outline structure. "
            f"Incorporate the provided research points naturally. "
            f"Target word count: {outline.target_word_count} words."
        )
        
        if not draft_response or not draft_response.content:
            yield RunResponse(
                content="Failed to write blog draft. Please try again.",
                event=RunEvent.workflow_completed
            )
            return
        
        draft_content = draft_response.content
        logger.info(f"Created blog draft with approximately {len(draft_content.split())} words")
        
        # Step 5: Edit and refine the content
        yield RunResponse(
            content="Step 5/6: Editing and refining content...",
            event=RunEvent.workflow_step_started
        )
        
        edit_response = self.editor.run(
            f"Edit and refine the following blog post draft:\n\n"
            f"{draft_content}\n\n"
            f"Improve clarity, fix any grammar issues, ensure consistent tone, "
            f"and enhance readability. Maintain the original voice while making "
            f"the content more engaging and professional."
        )
        
        if not edit_response or not edit_response.content:
            logger.warning("Editing failed, using unedited draft")
            edited_content = draft_content
        else:
            edited_content = edit_response.content
            logger.info("Successfully edited and refined blog content")
        
        # Step 6: Format and publish
        yield RunResponse(
            content="Step 6/6: Formatting final blog post...",
            event=RunEvent.workflow_step_started
        )
        
        publish_response = self.publisher.run(
            f"Format the following blog post for publishing:\n\n"
            f"{edited_content}\n\n"
            f"Ensure proper markdown formatting with appropriate headings, "
            f"paragraph spacing, and emphasis. Make sure all links are properly formatted. "
            f"Add metadata including title: '{outline.title}', keywords: {', '.join(topic.keywords)}."
        )
        
        if not publish_response or not publish_response.content:
            logger.warning("Formatting failed, using unformatted content")
            final_content = edited_content
        else:
            final_content = publish_response.content
            logger.info("Successfully formatted blog post for publishing")
        
        # Cache the final blog post
        self.add_blog_post_to_cache(user_input, final_content)
        
        # Return the final blog post
        yield RunResponse(
            content=final_content,
            event=RunEvent.workflow_completed
        )

    def get_cached_blog_post(self, user_input: str) -> Optional[str]:
        """Get a cached blog post if available."""
        return self.session_state.get("blog_posts", {}).get(user_input)

    def add_blog_post_to_cache(self, user_input: str, blog_post: str):
        """Cache a blog post for future reuse."""
        logger.info(f"Caching blog post for: {user_input}")
        self.session_state.setdefault("blog_posts", {})
        self.session_state["blog_posts"][user_input] = blog_post


# Create an instance of the workflow
blog_workflow = BlogPostGenerator(
    session_id="blog-post-generator",
    storage=SqliteStorage(
        table_name="blog_post_generator",
        db_file=agent_storage
    )
)
