# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 2: INTERMEDIATE AGENT WITH TOOL CALLING
# ==============================================================================
# File: examples/02_intermediate_agent.py
# Level: Intermediate / Junior Developer
# Purpose: Demonstrates how an AI agent uses tools (functions) to query databases.
# ==============================================================================

# Import built-in JSON library for structured output serialization.
import json

# Import built-in SQLite database engine to simulate a backend inventory database.
import sqlite3

# Import typing modules to provide type hints for variables and functions.
from typing import Dict, Any, List, Optional


# Define a database initialization helper function.
def setup_inventory_database() -> sqlite3.Connection:
    """
    Creates an in-memory database populated with sample retail inventory records.

    Returns:
        sqlite3.Connection: Active database connection.
    """
    # Open an in-memory SQLite database connection.
    conn = sqlite3.connect(":memory:")
    # Obtain a database cursor to execute SQL commands.
    cursor = conn.cursor()
    # Create the inventory table schema.
    cursor.execute("""
        CREATE TABLE inventory (
            item_id TEXT PRIMARY KEY,
            item_name TEXT NOT NULL,
            unit_price REAL NOT NULL,
            quantity_available INTEGER NOT NULL
        )
    """)
    # Insert sample product inventory records.
    cursor.executemany("""
        INSERT INTO inventory VALUES (?, ?, ?, ?)
    """, [
        ("SKU-1001", "NovaSmart HD Web Camera", 59.99, 42),
        ("SKU-1002", "NovaSmart Ergonomic Keyboard", 79.99, 18),
        ("SKU-1003", "NovaSmart Noise Cancelling Headset", 129.99, 0)
    ])
    # Commit table creation and inserts to database memory.
    conn.commit()
    # Return the active connection object.
    return conn


# Define the IntermediateToolAgent class.
class IntermediateToolAgent:
    """
    An AI agent that inspects user queries, determines necessary tool executions,
    calls data tools safely, and returns audited response structures.
    """

    def __init__(self, agent_name: str, db_connection: sqlite3.Connection):
        """
        Constructor initializing agent identity and database tool bindings.
        """
        # Set agent human-readable name.
        self.agent_name = agent_name
        # Store database connection reference for tool calls.
        self.db_connection = db_connection

    def tool_lookup_inventory(self, sku_or_name: str) -> Dict[str, Any]:
        """
        Tool Function: Queries the database for stock availability of a product.

        Args:
            sku_or_name (str): Product SKU ID or product name keyword.

        Returns:
            Dict[str, Any]: Query result status and item details payload.
        """
        # Obtain a database cursor object.
        cursor = self.db_connection.cursor()
        # Define parameterized SQL query string to prevent SQL injection vulnerabilities.
        sql_query = """
            SELECT item_id, item_name, unit_price, quantity_available
            FROM inventory
            WHERE item_id = ? OR item_name LIKE ?
        """
        # Execute query passing parameters safely.
        cursor.execute(sql_query, (sku_or_name, f"%{sku_or_name}%"))
        # Fetch all matching rows returned by SQLite.
        matching_rows = cursor.fetchall()

        # Check if no matching items were found in the database.
        if not matching_rows:
            return {
                "tool_name": "lookup_inventory",
                "status": "NOT_FOUND",
                "items": []
            }

        # Transform database tuple rows into structured dictionary objects.
        items_found = []
        for row in matching_rows:
            items_found.append({
                "item_id": row[0],
                "item_name": row[1],
                "unit_price": row[2],
                "quantity_available": row[3],
                "in_stock": row[3] > 0
            })

        # Return tool execution success response containing items payload.
        return {
            "tool_name": "lookup_inventory",
            "status": "SUCCESS",
            "items": items_found
        }

    def process_query(self, user_query: str) -> Dict[str, Any]:
        """
        Processes incoming user prompt, routes tool calls, and returns final output.
        """
        # Clean user query text string.
        query_clean = user_query.strip()
        # Log processing event to terminal output.
        print(f"[{self.agent_name}] Evaluating query: '{query_clean}'")

        # Intent evaluation: Check if prompt asks about stock or product details.
        if "stock" in query_clean.lower() or "camera" in query_clean.lower() or "keyboard" in query_clean.lower() or "headset" in query_clean.lower():
            # Extract target search term from query text.
            search_keyword = "Camera" if "camera" in query_clean.lower() else ("Keyboard" if "keyboard" in query_clean.lower() else "Headset")
            # Invoke the inventory lookup tool.
            tool_result = self.tool_lookup_inventory(search_keyword)
            # Formulate human-readable reply message based on tool output.
            if tool_result["status"] == "SUCCESS":
                found_count = len(tool_result["items"])
                reply_message = f"Found {found_count} matching product(s) in NovaSmart inventory."
            else:
                reply_message = f"No product matching '{search_keyword}' was found in stock."

            # Package audit payload.
            return {
                "agent_name": self.agent_name,
                "status": "SUCCESS",
                "user_query": query_clean,
                "reply": reply_message,
                "tool_audit": tool_result
            }
        else:
            # Fallback response when no tool calls are needed.
            return {
                "agent_name": self.agent_name,
                "status": "SUCCESS",
                "user_query": query_clean,
                "reply": "I can help check NovaSmart inventory stock. Try asking about 'camera' or 'keyboard'.",
                "tool_audit": None
            }


# Execution block when running script directly from terminal.
if __name__ == "__main__":
    # Print lesson banner.
    print("==================================================")
    print("  RUNNING LESSON 2: INTERMEDIATE TOOL-USING AGENT")
    print("==================================================")

    # Step 1: Set up sample database connection.
    db_conn = setup_inventory_database()

    # Step 2: Instantiate IntermediateToolAgent.
    inventory_agent = IntermediateToolAgent(
        agent_name="NovaSmart Inventory Tool Agent",
        db_connection=db_conn
    )

    # Step 3: Run test query for stock lookup tool execution.
    query_result_1 = inventory_agent.process_query("Is the NovaSmart HD Web Camera in stock?")
    print("\n--- Query 1 Result ---")
    print(json.dumps(query_result_1, indent=2))

    # Step 4: Run test query for out-of-stock item lookup.
    query_result_2 = inventory_agent.process_query("Check stock for NovaSmart Noise Cancelling Headset")
    print("\n--- Query 2 Result ---")
    print(json.dumps(query_result_2, indent=2))
