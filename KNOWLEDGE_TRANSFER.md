# NovaSmart AI Agent Architecture — Masterclass Knowledge Transfer (KT) & Developer Guide

Welcome to the **NovaSmart AI Agent Architecture Masterclass Knowledge Transfer (KT) Document**. This guide provides junior developers and engineers with an end-to-end understanding of how AI agents are designed, built, documented, and orchestrated—ranging from simple single-purpose text agents to autonomous security governance multi-agent estates.

---

## 1. Architectural Overview & Learning Progression Map

AI Agent architecture at NovaSmart is structured into eight progressive complexity tiers:

```
+-----------------------------------------------------------------------------------+
|                        NOVASMART AGENT PROGRESSION MAP                            |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [Tier 1: Simple Agent]                                                           |
|   - File: examples/01_simple_agent.py                                             |
|   - Concept: Persona instruction + Basic input parsing + Static responses         |
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
|              (Catalog Sub-Agent & Price Matcher Sub-Agent) + Multi-Tool           |
|              Orchestration + Aggregated Enterprise Audit Logs                     |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 4: Enterprise Customer Support Multi-Agent System]                        |
|   - File: examples/04_customer_support_multi_agent.py                             |
|   - Concept: Support Triage Router + Shipping Sub-Agent + Refund Sub-Agent        |
|              + Order Tracking + Refund Eligibility Audits                         |
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
|              + State Pause & Resume Workflow                                      |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 7: RAG Knowledge Retrieval Agent]                                          |
|   - File: examples/07_rag_knowledge_agent.py                                      |
|   - Concept: Retrieval-Augmented Generation + Vector/Keyword Search               |
|              + Policy Document Chunking + Citation Synthesizer                    |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 8: Autonomous Security Governance Multi-Agent Estate]                     |
|   - File: examples/08_autonomous_governance_multi_agent.py                        |
|   - Concept: Security Supervisor + Shadow Agent Discovery Sub-Agent               |
|              + Shared Identity Right-Sizing + Compliance Evidence Generation       |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

---

## 2. Technical Code Specifications

### 2.1 Tier 1 Specification (`01_simple_agent.py`)
- **Class**: `SimpleAgent`
- **Purpose**: Encapsulates basic text message evaluation without backend database tools.

### 2.2 Tier 2 Specification (`02_intermediate_agent.py`)
- **Class**: `IntermediateToolAgent`
- **Purpose**: Demonstrates single-agent Model Context Protocol (MCP) tool execution.

### 2.3 Tier 3 Specification (`03_complex_multi_agent.py`)
- **Classes**: `NovaSmartCoordinatorAgent`, `CatalogInventorySubAgent`, `PriceMatcherSubAgent`
- **Purpose**: Enterprise Retail Multi-Agent System orchestrating specialized sub-agents.

### 2.4 Tier 4 Specification (`04_customer_support_multi_agent.py`)
- **Classes**: `SupportTriageAgent`, `ShippingSubAgent`, `RefundSubAgent`
- **Purpose**: 4-Agent Customer Support system running locally with zero external dependencies.

### 2.5 Tier 5 Specification (`05_financial_audit_multi_agent.py`)
- **Classes**: `AuditSupervisorAgent`, `HighValueAuditSubAgent`, `FraudRiskSubAgent`
- **Purpose**: Financial compliance and fraud risk multi-agent auditing engine.

### 2.6 Tier 6 Specification (`06_human_in_the_loop_agent.py`)
- **Class**: `HumanInTheLoopAgent`
- **Purpose**: Pauses execution for actions $\ge \$500$, generating approval tokens for manager review.

### 2.7 Tier 7 Specification (`07_rag_knowledge_agent.py`)
- **Class**: `RAGKnowledgeAgent`
- **Purpose**: Performs keyword similarity retrieval over policy documentation and synthesizes cited answers.

### 2.8 Tier 8 Specification (`08_autonomous_governance_multi_agent.py`)
- **Classes**: `SecurityGovernanceSupervisorAgent`, `ShadowAgentDiscoverySubAgent`, `IdentityRightSizingSubAgent`
- **Purpose**: Autonomous governance estate scanner discovering shadow workloads and shared logins.

---

## 3. Execution Sequence Diagrams

### 3.1 Autonomous Security Governance Multi-Agent Estate Flow (`08_autonomous_governance_multi_agent.py`)

```
+--------------------------+         +-------------------------------+         +----------------------------+
| Security Audit Trigger   |  --->   | Security Governance Supervisor|  --->   | Shadow Discovery Sub-Agent |
+--------------------------+         +-------------------------------+         +----------------------------+
                                                    |                                       |
                                                    |                                       | <--- Returns Shadow Workloads
                                                    v                                       +----------------------------+
                                     +-------------------------------+
                                     | Identity Right-Sizing Agent   |
                                     +-------------------------------+
                                                    |
                                                    | ---> Queries Shared Logins
                                                    | <--- Flags Excessive Roles (roles/owner)
                                                    v
                                        +-----------------------+
                                        | Compliance Evidence   |
                                        +-----------------------+
```

---

## 4. Junior Developer Quickstart Guide

### 4.1 Running All 8 Masterclass Lessons Locally

Run any script using Python 3 directly on your local laptop:

```bash
python3 examples/01_simple_agent.py
python3 examples/02_intermediate_agent.py
python3 examples/03_complex_multi_agent.py
python3 examples/04_customer_support_multi_agent.py
python3 examples/05_financial_audit_multi_agent.py
python3 examples/06_human_in_the_loop_agent.py
python3 examples/07_rag_knowledge_agent.py
python3 examples/08_autonomous_governance_multi_agent.py
```

### 4.2 Best Practices Checklist for Engineers
- [x] **Zero Third-Party Dependencies**: Built using standard Python libraries (`sqlite3`, `json`, `uuid`) so anyone can copy and run locally.
- [x] **Parameterization**: Always use SQL placeholders (`?`) rather than string concatenation to block SQL injection.
- [x] **Line-by-Line Comments**: Write explanatory comments above every method and critical block so junior developers can follow logic easily.
- [x] **Auditability**: Return structured dictionaries (`status`, `sub_agent`, `audit_trail`) instead of raw unformatted strings.
- [x] **Human Control**: Use token-based state pause/resume for high-risk mutating operations.
