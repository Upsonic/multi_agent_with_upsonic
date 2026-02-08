"""
Code Example 3: Coordinate Team Product Launch Campaign

This example demonstrates:
1. Campaign Manager (Leader): Strategic planning and delegation
2. Market Researcher: Target audience and competitor analysis
3. Content Creator: Product messaging and value propositions
4. Social Media Strategist: Platform strategy and engagement tactics

Flow: Leader analyzes tasks → Delegates to specialists → Combines results (Coordinate Mode)
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

# Market Researcher: Analyzes target market and competitors
market_researcher = Agent(
    name="Market Researcher",
    role="Market Analysis Specialist",
    goal="Analyze target markets, competitors, and trends to inform campaign strategy",
    instructions="""You are an expert market researcher. Your job is to:
    - Identify target audience segments and their needs
    - Analyze competitor landscape and positioning
    - Identify market trends and opportunities
    - Provide data-driven insights for campaign planning
    
    Return comprehensive market analysis with actionable insights.""",
    model="openai/gpt-4o",
)

# Content Creator: Develops product messaging and content
content_creator = Agent(
    name="Content Creator",
    role="Product Messaging Specialist",
    goal="Create compelling product messaging and value propositions",
    instructions="""You are an expert content strategist. Your job is to:
    - Develop clear, compelling product messaging
    - Create value propositions that resonate with target audience
    - Craft key messages for different audience segments
    - Ensure messaging is consistent and impactful
    
    Return structured content strategy with messaging framework.""",
    model="openai/gpt-4o",
)

# Social Media Strategist: Plans social media campaign
social_media_strategist = Agent(
    name="Social Media Strategist",
    role="Social Media Campaign Expert",
    goal="Develop social media strategy and engagement tactics for product launch",
    instructions="""You are a social media strategy expert. Your job is to:
    - Recommend best platforms for target audience
    - Create content calendar and posting schedule
    - Define engagement tactics and KPIs
    - Plan influencer and community strategies
    
    Return actionable social media campaign plan.""",
    model="openai/gpt-4o"
)


# ============================================================================
# TEAM SECTION
# ============================================================================

# Create Coordinate Team with Leader
team = Team(
    agents=[market_researcher, content_creator, social_media_strategist],
    mode="coordinate",  # Leader agent coordinates and delegates
    model="openai/gpt-4o"  # Required: Model for leader (Campaign Manager)
)


# ============================================================================
# TASKS SECTION
# ============================================================================

# Campaign tasks (leader will delegate to appropriate specialists)
campaign_tasks = [
    Task(
        description="""Analyze the target market for our new AI-powered productivity tool.
        
        Focus on:
        - Target audience demographics and psychographics
        - Key competitors and their positioning
        - Market size and growth trends
        - Opportunities and gaps in the market
        
        Provide actionable insights for campaign planning."""
    ),
    
    Task(
        description="""Develop compelling product messaging for the AI productivity tool launch.
        
        Create:
        - Core value proposition
        - Key messaging pillars
        - Messaging for different audience segments (professionals, students, teams)
        - Differentiation from competitors
        
        Messaging should be clear, compelling, and action-oriented."""
    ),
    
    Task(
        description="""Create a social media strategy for the product launch campaign.
        
        Include:
        - Recommended platforms (LinkedIn, Twitter, etc.)
        - Content themes and post types
        - Launch timeline and content calendar (pre-launch, launch, post-launch)
        - Engagement tactics and community building
        - Success metrics and KPIs
        
        Strategy should maximize reach and engagement."""
    )
]


# ============================================================================
# EXECUTION SECTION
# ============================================================================

def main():
    """Execute the Coordinate Team product launch campaign workflow"""
    
    print("=" * 70)
    print("COORDINATE TEAM: PRODUCT LAUNCH CAMPAIGN")
    print("=" * 70)
    print()
    
    print(f"📋 Team Mode: Coordinate")
    print(f"👥 Specialists: {len(team.agents)} (Market, Content, Social Media)")
    print(f"🎯 Leader: Campaign Manager (coordinates and delegates)")
    print()
    
    # ========================================================================
    # WHY COORDINATE MODE?
    # ========================================================================
    print("\n" + "=" * 70)
    print("WHY COORDINATE MODE?")
    print("=" * 70)
    print("""
    ✅ Complex tasks - Market research, content, social media strategy
    ✅ Non-linear - Tasks can run in parallel
    ✅ Strategic planning - Leader decides priority and delegation
    ✅ Interconnected - Results must be combined into cohesive plan
    
    ❌ Sequential: Too rigid - tasks don't need strict order
    ❌ Route: Wrong - need ALL agents working together, not just one
    """)
    
    # ========================================================================
    # STEP 1: Leader Analysis
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 1: LEADER ANALYSIS - Strategic Planning")
    print("=" * 70)
    print(f"🎯 Leader: Campaign Manager")
    print(f"📝 Analyzing tasks and planning delegation...")
    print()
    
    # ========================================================================
    # STEP 2: Delegation
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 2: DELEGATION - Assigning to Specialists")
    print("=" * 70)
    print(f"👥 Available Specialists:")
    print(f"   - {market_researcher.name}")
    print(f"   - {content_creator.name}")
    print(f"   - {social_media_strategist.name}")
    print()
    
    # ========================================================================
    # STEP 3: Coordination
    # ========================================================================
    print("\n" + "=" * 70)
    print("STEP 3: COORDINATION - Combining Results")
    print("=" * 70)
    print(f"📊 Leader combines specialist outputs into unified campaign plan")
    print()
    
    # ========================================================================
    # EXECUTE TEAM WORKFLOW
    # ========================================================================
    print("\n" + "=" * 70)
    print("EXECUTING COORDINATE TEAM WORKFLOW")
    print("=" * 70)
    print()
    
    final_result = team.print_do(campaign_tasks)
    
    # ========================================================================
    # FINAL RESULTS
    # ========================================================================
    print("\n" + "=" * 70)
    print("WORKFLOW COMPLETE")
    print("=" * 70)
    print()
    
    word_count = len(str(final_result).split())
    print(f"✅ Product launch campaign plan created")
    print(f"📊 Word count: {word_count}")
    print()
    
    print("=" * 70)
    print("FINAL CAMPAIGN PLAN")
    print("=" * 70)
    print()
    print(final_result)
    print()
    
    return final_result


if __name__ == "__main__":
    main()
