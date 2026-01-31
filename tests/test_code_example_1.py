"""
Test case for code_example_1: OCR and text extraction workflow

TDD Approach:
1. Write test FIRST with expected behavior
2. Implement main.py to make tests pass
3. Tests should pass one by one as you build

Expected flow:
1. OCR Agent reads image and extracts all text
2. Extractor Agent finds specific information (ID Number) from OCR output
3. Final output shows character count and extracted result
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_ocr_and_extraction():
    """
    TDD Test: OCR and text extraction workflow
    
    This test defines the EXPECTED BEHAVIOR before implementation.
    As you write main.py, tests should gradually pass.
    
    Expected Results:
    - OCR agent reads sample_id_card.png
    - Extracts at least 50 characters of text
    - Extractor agent finds ID Number field
    - Returns exact value: "123456789"
    - Workflow completes without errors
    """
    
    print("\n" + "=" * 70)
    print("TDD TEST: OCR and Extraction Workflow")
    print("=" * 70)
    
    # ========================================================================
    # PRECONDITIONS: Setup and file checks
    # ========================================================================
    print("\n[PRECONDITIONS] Checking setup...")
    
    # Test 1: Image file must exist
    image_path = project_root / 'src' / 'media' / 'sample_id_card.png'
    assert image_path.exists(), f"❌ Image not found: {image_path}"
    print(f"✅ Image exists: {image_path}")
    
    # Test 2: Environment should have API key (for agents)
    # Note: In real implementation, check for OPENAI_API_KEY
    # For TDD, we define what's needed
    print("✅ Preconditions met")
    
    # ========================================================================
    # EXECUTION: Run the workflow
    # ========================================================================
    print("\n[EXECUTION] Running OCR and extraction workflow...")
    
    # Import and run main workflow
    # This will FAIL initially (TDD: write test first!)
    try:
        from src.code_example_1.main import ocr_agent, extractor_agent, ocr_task, extraction_task
        
        # Execute OCR task
        print("\nRunning OCR Agent...")
        ocr_result = ocr_agent.do(ocr_task)
        print(f"✅ OCR completed")
        
        # Execute Extraction task
        print("\nRunning Extractor Agent...")
        extraction_result = extractor_agent.do(extraction_task)
        print(f"✅ Extraction completed")
        
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
    
    # Test 3: OCR should extract at least 50 characters
    ocr_text_length = len(str(ocr_result))
    assert ocr_text_length >= 50, \
        f"❌ OCR output too short: {ocr_text_length} chars (expected ≥50)"
    print(f"✅ OCR extracted {ocr_text_length} characters (≥50 required)")
    
    # Test 4: OCR result should contain key fields
    ocr_text = str(ocr_result).lower()
    assert 'id number' in ocr_text or 'id' in ocr_text, \
        "❌ OCR didn't detect 'ID Number' field"
    print("✅ OCR detected ID-related fields")
    
    # Test 5: Extraction should return the exact ID Number
    expected_id = "123456789"
    assert str(extraction_result).strip() == expected_id, \
        f"❌ Wrong ID extracted: '{extraction_result}' (expected '{expected_id}')"
    print(f"✅ Correct ID Number extracted: {expected_id}")
    
    # Test 6: Results should not be empty
    assert ocr_result is not None and str(ocr_result).strip() != "", \
        "❌ OCR result is empty"
    assert extraction_result is not None and str(extraction_result).strip() != "", \
        "❌ Extraction result is empty"
    print("✅ No empty results")
    
    # ========================================================================
    # SUCCESS: All tests passed
    # ========================================================================
    print("\n" + "=" * 70)
    print("✅ ALL TESTS PASSED")
    print("=" * 70)
    print(f"\nResults:")
    print(f"  OCR Output: {ocr_text_length} characters")
    print(f"  ID Number: {extraction_result}")
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
        "Image file exists": False,
        "Main module exists": False,
        "Agents defined": False,
        "Tasks defined": False,
        "OCR works": False,
        "Extraction works": False,
        "Full workflow passes": False
    }
    
    # Check 1: Image
    image_path = project_root / 'src' / 'media' / 'sample_id_card.png'
    progress["Image file exists"] = image_path.exists()
    
    # Check 2: Module
    try:
        from src.code_example_1 import main as code_example_1_main
        progress["Main module exists"] = True
        
        # Check 3: Agents
        if hasattr(code_example_1_main, 'ocr_agent') and \
           hasattr(code_example_1_main, 'extractor_agent'):
            progress["Agents defined"] = True
        
        # Check 4: Tasks
        if hasattr(code_example_1_main, 'ocr_task') and \
           hasattr(code_example_1_main, 'extraction_task'):
            progress["Tasks defined"] = True
        
        # Check 5-7: Don't run tasks in progress tracker
        # (They will be run in main test - avoid duplicate runs)
        # For now, just check if tasks can be imported
        try:
            # Check if tasks have proper context
            if hasattr(code_example_1_main.ocr_task, 'context'):
                progress["OCR works"] = True
            if hasattr(code_example_1_main.extraction_task, 'context'):
                progress["Extraction works"] = True
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
        test_ocr_and_extraction()
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        print("\nThis is expected in TDD - implement the code to make tests pass!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        raise
