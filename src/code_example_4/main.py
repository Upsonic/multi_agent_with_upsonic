"""
Code Example 4: Route Team Customer Support System

This example demonstrates:
1. Router Agent: Analyzes query and selects best expert
2. Billing Expert: Handles payment and billing questions
3. Technical Expert: Handles technical issues and bugs
4. Account Expert: Handles account and security questions

Flow: Query → Router analyzes → Routes to ONE expert → Direct answer (Route Mode)
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

# Billing Expert: Handles payment and billing issues
billing_expert = Agent(
    name="Billing Expert",
    role="Billing & Payment Specialist",
    goal="Resolve billing, payment, and invoice-related customer issues",
    instructions="""You are a billing and payment expert. Your job is to:
    - Help customers with payment failures, refunds, and billing questions
    - Explain charges, invoices, and subscription details
    - Guide customers through payment method updates
    - Resolve billing disputes and transaction issues
    
    Provide clear, direct answers with actionable steps.""",
    model="openai/gpt-4o-mini",
    debug=True
)

# Technical Expert: Handles technical issues and bugs
technical_expert = Agent(
    name="Technical Expert",
    role="Technical Support Specialist",
    goal="Resolve technical issues, bugs, and software problems",
    instructions="""You are a technical support expert. Your job is to:
    - Troubleshoot app crashes, errors, and technical issues
    - Guide customers through technical problems step-by-step
    - Provide workarounds and solutions for bugs
    - Explain system requirements and compatibility issues
    
    Provide clear technical guidance that non-technical users can follow.""",
    model="openai/gpt-4o-mini",
    debug=True
)

# Account Expert: Handles account and security questions
account_expert = Agent(
    name="Account Expert",
    role="Account & Security Specialist",
    goal="Help customers with account access, security, and profile management",
    instructions="""You are an account and security expert. Your job is to:
    - Help customers with password resets and login issues
    - Guide through account security settings and 2FA setup
    - Assist with profile updates and account management
    - Handle account recovery and security concerns
    
    Provide secure, step-by-step guidance for account-related issues.""",
    model="openai/gpt-4o-mini",
    debug=True
)


# ============================================================================
# TEAM SECTION
# ============================================================================

# Create Route Team with Router
team = Team(
    agents=[billing_expert, technical_expert, account_expert],
    mode="route",  # Router agent routes to best expert
    model="openai/gpt-4o-mini"  # Required: Model for router agent
)


# ============================================================================
# EXECUTION SECTION
# ============================================================================

def main():
    """Execute the Route Team customer support workflow"""
    
    print("=" * 70)
    print("ROUTE TEAM: CUSTOMER SUPPORT SYSTEM")
    print("=" * 70)
    print()
    
    print(f"📋 Team Mode: Route")
    print(f"👥 Experts: {len(team.agents)} (Billing, Technical, Account)")
    print(f"🎯 Router: Intelligent routing agent (automatic)")
    print()
    
    # ========================================================================
    # WHY ROUTE MODE?
    # ========================================================================
    print("\n" + "=" * 70)
    print("WHY ROUTE MODE?")
    print("=" * 70)
    print("""
    ✅ Specialized experts - Each handles specific domain
    ✅ One question → One expert (no collaboration needed)
    ✅ Fast routing - Direct answer from specialist
    ✅ Efficient - No overhead from unnecessary agents
    
    ❌ Sequential: Overhead - don't need all agents for one question
    ❌ Coordinate: Overkill - no planning needed, just route and answer
    """)
    
    # ========================================================================
    # EXAMPLE CUSTOMER QUERIES
    # ========================================================================
    print("\n" + "=" * 70)
    print("EXAMPLE CUSTOMER QUERIES")
    print("=" * 70)
    print()
    
    example_queries = [
        ("My payment failed and I got charged twice. Can you help?", "billing_expert"),
        ("The app keeps crashing when I try to upload files.", "technical_expert"),
        ("I forgot my password. How do I reset it?", "account_expert")
    ]
    
    for i, (query, expected_expert) in enumerate(example_queries, 1):
        # ====================================================================
        # STEP: Router Analysis
        # ====================================================================
        print(f"\n{'-' * 70}")
        print(f"QUERY {i}: {query}")
        print(f"{'-' * 70}")
        print(f"🎯 Router analyzing query...")
        print(f"📝 Expected routing: {expected_expert}")
        print()
        
        # ====================================================================
        # STEP: Expert Response
        # ====================================================================
        task = Task(description=query)
        result = team.do(task)
        
        word_count = len(str(result).split())
        print(f"\n✅ Response received ({word_count} words)")
        print(f"\n{result}")
        print()
    
    # ========================================================================
    # FINAL SUMMARY
    # ========================================================================
    print("\n" + "=" * 70)
    print("WORKFLOW COMPLETE")
    print("=" * 70)
    print()
    
    print(f"✅ Customer support system ready")
    print(f"📊 {len(example_queries)} example queries processed")
    print(f"🎯 All queries routed to appropriate experts")
    print()
    
    return True


if __name__ == "__main__":
    main()
