# 💡 03. Core Engineering Concepts & Pattern Cards

### Concept 1: Lightweight Tool Dispatch Pattern
- **What is it?**: Mapping agent intents to registered Python functions that query databases or APIs without heavy framework overhead.
- **Why needed?**: Maximizes execution speed, eliminates complex dependencies, and ensures 100% deterministic tool execution.
- **Repository Implementation**: `novasmart_agent_framework.py` (`NovaSmartAgent.execute_tool`).

### Concept 2: Agent-to-User Interface (A2UI) Callbacks
- **What is it?**: Intercepting model response streams to render interactive UI components (cards, forms, tables) in client frontends.
- **Repository Implementation**: `.agents/skills/enable-a2ui/template/a2ui_utils.py` (`a2ui_callback`).

### Concept 3: In-Memory SQLite Seeding
- **What is it?**: Bootstrapping an ephemeral relational database (`:memory:`) during application startup for rapid prototyping and unit testing.
- **Repository Implementation**: `novasmart_agent_framework.py` (`initialize_demo_database`).
