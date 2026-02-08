"""
Code Example 2: Sequential Team Blog Post Creation

This example demonstrates:
1. Research Agent: Gathers information about a topic
2. Writer Agent: Creates blog post based on research
3. Editor Agent: Polishes content and adds SEO optimization

Flow: Research → Write → Edit (Sequential Mode)
"""

# ============================================================================
# IMPORTS SECTION
# ============================================================================
import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv
from upsonic import Agent, Task, Team

# Load environment variables
load_dotenv(project_root / '.env')


# ============================================================================
# AGENTS SECTION
# ============================================================================

# Research Agent: Gathers information and data
researcher = Agent(
    name="Research Specialist",
    role="Content Researcher",
    goal="Find accurate, up-to-date information and trends on topics",
    instructions="""You are an expert content researcher. Your job is to:
    - Gather the latest information and trends on given topics
    - Identify key facts, statistics, and insights
    - Provide comprehensive research that serves as a foundation for content creation
    - Focus on accuracy and relevance
    
    Return your research in a structured format with key points and insights.""",
    model="openai/gpt-4o"
)

# Writer Agent: Creates engaging content
writer = Agent(
    name="Blog Writer",
    role="Content Creator",
    goal="Write engaging, informative, and well-structured blog posts",
    instructions="""You are a professional blog writer. Your job is to:
    - Transform research into engaging blog posts
    - Write in a clear, conversational tone
    - Structure content with introduction, body, and conclusion
    - Make complex topics accessible to general audience
    - Aim for 400-600 words
    
    Use the research provided in context to create a comprehensive blog post.""",
    model="openai/gpt-4o",
)

# Editor Agent: Polishes and optimizes content
editor = Agent(
    name="Content Editor",
    role="SEO & Style Editor",
    goal="Polish content, optimize for SEO, and ensure high quality",
    instructions="""You are an expert content editor and SEO specialist. Your job is to:
    - Review and polish the blog post for clarity and flow
    - Add a compelling, SEO-friendly title
    - Ensure proper markdown formatting (headings, bold, lists)
    - Optimize for target keywords (AI, agents, 2026)
    - Add subheadings to improve structure
    - Ensure the content is publication-ready
    
    Return the final, polished blog post in markdown format.""",
    model="openai/gpt-4o",
)


# ============================================================================
# TEAM SECTION
# ============================================================================

# Create Sequential Team
team = Team(
    agents=[researcher, writer, editor],
    mode="sequential"  # Tasks flow from one agent to the next automatically
)


# ============================================================================
# TASKS SECTION
# ============================================================================

# Task 1: Research the topic
research_task = Task(
    description="""Research the latest trends and developments in AI agents for 2026.
    
    Focus on:
    - Current state of AI agent technology
    - Emerging trends for 2026
    - Key applications and use cases
    - Industry predictions and insights
    
    Provide comprehensive research with key points and data."""
)

# Task 2: Write the blog post
writing_task = Task(
    description="""Using the research from the previous task, write a 400-600 word blog post
    about AI agent trends for 2026.
    
    The blog post should:
    - Have a clear introduction that hooks the reader
    - Cover main trends and insights from the research
    - Include specific examples and use cases
    - Have a conclusion that summarizes key takeaways
    - Be written for a general tech-savvy audience
    
    Write in a conversational, engaging tone.""",
    context=[research_task]  # This task depends on research_task output
)

# Task 3: Edit and optimize
editing_task = Task(
    description="""Edit and optimize the blog post for publication.
    
    Your tasks:
    - Add a compelling, SEO-friendly title (as markdown header)
    - Review and improve clarity, flow, and readability
    - Format in proper markdown (use ## for subheadings, ** for emphasis)
    - Optimize for keywords: AI, agents, 2026
    - Add subheadings to break up content
    - Ensure it's publication-ready
    
    Return the final, polished blog post in markdown format.""",
    context=[writing_task]  # This task depends on writing_task output
)


# ============================================================================
# EXECUTION SECTION
# ============================================================================

def main():
    """Execute the Sequential Team blog creation workflow"""
    
    print("=" * 70)
    print("SEQUENTIAL TEAM: BLOG POST CREATION WORKFLOW")
    print("=" * 70)
    print()
    
    print(f"📋 Team Mode: Sequential")
    print(f"👥 Agents: {len(team.agents)} (Researcher → Writer → Editor)")
    print()
    
    # ========================================================================
    # STEP 1: Research
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 1: RESEARCH - Gathering information")
    print("=" * 70)
    print(f"🔍 Agent: {researcher.name}")
    print(f"📝 Task: Research AI agent trends for 2026")
    print()
    
    # ========================================================================
    # STEP 2: Writing
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 2: WRITING - Creating blog post")
    print("=" * 70)
    print(f"✍️  Agent: {writer.name}")
    print(f"📝 Task: Write 400-600 word blog post")
    print()
    
    # ========================================================================
    # STEP 3: Editing
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 3: EDITING - Polishing and optimizing")
    print("=" * 70)
    print(f"📝 Agent: {editor.name}")
    print(f"📝 Task: Add title, format, optimize for SEO")
    print()
    
    # ========================================================================
    # EXECUTE TEAM WORKFLOW
    # ========================================================================
    print("\n" + "=" * 70)
    print("EXECUTING SEQUENTIAL TEAM WORKFLOW")
    print("=" * 70)
    print()
    
    tasks = [research_task, writing_task, editing_task]
    final_result = team.print_do(tasks)
    
    # ========================================================================
    # FINAL RESULTS
    # ========================================================================
    print("\n" + "=" * 70)
    print("WORKFLOW COMPLETE")
    print("=" * 70)
    print()
    
    word_count = len(str(final_result).split())
    print(f"✅ Blog post created successfully")
    print(f"📊 Word count: {word_count}")
    print()
    
    print("=" * 70)
    print("FINAL BLOG POST")
    print("=" * 70)
    print()
    print(final_result)
    print()
    
    return final_result


if __name__ == "__main__":
    main()
