# 📌 01. NovaSmart Simplified AI Agent Framework - Repository Overview

## 🎯 Executive Summary & Problem Statement
Building enterprise AI Agent applications requires clean integration between tool execution, database query engines, structured JSON payload responses, Agent-to-User Interface (A2UI) rendering callbacks, RAG vector retrieval, and memory bank state management.

The **NovaSmart Simplified AI Agent Framework (`novasmart-simplified`)** provides a zero-dependency, lightweight Python framework establishing clean tool dispatch, SQLite relational query execution, structured JSON agent responses, and modular AGY `.agents/skills/` extensions (`enable-a2ui`, `build-rag`, `setup-memory-bank`, `build-agent-frontend`).

---

## 🏗️ Architecture & Component Overview

```
                            User Prompt Input
                                    │
                                    ▼
                     ┌──────────────────────────────┐
                     │     NovaSmartAgent Engine    │ (novasmart_agent_framework.py)
                     └──────────────┬───────────────┘
                                    │
            ┌───────────────────────┴───────────────────────┐
            │ Tool Registry Dispatch                        │
            ▼                                               ▼
┌───────────────────────────────────────┐ ┌───────────────────────────────────┐
│ query_retail_database(query)          │ │ A2UI Callback Renderer            │
│ (SQLite / initialize_demo_database)   │ │ (a2ui_utils.py)                   │
└───────────────────┬───────────────────┘ └─────────────────┬─────────────────┘
                    │                                       │
                    └───────────────────┬───────────────────┘
                                        │
                                        ▼
                             Structured JSON Response
```

---

## 🛠️ Technology Stack & Dependencies
- **Core Language**: Python 3.10+ (Standard Library `sqlite3`, `json`, `logging`)
- **Agent Architecture**: `NovaSmartAgent` (`novasmart_agent_framework.py`)
- **UI Extensions**: Agent-to-User Interface (A2UI) callbacks (`.agents/skills/enable-a2ui/template/a2ui_utils.py`)
- **RAG & Memory Skills**: RAG compatibility tester (`test_rag_a2ui_compat.py`), Memory Bank setup (`setup-memory-bank`), Frontend builder (`build-agent-frontend`)
