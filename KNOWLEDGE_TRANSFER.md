# NovaSmart AI Agent Architecture — Knowledge Transfer (KT) & Developer Guide

Welcome to the **NovaSmart AI Agent Architecture Knowledge Transfer (KT) Document**. This guide provides junior developers and engineers with an end-to-end understanding of how AI agents are designed, built, documented, and orchestrated—ranging from simple single-purpose text agents to complex multi-agent enterprise coordination systems.

---

## 1. Architectural Overview & Learning Progression Map

AI Agent architecture at NovaSmart is structured into three progressive complexity tiers:

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
|  [Tier 3: Complex Multi-Agent System]                                             |
|   - File: examples/03_complex_multi_agent.py                                      |
|   - Concept: System Coordinator Router + Specialized Sub-Agents                   |
|              (Catalog Sub-Agent & Price Matcher Sub-Agent) + Multi-Tool           |
|              Orchestration + Aggregated Enterprise Audit Logs                     |
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
- **Purpose**: Enterprise Multi-Agent System orchestrating specialized sub-agents.
- **Key Workflow**:
  1. **Coordinator Agent** receives user prompt (e.g. "Can you find the NovaSmart 4K Monitor and check if we can price match competitors?").
  2. **Catalog & Inventory Sub-Agent** executes product lookup for `SKU-201` (`NovaSmart 4K Monitor`, price `$299.99`, stock `15`).
  3. **Price Matcher Sub-Agent** queries competitor pricing (`TechSuperstore` price `$279.99`), evaluates eligibility (`competitor_price < novasmart_price`), and calculates `$20.00` discount.
  4. **Coordinator Agent** merges sub-agent results into a single audit payload with complete `audit_trail` records.

---

## 3. Execution Sequence Diagrams

### 3.1 Multi-Agent System Execution Flow (`03_complex_multi_agent.py`)

```
+---------------+         +-----------------------+         +-----------------------+         +---------------------+
| User Prompt   |  --->   | Coordinator Agent     |  --->   | Catalog Sub-Agent     |  --->   | SQLite Database     |
+---------------+         +-----------------------+         +-----------------------+         +---------------------+
                                      |                                 |                                |
                                      |                                 | <--- Returns Product (SKU-201) |
                                      v                                 +--------------------------------+
                               +-----------------------+
                               | Price Match Sub-Agent |
                               +-----------------------+
                                      |
                                      | ---> Queries Competitor Prices
                                      | <--- Returns Discount ($20.00)
                                      v
                          +-----------------------+
                          | Consolidated Response |
                          +-----------------------+
```

---

## 4. Junior Developer Quickstart Guide

### 4.1 Running All Lessons Locally

Execute the lesson scripts from your terminal:

```bash
# Lesson 1: Simple Agent
python3 /config/Desktop/Session1/build-with-gemini/examples/01_simple_agent.py

# Lesson 2: Intermediate Tool-Using Agent
python3 /config/Desktop/Session1/build-with-gemini/examples/02_intermediate_agent.py

# Lesson 3: Complex Multi-Agent System
python3 /config/Desktop/Session1/build-with-gemini/examples/03_complex_multi_agent.py
```

### 4.2 Best Practices Checklist for Engineers
- [x] **Parameterization**: Always use SQL placeholders (`?`) rather than string concatenation to block SQL injection.
- [x] **Line-by-Line Comments**: Write explanatory comments above every method and critical block so junior developers can follow logic easily.
- [x] **Auditability**: Return structured dictionaries (`status`, `sub_agent`, `audit_trail`) instead of raw unformatted strings.
- [x] **Graceful Fallbacks**: Ensure out-of-stock items and missing records return clean `NOT_FOUND` statuses rather than crashing.
