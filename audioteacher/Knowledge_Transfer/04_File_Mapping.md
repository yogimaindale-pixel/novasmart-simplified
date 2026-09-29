# 🗺️ 04. Master File, Function, and Line Range Mapping Matrix

| Concept | Target File | Class / Function | Start Line | End Line | Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Database Initialization**| `novasmart_agent_framework.py` | `initialize_demo_database`| 27 | 70 | Provisions and seeds in-memory SQLite retail database. |
| **Retail Database Tool**| `novasmart_agent_framework.py` | `query_retail_database` | 77 | 110 | Executes SQL product search queries. |
| **Agent Engine** | `novasmart_agent_framework.py` | `NovaSmartAgent` | 117 | 181 | Coordinates prompt parsing, tool invocation, and JSON responses. |
| **A2UI Callback** | `.agents/skills/.../a2ui_utils.py` | `a2ui_callback` | 220 | 259 | Intercepts model streams and formats A2UI component surfaces. |
| **RAG Compatibility** | `.agents/skills/.../test_rag_a2ui_compat.py`| `consult_docs` | 57 | 80 | Validates RAG tool search output against A2UI rendering spec. |
