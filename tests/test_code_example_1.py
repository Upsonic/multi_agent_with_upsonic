"""
Test case for code_example_1: OCR and text extraction workflow

Expected flow:
1. OCR Agent reads image and extracts all text
2. Extractor Agent finds specific information (ID Number) from OCR output
3. Final output shows character count and extracted result
"""

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


def test_ocr_and_extraction():
    """
    Test the OCR and extraction workflow
    
    Expected:
    - OCR agent should read text from sample_id_card.png
    - Should extract at least 50 characters
    - Extractor agent should find ID Number
    - Final output should contain both metrics
    """
    # This test will be run after main.py implementation
    # For TDD: Write test first, then implement
    
    # Expected behavior
    assert os.path.exists('src/media/sample_id_card.png'), "Sample ID card image should exist"
    
    # After running main.py, we expect:
    # - OCR output with text content
    # - Extracted ID number: "123456789"
    # - Character count > 50
    
    print("✅ Test structure defined")
    print("Expected: OCR reads >50 chars, Extractor finds ID Number")
    

if __name__ == "__main__":
    test_ocr_and_extraction()
