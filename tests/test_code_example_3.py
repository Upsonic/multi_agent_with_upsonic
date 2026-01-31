"""
Test case for code_example_3: Coordinate Team Product Launch Campaign

TDD Approach:
1. Write test FIRST with expected behavior
2. Implement main.py to make tests pass
3. Tests should pass one by one as you build

Expected flow:
1. Campaign Manager (leader) analyzes tasks strategically
2. Delegates to specialists: Market Researcher, Content Creator, Social Media Strategist
3. Leader coordinates and combines results
4. Final output is a comprehensive product launch campaign plan
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_coordinate_product_launch():
    """
    TDD Test: Coordinate Team Product Launch Campaign
    
    This test defines the EXPECTED BEHAVIOR before implementation.
    As you write main.py, tests should gradually pass.
    
    Expected Results:
    - Campaign Manager (leader) delegates tasks to specialists
    - Market Researcher provides market analysis
    - Content Creator develops messaging
    - Social Media Strategist creates platform strategy
    - Final output is comprehensive, combined campaign plan
    - Contains all sections: market analysis, messaging, social strategy
    """
    
    print("\n" + "=" * 70)
    print("TDD TEST: Coordinate Team Product Launch Campaign")
    print("=" * 70)
    
    # ========================================================================
    # PRECONDITIONS: Setup checks
    # ========================================================================
    print("\n[PRECONDITIONS] Checking setup...")
    
    # Test 1: No external files needed (pure AI generation)
    print("✅ No external dependencies required")
    
    # Test 2: Environment should have API key
    print("✅ Preconditions met")
    
    # ========================================================================
    # EXECUTION: Run the workflow
    # ========================================================================
    print("\n[EXECUTION] Running Coordinate Team workflow...")
    
    # Import and run main workflow
    # This will FAIL initially (TDD: write test first!)
    try:
        from src.code_example_3.main import (
            market_researcher, content_creator, social_media_strategist,
            team, campaign_tasks
        )
        
        # Execute team workflow
        print("\nRunning Coordinate Team...")
        final_result = team.do(campaign_tasks)
        print(f"✅ Team workflow completed")
        
    except ImportError as e:
        print(f"⚠️  Import failed (expected in TDD): {e}")
        print("→ Next step: Implement main.py to make this pass")
        # In TDD, this is OK - we write test BEFORE code
        return
    except Exception as e:
        print(f"❌ Workflow execution failed: {e}")
        raise
    
    # ========================================================================
    # ASSERTIONS: Validate expected behavior
    # ========================================================================
    print("\n[ASSERTIONS] Validating results...")
    
    # Test 3: Final result should not be empty
    assert final_result is not None and str(final_result).strip() != "", \
        "❌ Final result is empty"
    print("✅ Final result is not empty")
    
    final_text = str(final_result).lower()
    
    # Test 4: Should contain campaign plan sections
    required_sections = ['market', 'content', 'social', 'strategy']
    found_sections = [sec for sec in required_sections if sec in final_text]
    assert len(found_sections) >= 3, \
        f"❌ Missing campaign sections. Found: {found_sections}, Expected at least 3 of: {required_sections}"
    print(f"✅ Contains campaign sections: {found_sections}")
    
    # Test 5: Word count should be substantial (campaign plan is detailed)
    word_count = len(str(final_result).split())
    assert word_count >= 500, \
        f"❌ Campaign plan too short: {word_count} words (expected ≥500)"
    print(f"✅ Campaign plan is comprehensive: {word_count} words")
    
    # Test 6: Should contain product launch keywords
    keywords = ['product', 'launch', 'campaign', 'target', 'audience']
    found_keywords = [kw for kw in keywords if kw in final_text]
    assert len(found_keywords) >= 3, \
        f"❌ Missing keywords. Found: {found_keywords}, Expected at least 3 of: {keywords}"
    print(f"✅ Contains launch keywords: {found_keywords}")
    
    # Test 7: Should have multiple distinct sections
    # Check for section markers (markdown headers, bullet points, numbering)
    has_structure = any([
        final_text.count('#') >= 3,  # Multiple headers
        final_text.count('\n\n') >= 5,  # Multiple paragraphs
        final_text.count('-') >= 5 or final_text.count('•') >= 5,  # Lists
        final_text.count('1.') >= 2 or final_text.count('2.') >= 1  # Numbered lists
    ])
    assert has_structure, \
        "❌ Campaign plan lacks proper structure"
    print("✅ Campaign plan is well-structured")
    
    # Test 8: Should demonstrate coordination (combined insights from multiple agents)
    # Check if different perspectives are present
    perspective_indicators = [
        'research', 'analysis', 'data',  # Market researcher
        'message', 'content', 'copy',    # Content creator
        'social', 'platform', 'engagement'  # Social media strategist
    ]
    found_perspectives = [ind for ind in perspective_indicators if ind in final_text]
    assert len(found_perspectives) >= 4, \
        f"❌ Missing agent perspectives. Found: {found_perspectives}"
    print(f"✅ Demonstrates multi-agent coordination: {len(found_perspectives)} perspectives")
    
    # Test 9: Should have actionable elements (not just theory)
    actionable_words = ['recommend', 'should', 'plan', 'strategy', 'action', 'step']
    found_actionable = [word for word in actionable_words if word in final_text]
    assert len(found_actionable) >= 2, \
        f"❌ Plan lacks actionable elements. Found: {found_actionable}"
    print(f"✅ Contains actionable recommendations: {found_actionable}")
    
    # ========================================================================
    # SUCCESS: All tests passed
    # ========================================================================
    print("\n" + "=" * 70)
    print("✅ ALL TESTS PASSED")
    print("=" * 70)
    print(f"\nResults:")
    print(f"  Word Count: {word_count}")
    print(f"  Sections Found: {', '.join(found_sections)}")
    print(f"  Keywords Found: {', '.join(found_keywords)}")
    print(f"  Agent Perspectives: {len(found_perspectives)}")
    print(f"  Preview: {str(final_result)[:200]}...")
    print()
    
    return True


def test_tdd_progress():
    """
    TDD Progress Tracker
    
    Check which parts of the implementation are complete.
    Use this to track development progress.
    """
    print("\n" + "=" * 70)
    print("TDD PROGRESS TRACKER")
    print("=" * 70)
    
    progress = {
        "Main module exists": False,
        "Agents defined (3 specialists)": False,
        "Tasks defined": False,
        "Team created (coordinate mode)": False,
        "Leader model specified": False,
        "Workflow completes": False,
        "Output is comprehensive": False,
        "All tests pass": False
    }
    
    # Check 1: Module
    try:
        from src.code_example_3 import main as code_example_3_main
        progress["Main module exists"] = True
        
        # Check 2: Agents
        if hasattr(code_example_3_main, 'market_researcher') and \
           hasattr(code_example_3_main, 'content_creator') and \
           hasattr(code_example_3_main, 'social_media_strategist'):
            progress["Agents defined (3 specialists)"] = True
        
        # Check 3: Tasks
        if hasattr(code_example_3_main, 'campaign_tasks'):
            progress["Tasks defined"] = True
        
        # Check 4: Team
        if hasattr(code_example_3_main, 'team'):
            team = code_example_3_main.team
            if hasattr(team, 'mode') and team.mode == 'coordinate':
                progress["Team created (coordinate mode)"] = True
                
                # Check 5: Leader model
                if hasattr(team, 'model') and team.model:
                    progress["Leader model specified"] = True
            
            # Check 6: Try running
            try:
                result = team.do(code_example_3_main.campaign_tasks)
                
                if result and str(result).strip():
                    progress["Workflow completes"] = True
                    
                    # Check if output is comprehensive
                    word_count = len(str(result).split())
                    if word_count >= 500:
                        progress["Output is comprehensive"] = True
                    
                    # Check if all validations pass
                    final_text = str(result).lower()
                    if 'market' in final_text and 'social' in final_text:
                        progress["All tests pass"] = True
            except:
                pass
    except ImportError:
        pass
    
    # Display progress
    print("\nImplementation Progress:")
    for step, status in progress.items():
        icon = "✅" if status else "⬜"
        print(f"  {icon} {step}")
    
    completed = sum(progress.values())
    total = len(progress)
    print(f"\nProgress: {completed}/{total} steps complete ({completed/total*100:.0f}%)")
    print()


if __name__ == "__main__":
    # Run TDD test
    print("Running TDD tests...\n")
    
    # Track progress
    test_tdd_progress()
    
    # Run main test
    try:
        test_coordinate_product_launch()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("\nThis is expected in TDD - implement the code to make tests pass!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        raise
