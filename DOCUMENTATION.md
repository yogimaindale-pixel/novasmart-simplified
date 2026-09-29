# NovaSmart Agent Framework — Documentation & Developer Guide

## 1. System Requirements

This software framework requires the following runtime environment:
- **Programming Language**: Python 3.10+ (tested on Python 3.14).
- **Core Standard Libraries**: `json`, `sqlite3`, `typing` (no external `pip` dependencies required for local execution).
- **Cloud Runtime Context**: In production, agents run as managed cloud workloads on **Cloud Run** or **Vertex AI Agent Platform**, connecting to **BigQuery** databases via **Model Context Protocol (MCP)** tool connectors.

---

## 2. Technical Code Specification

### 2.1 Component Architecture

The framework consists of four main functional sections:

1. **Database Layer (`initialize_demo_database`)**:
   - Initializes an in-memory SQLite database (`:memory:`).
   - Creates the `products` table containing `product_id`, `name`, `category`, `price`, and `stock_count`.
   - Inserts 3 sample retail items (`P101`, `P102`, `P103`).

2. **MCP Tool Integration Layer (`query_retail_database`)**:
   - Simulates a read-only Model Context Protocol (MCP) data tool.
   - Converts raw database tuples into structured dictionary rows matching schema headers.

3. **Agent Workload Class (`NovaSmartAgent`)**:
   - Encapsulates agent identity (`agent_name`), persona instructions (`system_instruction`), and database bindings (`db_connection`).
   - Implements `execute_tool()` for routing tool calls.
   - Implements `process_user_prompt()` for intent evaluation and structured JSON response formatting.

4. **Execution Script Entrypoint (`if __name__ == "__main__":`)**:
   - Bootstraps the database, instantiates the `Retail Catalog Agent`, and executes a test prompt.

---

## 3. Code Runflow & Execution Diagram

### 3.1 Sequence Walkthrough

1. **Bootstrap**: Script enters `if __name__ == "__main__":` and calls `initialize_demo_database()`.
2. **Table Creation & Seeding**: SQLite creates the `products` table and inserts product rows `P101`, `P102`, `P103`.
3. **Agent Instantiation**: `NovaSmartAgent` is created with the `db_connection` reference.
4. **Prompt Submission**: `process_user_prompt()` receives the user request string.
5. **Intent Evaluation**: The agent checks if database tool invocation is needed.
6. **Tool Execution**: `execute_tool()` calls `query_retail_database()` with a formatted SQL read query.
7. **Response Serialization**: Results are packaged into a structured dictionary and serialized to JSON string via `json.dumps()`.

### 3.2 Architectural Flow Diagram

```
+------------------+         +------------------+         +-------------------------+
|   User Request   |  --->   |  NovaSmartAgent  |  --->   |  query_retail_database  |
|  (Prompt Text)   |         | (Intent Parsing) |         |     (MCP Tool Layer)    |
+------------------+         +------------------+         +-------------------------+
                                                                       |
                                                                       v
+------------------+         +------------------+         +-------------------------+
|   JSON Output    |  <---   | Audited Response |  <---   |    SQLite Database      |
|  (Console Dump)  |         | (Dict Structure) |         |     (Products Data)     |
+------------------+         +------------------+         +-------------------------+
```

---

## 4. Junior Developer Quickstart Guide

To execute and verify the framework locally:

```bash
python3 /config/Desktop/Session1/novasmart_agent_framework.py
```

### Best Practices Introduced in this Code:
- **Strict Parameterization**: Queries use SQL placeholders (`?`) to prevent SQL injection vulnerabilities.
- **Explicit Typing**: All functions declare type annotations (`List[Dict[str, Any]]`) for readability.
- **Structured Audit Outputs**: Agent responses return metadata (`status`, `message`, `agent_name`) alongside data payloads for full auditability.
