# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 3: COMPLEX MULTI-AGENT COORDINATION SYSTEM
# ==============================================================================
# File: examples/03_complex_multi_agent.py
# Level: Advanced / Enterprise Developer
# Purpose: Demonstrates Multi-Agent System architecture with Router Agent,
#          specialized Sub-agents, shared state, and tool orchestration.
# ==============================================================================

# Import built-in JSON module for structured data formatting.
import json

# Import SQLite module for database simulation.
import sqlite3

# Import typing primitives for strict type safety.
from typing import Dict, Any, List, Optional


# ------------------------------------------------------------------------------
# DATABASE CONNECTOR SETUP
# ------------------------------------------------------------------------------

def initialize_enterprise_database() -> sqlite3.Connection:
    """
    Creates an enterprise retail SQLite database with products and price-match data.

    Returns:
        sqlite3.Connection: Active database connection.
    """
    # Open SQLite in-memory database connection.
    conn = sqlite3.connect(":memory:")
    # Obtain cursor object.
    cursor = conn.cursor()
    
    # Create products inventory table.
    cursor.execute("""
        CREATE TABLE products (
            sku TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    
    # Create competitor pricing table for price matching agent.
    cursor.execute("""
        CREATE TABLE competitor_prices (
            competitor_name TEXT NOT NULL,
            sku TEXT NOT NULL,
            competitor_price REAL NOT NULL,
            FOREIGN KEY (sku) REFERENCES products(sku)
        )
    """)
    
    # Insert product records into inventory table.
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", [
        ("SKU-201", "NovaSmart 4K Monitor", 299.99, 15),
        ("SKU-202", "NovaSmart Mechanical Keyboard", 89.99, 45)
    ])
    
    # Insert competitor price records.
    cursor.executemany("INSERT INTO competitor_prices VALUES (?, ?, ?)", [
        ("TechSuperstore", "SKU-201", 279.99),
        ("ElectroMart", "SKU-202", 94.99)
    ])
    
    # Save database insertions to memory.
    conn.commit()
    # Return database connection.
    return conn


# ------------------------------------------------------------------------------
# SPECIALIZED SUB-AGENT 1: CATALOG & INVENTORY SUB-AGENT
# ------------------------------------------------------------------------------

class CatalogInventorySubAgent:
    """
    Specialized Sub-Agent responsible for product queries and stock checks.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Constructor setting database connection.
        """
        self.sub_agent_name = "Catalog & Inventory Sub-Agent"
        self.db_conn = db_conn

    def execute_stock_check(self, item_keyword: str) -> Dict[str, Any]:
        """
        Queries product stock details from database.
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT sku, name, price, stock FROM products WHERE name LIKE ?", (f"%{item_keyword}%",))
        rows = cursor.fetchall()
        
        results = []
        for r in rows:
            results.append({
                "sku": r[0],
                "name": r[1],
                "price": r[2],
                "stock": r[3]
            })
            
        return {
            "sub_agent": self.sub_agent_name,
            "status": "SUCCESS",
            "products_found": results
        }


# ------------------------------------------------------------------------------
# SPECIALIZED SUB-AGENT 2: PRICE MATCHER SUB-AGENT
# ------------------------------------------------------------------------------

class PriceMatcherSubAgent:
    """
    Specialized Sub-Agent responsible for competitor price comparison and price matching logic.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Constructor setting database connection.
        """
        self.sub_agent_name = "Price Matcher Sub-Agent"
        self.db_conn = db_conn

    def execute_price_match(self, sku: str) -> Dict[str, Any]:
        """
        Compares NovaSmart product price against competitor pricing data.
        """
        cursor = self.db_conn.cursor()
        # Query product price and competitor price using a SQL JOIN statement.
        sql = """
            SELECT p.name, p.price, c.competitor_name, c.competitor_price
            FROM products p
            JOIN competitor_prices c ON p.sku = c.sku
            WHERE p.sku = ?
        """
        cursor.execute(sql, (sku,))
        row = cursor.fetchone()
        
        if not row:
            return {
                "sub_agent": self.sub_agent_name,
                "status": "NO_COMPETITOR_DATA",
                "message": f"No competitor pricing available for SKU '{sku}'."
            }
            
        novasmart_price = row[1]
        competitor_price = row[3]
        can_price_match = competitor_price < novasmart_price
        match_discount = novasmart_price - competitor_price if can_price_match else 0.0
        
        return {
            "sub_agent": self.sub_agent_name,
            "status": "SUCCESS",
            "product_name": row[0],
            "novasmart_price": novasmart_price,
            "competitor_name": row[2],
            "competitor_price": competitor_price,
            "price_match_eligible": can_price_match,
            "potential_discount": round(match_discount, 2)
        }


# ------------------------------------------------------------------------------
# COORDINATOR / ROUTER AGENT: MULTI-AGENT SYSTEM ORCHESTRATOR
# ------------------------------------------------------------------------------

class NovaSmartCoordinatorAgent:
    """
    Main Coordinator Agent that routes user prompts to specialized sub-agents
    and aggregates multi-agent findings into a final response.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Constructor instantiating specialized sub-agents and coordinator state.
        """
        self.agent_name = "NovaSmart System Coordinator"
        # Instantiate Catalog Sub-Agent.
        self.catalog_agent = CatalogInventorySubAgent(db_conn)
        # Instantiate Price Matcher Sub-Agent.
        self.price_matcher_agent = PriceMatcherSubAgent(db_conn)

    def route_and_execute(self, user_prompt: str) -> Dict[str, Any]:
        """
        Analyzes incoming prompt, orchestrates sub-agents, and returns multi-agent execution payload.
        """
        print(f"\n[{self.agent_name}] Received enterprise request: '{user_prompt}'")
        execution_trace = []
        
        # Step 1: Execute Catalog Sub-Agent to retrieve product details.
        item_keyword = "Monitor" if "monitor" in user_prompt.lower() else "Keyboard"
        catalog_result = self.catalog_agent.execute_stock_check(item_keyword)
        execution_trace.append(catalog_result)
        
        # Check if products were found.
        products = catalog_result.get("products_found", [])
        price_match_results = []
        
        # Step 2: If prompt mentions price match, execute Price Matcher Sub-Agent for found products.
        if "match" in user_prompt.lower() or "price" in user_prompt.lower():
            for prod in products:
                prod_sku = prod["sku"]
                pm_result = self.price_matcher_agent.execute_price_match(prod_sku)
                price_match_results.append(pm_result)
                execution_trace.append(pm_result)

        # Step 3: Aggregate sub-agent outputs into final response payload.
        return {
            "coordinator": self.agent_name,
            "status": "COMPLETED",
            "request": user_prompt,
            "sub_agent_count": len(execution_trace),
            "catalog_summary": catalog_result,
            "price_match_summary": price_match_results,
            "audit_trail": execution_trace
        }


# Execution block when running directly from terminal.
if __name__ == "__main__":
    print("==========================================================")
    print("  RUNNING LESSON 3: COMPLEX MULTI-AGENT COORDINATION SYSTEM")
    print("==========================================================")

    # Initialize enterprise database.
    db = initialize_enterprise_database()

    # Instantiate Coordinator Agent.
    coordinator = NovaSmartCoordinatorAgent(db)

    # Test multi-agent orchestration for product inquiry and price match query.
    complex_request = "Can you find the NovaSmart 4K Monitor and check if we can price match competitors?"
    result_payload = coordinator.route_and_execute(complex_request)

    # Print pretty-printed JSON audit output.
    print("\n--- Multi-Agent Execution Result ---")
    print(json.dumps(result_payload, indent=2))
