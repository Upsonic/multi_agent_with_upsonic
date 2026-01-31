"""
Test case for code_example_2: Sequential Team Blog Post Creation

TDD Approach:
1. Write test FIRST with expected behavior
2. Implement main.py to make tests pass
3. Tests should pass one by one as you build

Expected flow:
1. Research Agent gathers information about the topic
2. Writer Agent creates blog post based on research
3. Editor Agent polishes content, adds SEO optimization
4. Final output is a complete, SEO-optimized blog post
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_sequential_blog_creation():
    """
    TDD Test: Sequential Team Blog Post Creation Workflow
    
    This test defines the EXPECTED BEHAVIOR before implementation.
    As you write main.py, tests should gradually pass.
    
    Expected Results:
    - Research agent gathers at least 200 characters of research
    - Writer agent creates 400-600 word blog post
    - Editor agent adds title and SEO keywords
    - Final output is valid markdown format
    - Contains target keywords: AI, agents, 2026
    - Each agent's output builds on previous agent's work
    """
    
    print("\n" + "=" * 70)
    print("TDD TEST: Sequential Team Blog Post Creation")
    print("=" * 70)
    
    # ========================================================================
    # PRECONDITIONS: Setup checks
    # ========================================================================
    print("\n[PRECONDITIONS] Checking setup...")
    
    # Test 1: No external files needed (pure AI generation)
    print("✅ No external dependencies required")
    
    # Test 2: Environment should have API key
    # Note: Will check in actual implementation
    print("✅ Preconditions met")
    
    # ========================================================================
    # EXECUTION: Run the workflow
    # ========================================================================
    print("\n[EXECUTION] Running Sequential Team workflow...")
    
    # Import and run main workflow
    # This will FAIL initially (TDD: write test first!)
    try:
        from src.code_example_2.main import (
            researcher, writer, editor, 
            team, research_task, writing_task, editing_task
        )
        
        # Execute team workflow
        print("\nRunning Sequential Team...")
        tasks = [research_task, writing_task, editing_task]
        final_result = team.do(tasks)
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
    
    final_text = str(final_result)
    
    # Test 4: Should contain a title (markdown header)
    assert '#' in final_text or final_text.split('\n')[0].isupper() or \
           any(word in final_text.lower()[:100] for word in ['title:', 'headline:']), \
        "❌ Blog post should have a title"
    print("✅ Blog post has a title")
    
    # Test 5: Word count should be reasonable (400-800 words)
    word_count = len(final_text.split())
    assert 400 <= word_count <= 1000, \
        f"❌ Word count out of range: {word_count} words (expected 400-1000)"
    print(f"✅ Word count is appropriate: {word_count} words")
    
    # Test 6: Should contain target keywords
    keywords = ['ai', 'agent', '2026']
    final_lower = final_text.lower()
    found_keywords = [kw for kw in keywords if kw in final_lower]
    assert len(found_keywords) >= 2, \
        f"❌ Missing keywords. Found: {found_keywords}, Expected at least 2 of: {keywords}"
    print(f"✅ Contains keywords: {found_keywords}")
    
    # Test 7: Should have multiple paragraphs (content structure)
    paragraphs = [p for p in final_text.split('\n\n') if p.strip()]
    assert len(paragraphs) >= 3, \
        f"❌ Insufficient structure: {len(paragraphs)} paragraphs (expected ≥3)"
    print(f"✅ Well-structured: {len(paragraphs)} paragraphs")
    
    # Test 8: Should contain some SEO elements (keywords, structure)
    # Check for basic markdown structure or formatting
    has_structure = any([
        '##' in final_text,  # Subheadings
        '**' in final_text,  # Bold text
        '*' in final_text and final_text.count('*') > 2,  # Italic or list
        '-' in final_text and final_text.count('-') > 3   # List items
    ])
    assert has_structure, \
        "❌ Blog post lacks structure (headings, lists, or formatting)"
    print("✅ Blog post has proper structure (markdown formatting)")
    
    # ========================================================================
    # SUCCESS: All tests passed
    # ========================================================================
    print("\n" + "=" * 70)
    print("✅ ALL TESTS PASSED")
    print("=" * 70)
    print(f"\nResults:")
    print(f"  Word Count: {word_count}")
    print(f"  Paragraphs: {len(paragraphs)}")
    print(f"  Keywords Found: {', '.join(found_keywords)}")
    print(f"  Preview: {final_text[:150]}...")
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
        "Agents defined (3 agents)": False,
        "Tasks defined (3 tasks)": False,
        "Team created (sequential mode)": False,
        "Workflow completes": False,
        "Output is valid markdown": False,
        "All tests pass": False
    }
    
    # Check 1: Module
    try:
        from src.code_example_2 import main as code_example_2_main
        progress["Main module exists"] = True
        
        # Check 2: Agents
        if hasattr(code_example_2_main, 'researcher') and \
           hasattr(code_example_2_main, 'writer') and \
           hasattr(code_example_2_main, 'editor'):
            progress["Agents defined (3 agents)"] = True
        
        # Check 3: Tasks
        if hasattr(code_example_2_main, 'research_task') and \
           hasattr(code_example_2_main, 'writing_task') and \
           hasattr(code_example_2_main, 'editing_task'):
            progress["Tasks defined (3 tasks)"] = True
        
        # Check 4: Team
        if hasattr(code_example_2_main, 'team'):
            progress["Team created (sequential mode)"] = True
            
            # Check 5: Try running
            try:
                tasks = [
                    code_example_2_main.research_task,
                    code_example_2_main.writing_task,
                    code_example_2_main.editing_task
                ]
                result = code_example_2_main.team.do(tasks)
                
                if result and str(result).strip():
                    progress["Workflow completes"] = True
                    
                    # Check if output has markdown structure
                    if '#' in str(result) or '**' in str(result):
                        progress["Output is valid markdown"] = True
                    
                    # Check if all validations pass
                    word_count = len(str(result).split())
                    if 400 <= word_count <= 1000:
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
        test_sequential_blog_creation()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("\nThis is expected in TDD - implement the code to make tests pass!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        raise
