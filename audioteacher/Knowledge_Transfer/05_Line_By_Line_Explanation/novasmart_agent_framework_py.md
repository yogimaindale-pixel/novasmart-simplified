# Line-by-Line Breakdown: novasmart_agent_framework.py

- **L1-L25**: Import `sqlite3`, `json`, `logging`, `typing`. Configure logger formatting.
- **L27-L70**: Define `initialize_demo_database()`. Connects to SQLite `:memory:`, creates `products` table, inserts 3 demo products, and commits transaction.
- **L77-L110**: Define `query_retail_database(db_conn, search_term)`. Prepares SQL query `SELECT * FROM products WHERE name LIKE ?`, fetches rows as dictionaries, and returns record list.
- **L117-L148**: Define `NovaSmartAgent.__init__` and `execute_tool(tool_name, **kwargs)`. Registers tool functions in internal dictionary map.
- **L150-L181**: Define `process_user_prompt(prompt)`. Logs incoming prompt, executes matching tool, and prints structured JSON response.
- **L185-L203**: Main block executing sample query prompt `'Can you list all available products and prices?'`.
