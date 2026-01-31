# Multi-Agent System Examples with Upsonic

This repository demonstrates different team modes and multi-agent workflows using [Upsonic](https://upsonic.ai).

## 📚 Code Examples

### Example 1: OCR and Text Extraction (Agent Basics)
**Location:** `src/code_example_1/`

Demonstrates basic agent-task workflow:
- OCR Agent reads text from images
- Extractor Agent finds specific information
- No team mode (individual agents)

**Run:**
```bash
python src/code_example_1/main.py
```

### Example 2: Blog Post Creation (Sequential Team)
**Location:** `src/code_example_2/`

Demonstrates **Sequential Mode** team workflow:
- Research Agent → Writer Agent → Editor Agent
- Linear workflow, tasks build on each other
- Automatic context passing

**Run:**
```bash
python src/code_example_2/main.py
```

### Example 3: Product Launch Campaign (Coordinate Team)
**Location:** `src/code_example_3/`

Demonstrates **Coordinate Mode** team workflow:
- Campaign Manager (leader) delegates to specialists
- Market Researcher, Content Creator, Social Media Strategist
- Strategic planning and parallel execution

**Run:**
```bash
python src/code_example_3/main.py
```

---

## 🎯 How Can I Choose the Right Team Mode?

Upsonic offers three team modes: **Sequential**, **Coordinate**, and **Route**. Here's how to choose:

### Decision Framework

| Criteria | **Sequential** | **Coordinate** | **Route** |
|----------|---------------|----------------|-----------|
| **Workflow** | Linear (A→B→C) | Non-linear, Complex | One-shot |
| **Tasks** | Dependent (build on each) | Independent (parallel ok) | Single task to expert |
| **Collaboration** | Sequential flow needed | Strategic plan + delegation | No collaboration (direct route) |
| **Leader Agent** | No | **YES** (Manager) | **YES** (Router) |
| **Best For** | Content pipelines<br>Data processing<br>Quality stages | Project management<br>Campaigns<br>Multi-domain projects | Expert routing<br>Support tickets<br>Triage systems |
| **Example** | Blog post:<br>Research→Write→Edit | Product launch:<br>Plan all, then delegate | Customer support:<br>Route to expert, DONE |

### When to Use Sequential Mode

**✅ Use Sequential when:**
- You have a **clear sequence of steps**
- Each step **builds on previous results**
- Tasks must happen **in order**
- Simple, automatic collaboration is enough

**Example: Blog Post Creation** (Example 2)
```
WHY SEQUENTIAL?
✅ Linear workflow - Each step builds on previous
✅ Research must come first → Writing depends on research
✅ Editing depends on draft
❌ Coordinate: Overkill - no strategic planning needed
❌ Route: Wrong - need all 3 agents, not just one
```

**Use Cases:**
- Research → Write → Edit workflows
- Data pipeline: Extract → Transform → Load
- Quality stages: Draft → Review → Approve

---

### When to Use Coordinate Mode

**✅ Use Coordinate when:**
- Tasks are **complex and interconnected**
- Workflow is **non-linear** (tasks can run in parallel)
- You need **strategic planning**
- A **leader should decide** priority and delegation

**Example: Product Launch Campaign** (Example 3)
```
WHY COORDINATE?
✅ Complex tasks - Market research, content, social, metrics
✅ Non-linear - Tasks can run in parallel
✅ Strategic planning - Leader decides priority, delegation
✅ Interconnected - Results combined strategically
❌ Sequential: Too rigid - tasks don't need strict order
❌ Route: Wrong - need ALL agents working together
```

**Use Cases:**
- Product launches (marketing + content + strategy)
- Software projects (architecture + dev + testing)
- Event planning (venue + catering + marketing + logistics)
- Website redesigns (UX + dev + content + SEO)

---

### When to Use Route Mode

**✅ Use Route when:**
- You have **specialized experts**
- Each request goes to **ONE expert** only
- You need **fast routing decisions**
- **No multi-step collaboration** needed

**Example: Customer Support System**
```
WHY ROUTE?
✅ Specialized experts - Billing, Technical, Account experts
✅ One question → One expert (no collaboration needed)
✅ Fast routing - User gets direct answer
❌ Sequential: Overhead - don't need all agents
❌ Coordinate: Overkill - no planning needed, just route
```

**Use Cases:**
- Customer support routing (billing → billing expert, tech → tech expert)
- Legal/Medical/Technical expert triage
- Department routing systems
- Specialized Q&A platforms

---

## 🚀 Quick Start

### Installation

```bash
# Create virtual environment
uv venv venv
source venv/bin/activate  # Linux/macOS
# or: venv\Scripts\activate  # Windows

# Install dependencies
uv pip install -r requirements.txt
```

### Set Up API Key

```bash
# Create .env file
echo "OPENAI_API_KEY=your_key_here" > .env
```

### Run Examples

```bash
# Example 1: OCR and Extraction
python src/code_example_1/main.py

# Example 2: Sequential Team (Blog Post)
python src/code_example_2/main.py

# Example 3: Coordinate Team (Product Launch)
python src/code_example_3/main.py
```

### Run Tests (TDD)

```bash
# Test individual examples
python tests/test_code_example_1.py
python tests/test_code_example_2.py
python tests/test_code_example_3.py
```

---

## 📓 Google Colab Notebooks

Each example has an interactive Colab notebook for easy experimentation:

- **Example 1:** `src/code_example_1/code_example_1_colab.ipynb`
- **Example 2:** `src/code_example_2/code_example_2_colab.ipynb`
- **Example 3:** `src/code_example_3/code_example_3_colab.ipynb`

Upload to [Google Colab](https://colab.research.google.com/) and run!

---

## 🧪 Test-Driven Development (TDD)

All examples follow TDD approach:

1. **Write test first** - Define expected behavior
2. **Write code** - Implement to pass tests
3. **Validate** - Ensure all tests pass

Run progress tracker:
```bash
python tests/test_code_example_X.py
```

---

## 📚 Learn More

- [Upsonic Documentation](https://docs.upsonic.ai)
- [Team Modes Guide](https://docs.upsonic.ai/concepts/team)
- [GitHub Repository](https://github.com/Upsonic/Upsonic)

---

## 📝 Requirements

- Python 3.12+
- OpenAI API key
- Dependencies listed in `requirements.txt`

---

## 🤝 Contributing

Feel free to add more examples or improve existing ones!

---

## 📄 License

MIT License
