# NovaSmart Simplified — AI Agent & Multi-Agent Architecture Masterclass

Welcome to **NovaSmart Simplified**! This repository is an end-to-end, production-ready educational masterclass designed to teach software engineers, junior developers, and cloud architects how to build, test, document, and govern AI Agents and Multi-Agent Systems.

---

## 📌 Executive Overview

Modern AI Agent development can often feel complex and difficult to grasp due to opaque abstractions. **NovaSmart Simplified** breaks down AI Agent design into clear, progressive architectural tiers. Every single script is written in clean Python using **zero external dependencies** (using standard built-in libraries like `sqlite3`, `json`, and `uuid`), allowing anyone to copy the repository onto a local laptop and run it immediately out-of-the-box using in-memory dummy data.

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

# Simple Agent Series (Dummy Data, Zero Tools):
python3 examples/01_simple_agent.py
python3 examples/01b_email_classifier_agent.py
python3 examples/01c_faq_retrieval_agent.py
python3 examples/01d_sentiment_moderator_agent.py

# Intermediate & Advanced Agent Series:
python3 examples/02_intermediate_agent.py
python3 examples/03_complex_multi_agent.py
python3 examples/04_customer_support_multi_agent.py
python3 examples/05_financial_audit_multi_agent.py
python3 examples/06_human_in_the_loop_agent.py
python3 examples/07_rag_knowledge_agent.py
python3 examples/08_autonomous_governance_multi_agent.py
```

---

## 📚 Curriculum & Code Specifications

| Tier / Lesson | Lesson File | Architectural Concept | Target Domain | Key Skills Taught |
|---|---|---|---|---|
| **Tier 1** | [`01_simple_agent.py`](examples/01_simple_agent.py) | Single-Purpose Agent | Support Greeting | Persona instructions, prompt normalization |
| **Tier 1B** | [`01b_email_classifier_agent.py`](examples/01b_email_classifier_agent.py) | Email Classifier Agent | Support Tickets | Keyword department mapping, urgency scoring |
| **Tier 1C** | [`01c_faq_retrieval_agent.py`](examples/01c_faq_retrieval_agent.py) | FAQ Search Agent | Knowledge Base | In-memory token matching, confidence scoring |
| **Tier 1D** | [`01d_sentiment_moderator_agent.py`](examples/01d_sentiment_moderator_agent.py) | Sentiment & Safety Agent | Product Reviews | Positive/negative scoring, spam moderation flags |
| **Tier 2** | [`02_intermediate_agent.py`](examples/02_intermediate_agent.py) | MCP Tool-Calling Agent | Inventory Stock | SQL parameterization (`?`), tool execution, audit logs |
| **Tier 3** | [`03_complex_multi_agent.py`](examples/03_complex_multi_agent.py) | Retail Multi-Agent System | Catalog & Price Match | Coordinator Router, Sub-Agent delegation |
| **Tier 4** | [`04_customer_support_multi_agent.py`](examples/04_customer_support_multi_agent.py) | Support Multi-Agent System | Order & Refunds | Multi-intent routing, shipping tracking, refunds |
| **Tier 5** | [`05_financial_audit_multi_agent.py`](examples/05_financial_audit_multi_agent.py) | Compliance Multi-Agent System | Financial Audit | High-value CTR thresholds ($10k+), fraud velocity |
| **Tier 6** | [`06_human_in_the_loop_agent.py`](examples/06_human_in_the_loop_agent.py) | HITL Approval Agent | High-Value Refunds | Threshold pausing ($500+), token manager approval |
| **Tier 7** | [`07_rag_knowledge_agent.py`](examples/07_rag_knowledge_agent.py) | RAG Search Agent | Policy Base | Document chunking, relevance scoring, citations |
| **Tier 8** | [`08_autonomous_governance_multi_agent.py`](examples/08_autonomous_governance_multi_agent.py) | Governance Estate System | Cloud Security Audit | Shadow agent discovery, shared login auditing |

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
- 🎓 [KNOWLEDGE_TRANSFER.md](KNOWLEDGE_TRANSFER.md) — Complete Masterclass developer Knowledge Transfer (KT) guide.

---

## 💡 Junior Developer Best Practices Checklist

1. **Parameterize Database Queries**: Never concatenate SQL strings! Always use `?` placeholders (e.g. `cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))`).
2. **Comment Every Function**: Write explanatory comments above every method explaining input arguments, return types, and business logic.
3. **Structured Outputs**: Always return JSON-serializable dictionaries with explicit `status` and `audit_trail` fields.
4. **Zero Crashing**: Handle missing items gracefully with `NOT_FOUND` status codes rather than raising unhandled exceptions.
