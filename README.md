# Multi Agent With Upsonic

Demonstrates Upsonic agents and team modes: manual calls, sequential, coordinate, route.

## REQUIREMENTS

    Python 3.12+
    OpenAI API key
    Dependencies: requirements.txt

## INSTALLATION

    $ uv venv venv
    $ source venv/bin/activate
    $ uv pip install -r requirements.txt

    # Set API key
    $ echo "OPENAI_API_KEY=your_key_here" > .env

## USAGE

    # Run with uv (project uses uv for dependency management)
    $ uv run src/code_example_1/main.py    # Manual agent calls (no team)
    $ uv run src/code_example_2/main.py    # Sequential team
    $ uv run src/code_example_3/main.py    # Coordinate team
    $ uv run src/code_example_4/main.py    # Route team

## TESTING

    # Run individual tests
    $ uv run tests/test_code_example_1.py
    $ uv run tests/test_code_example_2.py
    $ uv run tests/test_code_example_3.py
    $ uv run tests/test_code_example_4.py

    # All tests follow TDD approach
    # Test first, code second, validate

## TEAM MODES

### sequential
    Linear workflow. Tasks execute in order.
    Each task builds on previous results.
    
    Use when: Clear sequence of steps (A→B→C)
    Example: Research → Write → Edit
    
    Example 2: Blog post creation
        - Research Agent gathers information
        - Writer Agent creates draft
        - Editor Agent polishes and optimizes

### coordinate
    Leader manages specialists. Strategic planning.
    Tasks can run in parallel. Results combined.
    
    Use when: Complex, interconnected tasks
    Example: Product launch (market + content + social)
    
    Example 3: Product launch campaign
        - Campaign Manager (leader) delegates
        - Market Researcher analyzes target audience
        - Content Creator develops messaging
        - Social Media Strategist plans platforms

### route
    Router selects single best expert.
    Fast routing. No collaboration overhead.
    
    Use when: Specialized experts needed
    Example: Customer support routing
    
    Example 4: Customer support system
        - Router analyzes query
        - Routes to: Billing, Technical, or Account expert
        - Expert provides direct answer

## DECISION FRAMEWORK

| Criteria      | Sequential     | Coordinate         | Route           |
|---------------|----------------|--------------------|-----------------|
| Workflow      | Linear         | Non-linear         | One-shot        |
| Tasks         | Dependent      | Independent        | Single query    |
| Leader        | No             | Yes (Manager)      | Yes (Router)    |
| Collaboration | Sequential     | Strategic planning | No collaboration|
| Best for      | Pipelines      | Projects           | Expert routing  |

### When to use Sequential
    ✓ Clear sequence of steps
    ✓ Each step builds on previous
    ✓ Simple collaboration
    
    ✗ Don't use for parallel tasks
    ✗ Don't use when planning needed

### When to use Coordinate
    ✓ Complex, multi-domain tasks
    ✓ Strategic planning required
    ✓ Non-linear workflow
    
    ✗ Don't use for simple linear tasks
    ✗ Don't use for single-expert queries

### When to use Route
    ✓ Specialized experts
    ✓ One query → One expert
    ✓ Fast routing needed
    
    ✗ Don't use when all agents needed
    ✗ Don't use for multi-step workflows

## STRUCTURE

    src/
        code_example_1/     Manual agent calls (no team mode)
        code_example_2/     Blog post creation (sequential team)
        code_example_3/     Product launch campaign (coordinate team)
        code_example_4/     Customer support system (route team)
        
    tests/
        test_code_example_1.py
        test_code_example_2.py
        test_code_example_3.py
        test_code_example_4.py
        
    requirements.txt        Direct dependencies only
    README.md               This file

## GOOGLE COLAB NOTEBOOKS

    Each example includes interactive notebook:
    
    src/code_example_1/code_example_1_colab.ipynb
    src/code_example_2/code_example_2_colab.ipynb
    src/code_example_3/code_example_3_colab.ipynb
    src/code_example_4/code_example_4_colab.ipynb
    
    Upload to colab.research.google.com

## EXAMPLES IN DETAIL

### Example 1: OCR and Text Extraction (Manual Agent Calls)
    Demonstrates: Manual agent calls without team mode
    Agents: OCR Agent, Extractor Agent
    Flow: Image → OCR → Text extraction
    Note: Direct agent.do(task) calls, no Team coordination

### Example 2: Blog Post Creation (Sequential)
    Demonstrates: Sequential team mode
    Agents: Research Specialist, Blog Writer, Content Editor
    Flow: Research → Write → Edit
    Context passing: Automatic

### Example 3: Product Launch Campaign (Coordinate)
    Demonstrates: Coordinate team mode
    Agents: Market Researcher, Content Creator, Social Media Strategist
    Leader: Campaign Manager (automatic)
    Flow: Leader plans → Delegates → Combines

### Example 4: Customer Support System (Route)
    Demonstrates: Route team mode
    Agents: Billing Expert, Technical Expert, Account Expert
    Router: Automatic routing agent
    Flow: Query → Router → Expert → Answer

## TDD APPROACH

    All examples follow Test-Driven Development:
    
    1. Write test first (define expected behavior)
    2. Write code (implement to pass tests)
    3. Validate (ensure all tests pass)
    
    Progress trackers included in each test file.

## CONTRIBUTING

    Follow TDD. Write tests first.
    Use exact versions in requirements.txt (==)
    Maintain Technical Manual README style.
    
    Conventional commits:
        feat: Add new feature
        fix: Fix bug
        docs: Update documentation
        test: Add/update tests

## DOCUMENTATION

    Upsonic docs:  https://docs.upsonic.ai
    Team modes:    https://docs.upsonic.ai/concepts/team
    GitHub:        https://github.com/Upsonic/Upsonic
    
    Find skills:   https://clawdhub.com

## LICENSE

    MIT License
    
    Copyright (c) 2024 Upsonic Teknoloji A.Ş.
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
