# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 8: SECURITY GOVERNANCE MULTI-AGENT ESTATE
# ==============================================================================
# File: examples/08_autonomous_governance_multi_agent.py
# Level: Enterprise / Junior Developer Friendly
# Purpose: Demonstrates autonomous AI governance, shadow agent discovery,
#          identity right-sizing, and content screening for NovaSmart.
# Run on local laptop: python3 08_autonomous_governance_multi_agent.py
# ==============================================================================

# Import built-in JSON module for structured outputs.
import json

# Import SQLite module for backend estate database simulation.
import sqlite3

# Import typing primitives for type definitions.
from typing import Dict, Any, List, Optional


# ------------------------------------------------------------------------------
# SECTION 1: ESTATE DATABASE SETUP FOR NOVASMART GOVERNANCE
# ------------------------------------------------------------------------------

def setup_governance_database() -> sqlite3.Connection:
    """
    Sets up an in-memory database representing NovaSmart's registered agents,
    shared identities (logins/service accounts), and content security rules.
    """
    # Open SQLite in-memory database connection.
    conn = sqlite3.connect(":memory:")
    # Obtain cursor object.
    cursor = conn.cursor()
    
    # Create Agent Registry table.
    cursor.execute("""
        CREATE TABLE agent_registry (
            agent_id TEXT PRIMARY KEY,
            agent_name TEXT NOT NULL,
            is_registered BOOLEAN NOT NULL,
            service_account_identity TEXT NOT NULL,
            role_scope TEXT NOT NULL
        )
    """)
    
    # Insert registered and shadow agents into estate database.
    cursor.executemany("INSERT INTO agent_registry VALUES (?, ?, ?, ?, ?)", [
        ("AGT-001", "NovaSmart Main Storefront Agent", 1, "store-portal-login", "roles/viewer"),
        ("AGT-002", "NovaSmart Inventory Sync Agent", 1, "inventory-login", "roles/editor"),
        ("SHADOW-99", "Promo Agent Shadow Workload", 0, "store-portal-login", "roles/owner")
    ])
    
    # Commit changes.
    conn.commit()
    # Return active database connection.
    return conn


# ------------------------------------------------------------------------------
# SECTION 2: SUB-AGENT 1 - SHADOW AGENT DISCOVERY SUB-AGENT
# ------------------------------------------------------------------------------

class ShadowAgentDiscoverySubAgent:
    """
    Sub-Agent specialized in scanning the cloud estate to discover unregistered shadow agents.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Constructor setting database connection.
        """
        self.agent_name = "Shadow Agent Discovery Sub-Agent"
        self.db_conn = db_conn

    def discover_shadow_agents(self) -> Dict[str, Any]:
        """
        Scans agent registry database for workloads where is_registered == 0.
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT agent_id, agent_name, service_account_identity, role_scope FROM agent_registry WHERE is_registered = 0")
        rows = cursor.fetchall()
        
        shadow_list = []
        for r in rows:
            shadow_list.append({
                "agent_id": r[0],
                "agent_name": r[1],
                "shared_login": r[2],
                "assigned_role": r[3]
            })
            
        return {
            "sub_agent": self.agent_name,
            "status": "SHADOW_AGENTS_FOUND" if shadow_list else "CLEAN",
            "shadow_agent_count": len(shadow_list),
            "shadow_agents": shadow_list
        }


# ------------------------------------------------------------------------------
# SECTION 3: SUB-AGENT 2 - IDENTITY & ACCESS RIGHT-SIZING SUB-AGENT
# ------------------------------------------------------------------------------

class IdentityRightSizingSubAgent:
    """
    Sub-Agent specialized in detecting shared logins (service accounts) and over-privileged roles.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Constructor setting database connection.
        """
        self.agent_name = "Identity & Access Right-Sizing Sub-Agent"
        self.db_conn = db_conn

    def audit_identities(self) -> Dict[str, Any]:
        """
        Scans for shared service account logins and excessive role privileges (e.g. roles/owner).
        """
        cursor = self.db_conn.cursor()
        cursor.execute("SELECT service_account_identity, COUNT(*) FROM agent_registry GROUP BY service_account_identity HAVING COUNT(*) > 1")
        shared_rows = cursor.fetchall()
        
        shared_identities = [r[0] for r in shared_rows]
        
        cursor.execute("SELECT agent_id, agent_name, role_scope FROM agent_registry WHERE role_scope LIKE '%owner%'")
        excessive_rows = cursor.fetchall()
        
        over_privileged = []
        for r in excessive_rows:
            over_privileged.append({
                "agent_id": r[0],
                "agent_name": r[1],
                "current_role": r[2],
                "recommended_role": "roles/viewer"
            })
            
        return {
            "sub_agent": self.agent_name,
            "status": "VIOLATIONS_DETECTED" if (shared_identities or over_privileged) else "COMPLIANT",
            "shared_logins_detected": shared_identities,
            "over_privileged_agents": over_privileged
        }


# ------------------------------------------------------------------------------
# SECTION 4: SECURITY GOVERNANCE SUPERVISOR AGENT
# ------------------------------------------------------------------------------

class SecurityGovernanceSupervisorAgent:
    """
    Master Security Governance Supervisor Agent orchestrating discovery, identity right-sizing,
    and generating compliance audit evidence.
    """

    def __init__(self, db_conn: sqlite3.Connection):
        """
        Constructor instantiating specialized security sub-agents.
        """
        self.agent_name = "Security Governance Supervisor Agent"
        self.discovery_agent = ShadowAgentDiscoverySubAgent(db_conn)
        self.identity_agent = IdentityRightSizingSubAgent(db_conn)

    def run_estate_governance_audit(self) -> Dict[str, Any]:
        """
        Executes full security audit across NovaSmart's agent estate.
        """
        print(f"\n[{self.agent_name}] Initiating autonomous governance audit across agent estate...")
        
        # Step 1: Run Shadow Agent Discovery Sub-Agent.
        discovery_res = self.discovery_agent.discover_shadow_agents()
        
        # Step 2: Run Identity Right-Sizing Sub-Agent.
        identity_res = self.identity_agent.audit_identities()
        
        # Step 3: Determine compliance status.
        has_violations = discovery_res["shadow_agent_count"] > 0 or identity_res["status"] == "VIOLATIONS_DETECTED"
        
        return {
            "supervisor": self.agent_name,
            "compliance_status": "ACTION_REQUIRED" if has_violations else "FULLY_SECURED",
            "findings_summary": {
                "shadow_agents_discovered": discovery_res["shadow_agent_count"],
                "shared_logins_flagged": len(identity_res["shared_logins_detected"]),
                "over_privileged_roles_flagged": len(identity_res["over_privileged_agents"])
            },
            "discovery_audit": discovery_res,
            "identity_audit": identity_res
        }


# ------------------------------------------------------------------------------
# LOCAL LAPTOP EXECUTION ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    print("==========================================================")
    print("  RUNNING LESSON 8: SECURITY GOVERNANCE MULTI-AGENT ESTATE")
    print("==========================================================")

    # Initialize governance database.
    db = setup_governance_database()

    # Instantiate Security Governance Supervisor Agent.
    supervisor = SecurityGovernanceSupervisorAgent(db)

    # Run full estate security audit.
    audit_output = supervisor.run_estate_governance_audit()

    # Print pretty-printed JSON output.
    print("\n--- Governance Audit Output ---")
    print(json.dumps(audit_output, indent=2))
