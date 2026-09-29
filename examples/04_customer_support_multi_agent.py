# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 4: CUSTOMER SUPPORT MULTI-AGENT SYSTEM
# ==============================================================================
# File: examples/04_customer_support_multi_agent.py
# Level: Enterprise / Junior Developer Friendly
# Purpose: Demonstrates a fully working 4-agent customer support system.
# Run on local laptop: python3 04_customer_support_multi_agent.py
# ==============================================================================

# Import built-in JSON module to serialize dictionary responses.
import json

# Import SQLite library to simulate customer order and refund databases.
import sqlite3

# Import typing hints for strict parameter and return type signatures.
from typing import Dict, Any, List, Optional


# ------------------------------------------------------------------------------
# SECTION 1: DATABASE INITIALIZATION FOR CUSTOMER SUPPORT
# ------------------------------------------------------------------------------

def setup_support_database() -> sqlite3.Connection:
    """
    Sets up an in-memory SQLite database storing orders, shipping, and returns.
    """
    # Open SQLite in-memory database connection.
    conn = sqlite3.connect(":memory:")
    # Obtain a database cursor to execute SQL statements.
    cursor = conn.cursor()
    
    # Create orders table.
    cursor.execute("""
        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            customer_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            status TEXT NOT NULL,
            tracking_number TEXT NOT NULL
        )
    """)
    
    # Create returns table.
    cursor.execute("""
        CREATE TABLE returns (
            return_id TEXT PRIMARY KEY,
            order_id TEXT NOT NULL,
            refund_amount REAL NOT NULL,
            return_status TEXT NOT NULL
        )
    """)
    
    # Insert sample order records.
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?)", [
        ("ORD-901", "Alice Smith", "NovaSmart Wireless Earbuds", "SHIPPED", "TRK-88102"),
        ("ORD-902", "Bob Jones", "NovaSmart 4K Monitor", "PROCESSING", "TRK-88103")
    ])
    
    # Insert sample return records.
    cursor.executemany("INSERT INTO returns VALUES (?, ?, ?, ?)", [
        ("RET-101", "ORD-901", 49.99, "REFUND_APPROVED")
    ])
    
    # Commit table creation and inserts to memory.
    conn.commit()
    # Return database connection.
    return conn


# ------------------------------------------------------------------------------
# SECTION 2: SUB-AGENT 1 - ORDER & SHIPPING SUB-AGENT
# ------------------------------------------------------------------------------

class ShippingSubAgent:
    """
    Sub-Agent specialized in checking order status and tracking details.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Initializes sub-agent with database tool connection.
        """
        self.agent_name = "Order & Shipping Sub-Agent"
        self.db_conn = db_conn

    def check_order_status(self, order_id: str) -> Dict[str, Any]:
        """
        Queries order status and tracking details from SQLite database.
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT order_id, customer_name, item_name, status, tracking_number FROM orders WHERE order_id = ?", (order_id,))
        row = cursor.fetchone()
        
        if not row:
            return {
                "sub_agent": self.agent_name,
                "status": "NOT_FOUND",
                "message": f"Order '{order_id}' was not found in NovaSmart orders database."
            }
            
        return {
            "sub_agent": self.agent_name,
            "status": "SUCCESS",
            "order_details": {
                "order_id": row[0],
                "customer_name": row[1],
                "item_name": row[2],
                "order_status": row[3],
                "tracking_number": row[4]
            }
        }


# ------------------------------------------------------------------------------
# SECTION 3: SUB-AGENT 2 - RETURNS & REFUNDS SUB-AGENT
# ------------------------------------------------------------------------------

class RefundSubAgent:
    """
    Sub-Agent specialized in checking return eligibility and refund statuses.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Initializes sub-agent with database tool connection.
        """
        self.agent_name = "Returns & Refunds Sub-Agent"
        self.db_conn = db_conn

    def check_refund_status(self, order_id: str) -> Dict[str, Any]:
        """
        Queries refund status details from SQLite returns database.
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT return_id, order_id, refund_amount, return_status FROM returns WHERE order_id = ?", (order_id,))
        row = cursor.fetchone()
        
        if not row:
            return {
                "sub_agent": self.agent_name,
                "status": "NO_RETURN_RECORD",
                "message": f"No return or refund request found for order '{order_id}'."
            }
            
        return {
            "sub_agent": self.agent_name,
            "status": "SUCCESS",
            "refund_details": {
                "return_id": row[0],
                "order_id": row[1],
                "refund_amount": row[2],
                "return_status": row[3]
            }
        }


# ------------------------------------------------------------------------------
# SECTION 4: TRIAGE / ROUTER AGENT
# ------------------------------------------------------------------------------

class SupportTriageAgent:
    """
    Master Triage Agent that routes incoming customer prompts to specialized sub-agents.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Initializes Triage Agent and specialized sub-agents.
        """
        self.agent_name = "Support Triage Router Agent"
        self.shipping_agent = ShippingSubAgent(db_conn)
        self.refund_agent = RefundSubAgent(db_conn)

    def process_customer_prompt(self, user_prompt: str, order_id: str) -> Dict[str, Any]:
        """
        Evaluates customer prompt intent, routes to sub-agents, and aggregates output.
        """
        print(f"\n[{self.agent_name}] Routing prompt: '{user_prompt}' for Order: '{order_id}'")
        sub_agent_audits = []
        
        # Check if shipping or order tracking is requested.
        is_shipping_query = "where" in user_prompt.lower() or "shipping" in user_prompt.lower() or "track" in user_prompt.lower() or "order" in user_prompt.lower()
        # Check if refund or return status is requested.
        is_refund_query = "refund" in user_prompt.lower() or "return" in user_prompt.lower() or "money" in user_prompt.lower()
        
        # Route to Shipping Sub-Agent if shipping query.
        if is_shipping_query:
            shipping_res = self.shipping_agent.check_order_status(order_id)
            sub_agent_audits.append(shipping_res)
            
        # Route to Refund Sub-Agent if refund query.
        if is_refund_query:
            refund_res = self.refund_agent.check_refund_status(order_id)
            sub_agent_audits.append(refund_res)
            
        # Aggregate results into structured JSON response.
        return {
            "triage_agent": self.agent_name,
            "user_prompt": user_prompt,
            "target_order_id": order_id,
            "sub_agents_executed": len(sub_agent_audits),
            "results": sub_agent_audits
        }


# ------------------------------------------------------------------------------
# LOCAL LAPTOP EXECUTION ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    print("==========================================================")
    print("  RUNNING LESSON 4: CUSTOMER SUPPORT MULTI-AGENT SYSTEM")
    print("==========================================================")

    # Initialize support database.
    db = setup_support_database()

    # Instantiate Triage Router Agent.
    triage_agent = SupportTriageAgent(db)

    # Test Case 1: Order tracking query.
    test_1 = triage_agent.process_customer_prompt("Where is my order and tracking number?", "ORD-901")
    print("\n--- Test Case 1 Output ---")
    print(json.dumps(test_1, indent=2))

    # Test Case 2: Combined tracking and refund query.
    test_2 = triage_agent.process_customer_prompt("Check order status and refund status for my return", "ORD-901")
    print("\n--- Test Case 2 Output ---")
    print(json.dumps(test_2, indent=2))
