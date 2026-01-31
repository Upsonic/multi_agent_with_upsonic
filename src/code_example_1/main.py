"""
Code Example 1: OCR and Text Extraction Workflow

This example demonstrates:
1. OCR Agent: Reads text from an ID card image
2. Extractor Agent: Extracts specific information (ID Number) from OCR output
3. Analyzer Agent: Provides final statistics

Flow: Image → OCR → Text Extraction → Statistics
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
from upsonic import Agent, Task

# Load environment variables
load_dotenv(project_root / '.env')


# ============================================================================
# AGENTS SECTION
# ============================================================================

# OCR Agent: Reads text from images
ocr_agent = Agent(
    name="OCR Agent",
    role="Text Recognition Specialist",
    goal="Extract all visible text from images accurately",
    instructions="""You are an expert OCR (Optical Character Recognition) specialist.
    Your job is to carefully read images and extract all visible text with high accuracy.
    You pay attention to every detail and return complete text content.""",
    model="openai/gpt-4o-mini",
    debug=True
)

# Extractor Agent: Finds specific information
extractor_agent = Agent(
    name="Extractor Agent",
    role="Information Extraction Specialist",
    goal="Find and extract specific information from text",
    instructions="""You are a data extraction expert. You excel at finding specific
    information in text documents. You are precise and always return exactly
    what is requested, nothing more, nothing less.""",
    model="openai/gpt-4o-mini",
    debug=True
)

# Analyzer Agent: Provides statistics
analyzer_agent = Agent(
    name="Analyzer Agent",
    role="Data Analyst",
    goal="Analyze results and provide clear statistics",
    instructions="""You are a data analyst who excels at summarizing results
    and providing clear, concise statistics about the work done.""",
    model="openai/gpt-4o-mini",
    debug=True
)


# ============================================================================
# TASKS SECTION
# ============================================================================

# Get image path
image_path = str(project_root / 'src' / 'media' / 'sample_id_card.png')

# Task 1: OCR - Read text from image
ocr_task = Task(
    description="""Read the ID card image and extract ALL visible text.
    
    Return all text you can see in the image, maintaining the original structure.
    Include all fields and their values.""",
    context=[image_path]  # Image file path in context
)

# Task 2: Extract ID Number
extraction_task = Task(
    description="""From the OCR text provided in the context, find and extract
    ONLY the ID Number value.
    
    Look for a field labeled 'ID Number' and return only the number itself.
    If you find it, return just the number. If not found, return 'NOT_FOUND'.""",
    context=[ocr_task]  # This task depends on ocr_task output
)

# Task 3: Analyze and report statistics
analysis_task = Task(
    description="""Analyze the results and provide a summary report.
    
    From the context, you have:
    1. OCR Agent output (full text)
    2. Extractor Agent output (ID Number)
    
    Create a report with:
    - Total characters read by OCR Agent
    - ID Number extracted by Extractor Agent
    
    Format:
    OCR Agent read X characters
    Extractor Agent found ID Number: Y""",
    context=[ocr_task, extraction_task]  # Depends on both previous tasks
)


# ============================================================================
# EXECUTION SECTION
# ============================================================================

def main():
    """Execute the OCR and extraction workflow"""
    
    print("=" * 70)
    print("OCR AND TEXT EXTRACTION WORKFLOW")
    print("=" * 70)
    print()
    
    # Check if image exists
    image_path = project_root / 'src' / 'media' / 'sample_id_card.png'
    if not image_path.exists():
        print(f"❌ Error: Image not found at {image_path}")
        return
    
    print(f"✅ Image found: {image_path}")
    print()
    
    # Execute Task 1: OCR
    print("\n" + "=" * 70)
    print("STEP 1: OCR - Reading image")
    print("=" * 70)
    ocr_result = ocr_agent.do(ocr_task)
    print(f"\n📄 OCR Output:")
    print(ocr_result)
    print(f"\n📊 Characters read: {len(str(ocr_result))}")
    
    # Execute Task 2: Extraction
    print("\n" + "=" * 70)
    print("STEP 2: EXTRACTION - Finding ID Number")
    print("=" * 70)
    extraction_result = extractor_agent.do(extraction_task)
    print(f"\n🔍 Extracted ID Number: {extraction_result}")
    
    # Execute Task 3: Analysis
    print("\n" + "=" * 70)
    print("STEP 3: ANALYSIS - Final Statistics")
    print("=" * 70)
    analysis_result = analyzer_agent.do(analysis_task)
    print(f"\n📈 Final Report:")
    print(analysis_result)
    
    # Summary
    print("\n" + "=" * 70)
    print("WORKFLOW COMPLETE")
    print("=" * 70)
    print(f"\n✅ OCR Agent read {len(str(ocr_result))} characters")
    print(f"✅ Extractor Agent found: {extraction_result}")
    print()


if __name__ == "__main__":
    main()
