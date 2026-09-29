# NovaSmart Simplified — AI Agent & Multi-Agent Architecture Masterclass

Welcome to **NovaSmart Simplified**! This repository is an end-to-end, production-ready educational masterclass designed to teach software engineers, junior developers, and cloud architects how to build, test, document, and govern AI Agents and Multi-Agent Systems.

---

## 📌 Executive Overview

Modern AI Agent development can often feel complex and difficult to grasp due to opaque abstractions. **NovaSmart Simplified** breaks down AI Agent design into clear, progressive architectural tiers. Every single script is written in clean Python using **zero external dependencies** (using standard built-in libraries like `sqlite3`, `json`, and `uuid`), allowing anyone to copy the repository onto a local laptop and run it immediately out-of-the-box.

---

## 🚀 Quickstart: Running on Your Local Laptop

### Requirements
- **Python 3.8+** (No `pip install` required!)

### Installation & Run Instructions

```bash
# 1. Clone your repository
git clone https://github.com/yogimaindale-pixel/novasmart-simplified.git

# 2. Change into the project directory
cd novasmart-simplified

# 3. Run any lesson script directly:

# Tier 1: Basic Text Persona Agent
python3 examples/01_simple_agent.py

# Tier 2: MCP Tool-Calling & SQLite Database Agent
python3 examples/02_intermediate_agent.py

# Tier 3: Retail Multi-Agent Coordination System
python3 examples/03_complex_multi_agent.py

# Tier 4: Customer Support Multi-Agent System
python3 examples/04_customer_support_multi_agent.py

# Tier 5: Financial Audit & Fraud Detection Multi-Agent System
python3 examples/05_financial_audit_multi_agent.py

# Tier 6: Human-in-the-Loop (HITL) Approval Agent
python3 examples/06_human_in_the_loop_agent.py

# Tier 7: RAG Policy Retrieval & Citation Agent
python3 examples/07_rag_knowledge_agent.py

# Tier 8: Autonomous Security Governance Multi-Agent Estate
python3 examples/08_autonomous_governance_multi_agent.py
```

---

## 📚 8-Tier Curriculum & Code Specifications

| Tier | Lesson File | Architectural Concept | Target Domain | Key Skills Taught |
|---|---|---|---|---|
| **Tier 1** | [`01_simple_agent.py`](examples/01_simple_agent.py) | Single-Purpose Agent | Support Greeting | Persona instructions, prompt normalization, static responses |
| **Tier 2** | [`02_intermediate_agent.py`](examples/02_intermediate_agent.py) | MCP Tool-Calling Agent | Inventory Stock | SQL parameterization (`?`), tool execution, audit logs |
| **Tier 3** | [`03_complex_multi_agent.py`](examples/03_complex_multi_agent.py) | Retail Multi-Agent System | Catalog & Price Match | Coordinator Router, Sub-Agent delegation, price matching |
| **Tier 4** | [`04_customer_support_multi_agent.py`](examples/04_customer_support_multi_agent.py) | Support Multi-Agent System | Order & Refunds | Multi-intent routing, shipping tracking, refund status |
| **Tier 5** | [`05_financial_audit_multi_agent.py`](examples/05_financial_audit_multi_agent.py) | Compliance Multi-Agent System | Financial Audit | High-value CTR thresholds ($10k+), geographic velocity fraud |
| **Tier 6** | [`06_human_in_the_loop_agent.py`](examples/06_human_in_the_loop_agent.py) | HITL Approval Agent | High-Value Refunds | Threshold pausing ($500+), token generation, manager approval |
| **Tier 7** | [`07_rag_knowledge_agent.py`](examples/07_rag_knowledge_agent.py) | RAG Search Agent | Policy Knowledge Base | Document chunking, keyword relevance scoring, citations |
| **Tier 8** | [`08_autonomous_governance_multi_agent.py`](examples/08_autonomous_governance_multi_agent.py) | Governance Estate System | Cloud Security Audit | Shadow agent discovery, shared login auditing, role right-sizing |

---

## 🗺️ Visual Architecture & Sequence Runflow Diagrams

### Multi-Agent Triage & Execution Sequence (Tier 4 & Tier 8)

```
+------------------+         +--------------------------+         +--------------------------+         +---------------------+
| User Prompt      |  --->   | System Coordinator Router|  --->   | Specialized Sub-Agent A  |  --->   | SQLite Backend DB   |
+------------------+         +--------------------------+         +--------------------------+         +---------------------+
                                          |                                     |                                 |
                                          |                                     | <--- Returns Sub-Query Data     |
                                          v                                     +---------------------------------+
                               +--------------------------+
                               | Specialized Sub-Agent B  |
                               +--------------------------+
                                          |
                                          | ---> Executes Tool Query
                                          | <--- Returns Sub-Query Data
                                          v
                              +----------------------------+
                              | Consolidated Audit Payload |
                              +----------------------------+
```

---

## 📑 Complete Documentation Suite

For detailed technical specifications, database schemas, and developer knowledge transfer guides, refer to:
- 📖 [DOCUMENTATION.md](DOCUMENTATION.md) — System specifications, database architecture, and sequence flow diagrams.
- 🎓 [KNOWLEDGE_TRANSFER.md](KNOWLEDGE_TRANSFER.md) — Complete 8-tier Masterclass developer Knowledge Transfer (KT) guide.

---

## 💡 Junior Developer Best Practices Checklist

1. **Parameterize Database Queries**: Never concatenate SQL strings! Always use `?` placeholders (e.g. `cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))`).
2. **Comment Every Function**: Write explanatory comments above every method explaining input arguments, return types, and business logic.
3. **Structured Outputs**: Always return JSON-serializable dictionaries with explicit `status` and `audit_trail` fields.
4. **Zero Crashing**: Handle missing items gracefully with `NOT_FOUND` status codes rather than raising unhandled exceptions.
