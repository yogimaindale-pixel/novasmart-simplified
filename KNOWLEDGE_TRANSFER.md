# NovaSmart AI Agent Architecture — Knowledge Transfer (KT) & Developer Guide

Welcome to the **NovaSmart AI Agent Architecture Knowledge Transfer (KT) Document**. This guide provides junior developers and engineers with an end-to-end understanding of how AI agents are designed, built, documented, and orchestrated—ranging from simple single-purpose text agents to complex multi-agent enterprise systems.

---

## 1. Architectural Overview & Learning Progression Map

AI Agent architecture at NovaSmart is structured into five progressive complexity tiers:

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
|  [Tier 2: Intermediate Agent]                                                     |
|   - File: examples/02_intermediate_agent.py                                       |
|   - Concept: Model Context Protocol (MCP) Tool Calling + Parameter Validation     |
|              + SQLite Inventory Queries + Audit Trail Serialization               |
|                                                                                   |
|         |                                                                         |
|         v                                                                         |
|                                                                                   |
|  [Tier 3: Complex Retail Multi-Agent System]                                      |
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
+-----------------------------------------------------------------------------------+
```

---

## 2. Technical Code Specifications

### 2.1 Tier 1 Specification (`01_simple_agent.py`)
- **Class**: `SimpleAgent`
- **Purpose**: Encapsulates basic text message evaluation without backend database tools.
- **Key Methods**:
  - `__init__(agent_name, system_instruction)`: Initializes persona metadata.
  - `generate_response(user_prompt)`: Strips input whitespace, checks empty string constraints, evaluates keyword rules, and returns a JSON-serializable dictionary.

### 2.2 Tier 2 Specification (`02_intermediate_agent.py`)
- **Class**: `IntermediateToolAgent`
- **Purpose**: Demonstrates single-agent Model Context Protocol (MCP) tool execution.
- **Key Methods**:
  - `tool_lookup_inventory(sku_or_name)`: Executes parameterized SQL queries (`WHERE item_id = ? OR item_name LIKE ?`) against an SQLite inventory database.
  - `process_query(user_query)`: Evaluates user intent, invokes database lookup tools, handles out-of-stock items (`quantity_available == 0`), and attaches `tool_audit` metadata to response payloads.

### 2.3 Tier 3 Specification (`03_complex_multi_agent.py`)
- **Classes**: `NovaSmartCoordinatorAgent`, `CatalogInventorySubAgent`, `PriceMatcherSubAgent`
- **Purpose**: Enterprise Retail Multi-Agent System orchestrating specialized sub-agents.
- **Key Workflow**:
  1. **Coordinator Agent** receives user prompt.
  2. **Catalog & Inventory Sub-Agent** executes product lookup for `SKU-201`.
  3. **Price Matcher Sub-Agent** queries competitor pricing (`TechSuperstore` price `$279.99`) and calculates discount.
  4. **Coordinator Agent** merges sub-agent results into a single audit payload.

### 2.4 Tier 4 Specification (`04_customer_support_multi_agent.py`)
- **Classes**: `SupportTriageAgent`, `ShippingSubAgent`, `RefundSubAgent`
- **Purpose**: 4-Agent Customer Support system running locally with zero external dependencies.
- **Key Workflow**:
  1. **Support Triage Router Agent** inspects incoming prompt keywords (shipping, tracking, refund).
  2. **Order & Shipping Sub-Agent** checks SQLite `orders` table for tracking numbers.
  3. **Returns & Refunds Sub-Agent** checks SQLite `returns` table for refund approval statuses.
  4. Aggregates results into a structured JSON response object.

### 2.5 Tier 5 Specification (`05_financial_audit_multi_agent.py`)
- **Classes**: `AuditSupervisorAgent`, `HighValueAuditSubAgent`, `FraudRiskSubAgent`
- **Purpose**: Financial compliance and fraud risk multi-agent auditing engine.
- **Key Workflow**:
  1. **High-Value Transaction Audit Sub-Agent** flags transactions $\ge \$10,000$ USD for Regulatory CTR reporting.
  2. **Fraud Risk Sub-Agent** calculates geographic anomaly scores based on multi-country account transactions.
  3. **Audit Supervisor Agent** determines final hold/approval decision (`HOLD_FOR_REVIEW` vs `APPROVED`).

---

## 3. Execution Sequence Diagrams

### 3.1 Multi-Agent Customer Support System Flow (`04_customer_support_multi_agent.py`)

```
+--------------------+         +-----------------------+         +----------------------+         +--------------------+
| Customer Prompt    |  --->   | Support Triage Router |  --->   | Shipping Sub-Agent   |  --->   | SQLite Orders Table|
+--------------------+         +-----------------------+         +----------------------+         +--------------------+
                                           |                                |                               |
                                           |                                | <--- Returns Tracking Details |
                                           v                                +-------------------------------+
                                    +---------------------+
                                    | Refund Sub-Agent    |
                                    +---------------------+
                                           |
                                           | ---> Queries Returns Table
                                           | <--- Returns Refund Status
                                           v
                               +-----------------------+
                               | Consolidated Response |
                               +-----------------------+
```

---

## 4. Junior Developer Quickstart Guide

### 4.1 Running All Lessons on Your Local Laptop

Execute all five tutorial scripts directly using Python 3:

```bash
# Lesson 1: Simple Agent
python3 examples/01_simple_agent.py

# Lesson 2: Intermediate Tool-Using Agent
python3 examples/02_intermediate_agent.py

# Lesson 3: Complex Retail Multi-Agent System
python3 examples/03_complex_multi_agent.py

# Lesson 4: Customer Support Multi-Agent System
python3 examples/04_customer_support_multi_agent.py

# Lesson 5: Financial Audit Multi-Agent System
python3 examples/05_financial_audit_multi_agent.py
```

### 4.2 Best Practices Checklist for Engineers
- [x] **Zero Third-Party Dependencies**: Built using standard Python libraries (`sqlite3`, `json`) so anyone can copy and run locally.
- [x] **Parameterization**: Always use SQL placeholders (`?`) rather than string concatenation to block SQL injection.
- [x] **Line-by-Line Comments**: Write explanatory comments above every method and critical block so junior developers can follow logic easily.
- [x] **Auditability**: Return structured dictionaries (`status`, `sub_agent`, `audit_trail`) instead of raw unformatted strings.
- [x] **Graceful Fallbacks**: Ensure out-of-stock items and missing records return clean `NOT_FOUND` statuses rather than crashing.
