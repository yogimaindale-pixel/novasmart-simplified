# NovaSmart AI Agent Architecture — Masterclass Knowledge Transfer (KT) & Developer Guide

Welcome to the **NovaSmart AI Agent Architecture Masterclass Knowledge Transfer (KT) Document**. This guide provides junior developers and engineers with an end-to-end understanding of how AI agents are designed, built, documented, and orchestrated—ranging from simple single-purpose text agents using in-memory dummy data to autonomous security governance multi-agent estates.

---

## 1. Architectural Overview & Learning Progression Map

AI Agent architecture at NovaSmart is structured into progressive, beginner-friendly complexity tiers:

```
+-----------------------------------------------------------------------------------+
|                        NOVASMART AGENT PROGRESSION MAP                            |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [Tier 1 Series: Simple In-Memory Single Agents (Zero Tools Needed)]              |
|   - 01_simple_agent.py : Persona instructions & prompt greeting responses         |
|   - 01b_email_classifier_agent.py : Ticket classification & urgency scoring        |
|   - 01c_faq_retrieval_agent.py : In-memory FAQ search & match confidence          |
|   - 01d_sentiment_moderator_agent.py : Product review sentiment & content safety   |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 2: Intermediate Tool-Using Agent]                                          |
|   - File: examples/02_intermediate_agent.py                                       |
|   - Concept: Model Context Protocol (MCP) Tool Calling + Parameter Validation     |
|              + SQLite Inventory Queries + Audit Trail Serialization               |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 3: Retail Multi-Agent System]                                              |
|   - File: examples/03_complex_multi_agent.py                                      |
|   - Concept: System Coordinator Router + Specialized Sub-Agents                   |
|              (Catalog Sub-Agent & Price Matcher Sub-Agent)                       |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 4: Enterprise Customer Support Multi-Agent System]                        |
|   - File: examples/04_customer_support_multi_agent.py                             |
|   - Concept: Support Triage Router + Shipping Sub-Agent + Refund Sub-Agent        |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 5: Financial Compliance & Fraud Audit Multi-Agent System]                 |
|   - File: examples/05_financial_audit_multi_agent.py                              |
|   - Concept: Audit Supervisor + High-Value CTR Audit Sub-Agent                    |
|              + Fraud Risk Sub-Agent + Anomaly & Velocity Detection                |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 6: Human-in-the-Loop (HITL) Approval Agent]                                |
|   - File: examples/06_human_in_the_loop_agent.py                                  |
|   - Concept: Threshold Auditing + Approval Token Persistence                      |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 7: RAG Knowledge Retrieval Agent]                                          |
|   - File: examples/07_rag_knowledge_agent.py                                      |
|   - Concept: Retrieval-Augmented Generation + Policy Document Chunking             |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 8: Autonomous Security Governance Multi-Agent Estate]                     |
|   - File: examples/08_autonomous_governance_multi_agent.py                        |
|   - Concept: Security Supervisor + Shadow Agent Discovery Sub-Agent               |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

---

## 2. Technical Code Specifications for Simple Agent Series

### 2.1 Lesson 1b Specification (`01b_email_classifier_agent.py`)
- **Class**: `SimpleEmailClassifierAgent`
- **Purpose**: Classifies incoming customer emails into support categories (`BILLING`, `TECHNICAL_SUPPORT`, `SPAM`, `GENERAL_INQUIRY`) and assigns urgency levels (`CRITICAL`, `HIGH`, `LOW`, `NONE`).
- **Data Source**: In-memory `DUMMY_EMAILS` list containing simulated email dictionaries.

### 2.2 Lesson 1c Specification (`01c_faq_retrieval_agent.py`)
- **Class**: `SimpleFAQAgent`
- **Purpose**: Searches a dummy FAQ knowledge base (`DUMMY_FAQ_DATABASE`) using string token matching and returns answers with confidence scores.

### 2.3 Lesson 1d Specification (`01d_sentiment_moderator_agent.py`)
- **Class**: `SimpleModeratorAgent`
- **Purpose**: Evaluates sentiment signals (`POSITIVE`, `NEUTRAL`, `NEGATIVE`) in product reviews and flags inappropriate spam/scam keywords for moderation.

---

## 3. Junior Developer Quickstart Guide

### Running All Simple Agent Lessons on Your Local Laptop

```bash
# Tier 1 Series (Zero Tool Installation Needed!)
python3 examples/01_simple_agent.py
python3 examples/01b_email_classifier_agent.py
python3 examples/01c_faq_retrieval_agent.py
python3 examples/01d_sentiment_moderator_agent.py
```

### Best Practices Checklist for Engineers
- [x] **Zero Third-Party Dependencies**: Built using standard Python libraries (`json`, `sqlite3`, `uuid`) so anyone can copy and run locally.
- [x] **In-Memory Dummy Data**: Uses clean Python dictionary lists so junior developers can easily modify sample datasets.
- [x] **Line-by-Line Comments**: Write explanatory comments above every method and critical block so junior developers can follow logic easily.
