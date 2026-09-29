# 🏛️ 02. NovaSmart Simplified - System Architecture

## 1. Core Framework Architecture

### Stage 1: In-Memory Database Initialization (`initialize_demo_database`)
- Creates an in-memory SQLite database (`:memory:`).
- Provisions the `products` table with schema (`product_id`, `name`, `price`, `stock_count`).
- Seeds 3 sample retail items (`NovaSmart Wireless Earbuds`, `NovaSmart Ergonomic Mouse`, `NovaSmart USB-C Hub`).

### Stage 2: Database Query Tool (`query_retail_database`)
- Accepts natural text search queries.
- Executes parameterized SQL `SELECT` queries across product name and ID fields.
- Returns structured Python dictionary lists.

### Stage 3: Agent Orchestration Engine (`NovaSmartAgent`)
- Accepts user prompts, resolves target tool functions, executes SQL lookups, and builds formatted JSON response payloads.
- Status codes: `SUCCESS` or `ERROR`.

### Stage 4: Extension Skills Suite (`.agents/skills/`)
- `enable-a2ui`: Renders dynamic UI widgets using Google A2UI callback standard (`a2ui_callback`).
- `build-rag`: Validates RAG tool compatibility (`test_rag_a2ui_compat.py`).
- `publish-to-github`: Deploys finished project to personal GitHub via `gh` CLI.
