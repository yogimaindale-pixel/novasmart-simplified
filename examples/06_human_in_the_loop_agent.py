# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 6: HUMAN-IN-THE-LOOP (HITL) APPROVAL AGENT
# ==============================================================================
# File: examples/06_human_in_the_loop_agent.py
# Level: Enterprise / Junior Developer Friendly
# Purpose: Demonstrates how AI agents pause execution for human manager approval.
# Run on local laptop: python3 06_human_in_the_loop_agent.py
# ==============================================================================

# Import built-in JSON module for structured serialization.
import json

# Import SQLite module for database operations.
import sqlite3

# Import uuid library to generate approval tokens.
import uuid

# Import typing annotations for type safety.
from typing import Dict, Any, Optional


# ------------------------------------------------------------------------------
# DATABASE SETUP FOR HUMAN APPROVAL WORKFLOWS
# ------------------------------------------------------------------------------

def setup_hitl_database() -> sqlite3.Connection:
    """
    Sets up an in-memory SQLite database for pending action approvals.
    """
    # Open SQLite in-memory database connection.
    conn = sqlite3.connect(":memory:")
    # Obtain cursor object.
    cursor = conn.cursor()
    
    # Create pending approvals table.
    cursor.execute("""
        CREATE TABLE pending_approvals (
            token_id TEXT PRIMARY KEY,
            requested_by_agent TEXT NOT NULL,
            action_type TEXT NOT NULL,
            target_id TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)
    
    # Commit changes.
    conn.commit()
    # Return database connection.
    return conn


# ------------------------------------------------------------------------------
# HUMAN-IN-THE-LOOP (HITL) AGENT CLASS
# ------------------------------------------------------------------------------

class HumanInTheLoopAgent:
    """
    An AI Agent that automatically executes low-value actions (< $500),
    but pauses and generates approval tokens for high-value actions (>= $500).
    """

    def __init__(self, agent_name: str, db_conn: sqlite3.Connection):
        """
        Constructor initializing agent identity and approval database connection.
        """
        self.agent_name = agent_name
        self.db_conn = db_conn
        # High value threshold requiring human authorization.
        self.approval_threshold = 500.00

    def request_action(self, action_type: str, target_id: str, amount: float) -> Dict[str, Any]:
        """
        Processes an action request. Auto-approves under threshold; pauses for HITL approval if over threshold.
        """
        print(f"\n[{self.agent_name}] Evaluating action '{action_type}' for target '{target_id}' with amount ${amount:.2f}")
        
        # Check if amount requires human approval.
        requires_human_approval = amount >= self.approval_threshold
        
        if not requires_human_approval:
            # Auto-approve action under threshold.
            return {
                "agent_name": self.agent_name,
                "status": "AUTO_APPROVED",
                "action_type": action_type,
                "target_id": target_id,
                "amount": amount,
                "approval_token": None,
                "message": "Action auto-approved under threshold."
            }
        else:
            # Generate unique approval token ID.
            token_id = f"TOKEN-{uuid.uuid4().hex[:8].upper()}"
            
            # Store pending approval record in database.
            cursor = self.db_conn.cursor()
            cursor.execute(
                "INSERT INTO pending_approvals VALUES (?, ?, ?, ?, ?, ?)",
                (token_id, self.agent_name, action_type, target_id, amount, "PENDING_HUMAN_REVIEW")
            )
            self.db_conn.commit()
            
            # Return paused HITL payload.
            return {
                "agent_name": self.agent_name,
                "status": "PAUSED_AWAITING_APPROVAL",
                "action_type": action_type,
                "target_id": target_id,
                "amount": amount,
                "approval_token": token_id,
                "message": f"Action exceeds ${self.approval_threshold:.2f} threshold. Human manager approval required."
            }

    def execute_approved_action(self, token_id: str, manager_decision: str) -> Dict[str, Any]:
        """
        Resumes and executes a paused action once a human manager provides a decision ('APPROVE' or 'REJECT').
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT token_id, action_type, target_id, amount, status FROM pending_approvals WHERE token_id = ?", (token_id,))
        row = cursor.fetchone()
        
        if not row:
            return {
                "agent_name": self.agent_name,
                "status": "INVALID_TOKEN",
                "message": f"Approval token '{token_id}' not found."
            }
            
        new_status = "EXECUTED" if manager_decision.upper() == "APPROVE" else "REJECTED_BY_MANAGER"
        cursor.execute("UPDATE pending_approvals SET status = ? WHERE token_id = ?", (new_status, token_id))
        self.db_conn.commit()
        
        return {
            "agent_name": self.agent_name,
            "status": new_status,
            "approval_token": token_id,
            "action_type": row[1],
            "target_id": row[2],
            "amount": row[3],
            "manager_decision": manager_decision.upper()
        }


# ------------------------------------------------------------------------------
# LOCAL LAPTOP EXECUTION ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    print("==========================================================")
    print("  RUNNING LESSON 6: HUMAN-IN-THE-LOOP (HITL) APPROVAL AGENT")
    print("==========================================================")

    # Initialize HITL database.
    db = setup_hitl_database()

    # Instantiate HITL Agent.
    hitl_agent = HumanInTheLoopAgent("NovaSmart HITL Refund Agent", db)

    # Test Case 1: Low-value refund (Auto-approved).
    res_1 = hitl_agent.request_action("REFUND", "ORD-101", 75.00)
    print("\n--- Test Case 1 (Low-Value) Output ---")
    print(json.dumps(res_1, indent=2))

    # Test Case 2: High-value refund (Paused awaiting human approval).
    res_2 = hitl_agent.request_action("REFUND", "ORD-102", 1200.00)
    print("\n--- Test Case 2 (High-Value) Output ---")
    print(json.dumps(res_2, indent=2))

    # Test Case 3: Human Manager Approves the paused action using the token.
    token = res_2["approval_token"]
    res_3 = hitl_agent.execute_approved_action(token, "APPROVE")
    print("\n--- Test Case 3 (Human Manager Approval Executed) Output ---")
    print(json.dumps(res_3, indent=2))
