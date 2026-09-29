# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 5: FINANCIAL & FRAUD AUDIT MULTI-AGENT SYSTEM
# ==============================================================================
# File: examples/05_financial_audit_multi_agent.py
# Level: Enterprise / Junior Developer Friendly
# Purpose: Demonstrates a 3-agent financial transaction audit & fraud detection system.
# Run on local laptop: python3 05_financial_audit_multi_agent.py
# ==============================================================================

# Import built-in JSON library for serialization.
import json

# Import SQLite module for database simulation.
import sqlite3

# Import typing module for type safety.
from typing import Dict, Any, List, Optional


# ------------------------------------------------------------------------------
# SECTION 1: DATABASE INITIALIZATION FOR FINANCIAL TRANSACTIONS
# ------------------------------------------------------------------------------

def setup_financial_database() -> sqlite3.Connection:
    """
    Sets up an in-memory SQLite database storing retail transactions and audit risk rules.
    """
    # Open SQLite in-memory database connection.
    conn = sqlite3.connect(":memory:")
    # Obtain cursor object.
    cursor = conn.cursor()
    
    # Create transactions table.
    cursor.execute("""
        CREATE TABLE transactions (
            tx_id TEXT PRIMARY KEY,
            account_id TEXT NOT NULL,
            amount REAL NOT NULL,
            currency TEXT NOT NULL,
            merchant TEXT NOT NULL,
            country TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    
    # Insert sample financial transactions.
    cursor.executemany("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?)", [
        ("TX-5001", "ACC-101", 250.00, "USD", "NovaSmart Online Store", "US", "2026-09-29 08:00:00"),
        ("TX-5002", "ACC-101", 12500.00, "USD", "Luxury Jewelers Foreign", "UK", "2026-09-29 08:05:00")
    ])
    
    # Save transactions to memory.
    conn.commit()
    # Return database connection.
    return conn


# ------------------------------------------------------------------------------
# SECTION 2: SUB-AGENT 1 - HIGH-VALUE TRANSACTION AUDIT SUB-AGENT
# ------------------------------------------------------------------------------

class HighValueAuditSubAgent:
    """
    Sub-Agent specialized in checking transactions exceeding threshold values ($10,000 USD).
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Initializes sub-agent with database tool connection.
        """
        self.agent_name = "High-Value Transaction Audit Sub-Agent"
        self.db_conn = db_conn
        # Define high value reporting threshold limit.
        self.threshold = 10000.00

    def audit_transaction_value(self, tx_id: str) -> Dict[str, Any]:
        """
        Queries transaction amount and checks if high-value regulatory flag is required.
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT tx_id, account_id, amount, currency, merchant FROM transactions WHERE tx_id = ?", (tx_id,))
        row = cursor.fetchone()
        
        if not row:
            return {
                "sub_agent": self.agent_name,
                "status": "NOT_FOUND",
                "message": f"Transaction '{tx_id}' was not found in transactions database."
            }
            
        amount = row[2]
        is_high_value = amount >= self.threshold
        
        return {
            "sub_agent": self.agent_name,
            "status": "SUCCESS",
            "transaction_id": row[0],
            "account_id": row[1],
            "amount": amount,
            "currency": row[3],
            "merchant": row[4],
            "high_value_flag": is_high_value,
            "compliance_action": "REPORT_CTR" if is_high_value else "NONE"
        }


# ------------------------------------------------------------------------------
# SECTION 3: SUB-AGENT 2 - FRAUD RISK SUB-AGENT
# ------------------------------------------------------------------------------

class FraudRiskSubAgent:
    """
    Sub-Agent specialized in detecting location anomalies and rapid velocity risk.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Initializes sub-agent with database tool connection.
        """
        self.agent_name = "Fraud Risk Sub-Agent"
        self.db_conn = db_conn

    def evaluate_fraud_risk(self, account_id: str) -> Dict[str, Any]:
        """
        Evaluates geographic risk across account transactions.
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT tx_id, amount, country, timestamp FROM transactions WHERE account_id = ?", (account_id,))
        rows = cursor.fetchall()
        
        distinct_countries = set([r[2] for r in rows])
        transaction_count = len(rows)
        # Risk flagged if transactions originate from multiple countries within short window.
        has_geographic_anomaly = len(distinct_countries) > 1
        
        risk_score = 85 if has_geographic_anomaly else 10
        
        return {
            "sub_agent": self.agent_name,
            "status": "SUCCESS",
            "account_id": account_id,
            "transaction_count": transaction_count,
            "countries_involved": list(distinct_countries),
            "geographic_anomaly_detected": has_geographic_anomaly,
            "risk_score": risk_score,
            "risk_level": "HIGH" if risk_score > 50 else "LOW"
        }


# ------------------------------------------------------------------------------
# SECTION 4: AUDIT SUPERVISOR / COORDINATOR AGENT
# ------------------------------------------------------------------------------

class AuditSupervisorAgent:
    """
    Master Audit Supervisor Agent orchestrating high-value audit and fraud detection sub-agents.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Initializes Audit Supervisor and sub-agents.
        """
        self.agent_name = "Audit Supervisor Agent"
        self.value_agent = HighValueAuditSubAgent(db_conn)
        self.fraud_agent = FraudRiskSubAgent(db_conn)

    def run_full_audit(self, tx_id: str) -> Dict[str, Any]:
        """
        Executes complete multi-agent compliance and risk audit for a transaction.
        """
        print(f"\n[{self.agent_name}] Initiating multi-agent audit for transaction: '{tx_id}'")
        
        # Step 1: Execute High-Value Transaction Audit Sub-Agent.
        value_audit = self.value_agent.audit_transaction_value(tx_id)
        
        if value_audit["status"] != "SUCCESS":
            return {
                "supervisor": self.agent_name,
                "status": "FAILED",
                "message": value_audit["message"]
            }
            
        account_id = value_audit["account_id"]
        
        # Step 2: Execute Fraud Risk Sub-Agent for target account.
        fraud_audit = self.fraud_agent.evaluate_fraud_risk(account_id)
        
        # Step 3: Determine overall audit decision.
        requires_hold = value_audit["high_value_flag"] or fraud_audit["risk_level"] == "HIGH"
        
        return {
            "supervisor": self.agent_name,
            "status": "AUDIT_COMPLETED",
            "audited_tx_id": tx_id,
            "account_id": account_id,
            "audit_decision": "HOLD_FOR_REVIEW" if requires_hold else "APPROVED",
            "value_audit_summary": value_audit,
            "fraud_audit_summary": fraud_audit,
            "audit_trail": [value_audit, fraud_audit]
        }


# ------------------------------------------------------------------------------
# LOCAL LAPTOP EXECUTION ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    print("==========================================================")
    print("  RUNNING LESSON 5: FINANCIAL AUDIT MULTI-AGENT SYSTEM")
    print("==========================================================")

    # Initialize financial database.
    db = setup_financial_database()

    # Instantiate Audit Supervisor Agent.
    supervisor = AuditSupervisorAgent(db)

    # Test Case 1: Standard transaction audit.
    audit_1 = supervisor.run_full_audit("TX-5001")
    print("\n--- Test Case 1 (Standard Tx) Output ---")
    print(json.dumps(audit_1, indent=2))

    # Test Case 2: High-value foreign transaction audit.
    audit_2 = supervisor.run_full_audit("TX-5002")
    print("\n--- Test Case 2 (High-Value Foreign Tx) Output ---")
    print(json.dumps(audit_2, indent=2))
