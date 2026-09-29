# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 1B: SIMPLE EMAIL & TICKET CLASSIFIER AGENT
# ==============================================================================
# File: examples/01b_email_classifier_agent.py
# Level: Beginner / Junior Developer Friendly
# Purpose: Demonstrates a simple AI agent that classifies incoming emails using
#          in-memory dummy data and rule-based evaluation. Zero extra tools needed!
# Run on local laptop: python3 01b_email_classifier_agent.py
# ==============================================================================

# Import built-in JSON module to convert Python dictionary outputs into formatted JSON.
import json

# Import typing annotations to specify expected parameter and return types clearly.
from typing import Dict, Any, List


# ------------------------------------------------------------------------------
# DUMMY EMAIL INCOMING DATASET (SIMULATED EMAIL INBOX)
# ------------------------------------------------------------------------------

# Define a list of dummy customer emails simulating an incoming customer service inbox.
DUMMY_EMAILS = [
    {
        "email_id": "EML-101",
        "sender": "john.doe@example.com",
        "subject": "Urgent: Charged twice on my credit card",
        "body": "Hello, I noticed a duplicate charge of $89.99 on my account. Please refund immediately!"
    },
    {
        "email_id": "EML-102",
        "sender": "sarah.connor@example.com",
        "subject": "Screen is black when turning on monitor",
        "body": "My NovaSmart 4K Monitor power light is blue but the display remains completely dark."
    },
    {
        "email_id": "EML-103",
        "sender": "marketing@spamservices.com",
        "subject": "Win a free luxury cruise now!",
        "body": "Congratulations! You have been selected for a free cruise. Click here to claim your prize."
    }
]


# ------------------------------------------------------------------------------
# SIMPLE EMAIL CLASSIFIER AGENT CLASS
# ------------------------------------------------------------------------------

class SimpleEmailClassifierAgent:
    """
    A simple AI Agent that inspects incoming emails, categorizes them into support
    departments (BILLING, TECHNICAL_SUPPORT, SPAM, GENERAL), and assigns an urgency level.
    """

    def __init__(self, agent_name: str):
        """
        Constructor method to set up the agent's identity.
        
        Args:
            agent_name (str): The name of this classifier agent.
        """
        # Store the agent's name in an instance variable.
        self.agent_name = agent_name
        
        # Define keyword lists for department matching using standard python dictionaries.
        self.category_keywords = {
            "BILLING": ["charge", "charged", "refund", "credit card", "payment", "invoice", "price"],
            "TECHNICAL_SUPPORT": ["screen", "monitor", "power", "dark", "broken", "setup", "error", "bug"],
            "SPAM": ["win", "free", "cruise", "prize", "congratulations", "click here", "lottery"]
        }

    def classify_email(self, email_data: Dict[str, str]) -> Dict[str, Any]:
        """
        Classifies a single email dictionary based on subject and body content.

        Args:
            email_data (Dict[str, str]): Dictionary containing email_id, sender, subject, body.

        Returns:
            Dict[str, Any]: Structured classification result including department and urgency.
        """
        # Extract email fields from input dictionary.
        email_id = email_data.get("email_id", "UNKNOWN")
        subject = email_data.get("subject", "")
        body = email_data.get("body", "")
        
        # Combine subject and body into a single lowercased string for easy keyword search.
        full_text = f"{subject} {body}".lower()
        
        # Default category and urgency settings.
        assigned_category = "GENERAL_INQUIRY"
        urgency_level = "LOW"
        
        # Evaluate text against category keywords.
        for category, keywords in self.category_keywords.items():
            # Check if any keyword matches the email text.
            for kw in keywords:
                if kw in full_text:
                    assigned_category = category
                    break
            if assigned_category != "GENERAL_INQUIRY":
                break

        # Calculate urgency level based on specific high-priority indicators.
        if "urgent" in full_text or "immediately" in full_text or "broken" in full_text:
            urgency_level = "CRITICAL"
        elif assigned_category == "BILLING" or assigned_category == "TECHNICAL_SUPPORT":
            urgency_level = "HIGH"
        elif assigned_category == "SPAM":
            urgency_level = "NONE"

        # Return structured classification payload dictionary.
        return {
            "agent_name": self.agent_name,
            "status": "CLASSIFIED",
            "email_id": email_id,
            "sender": email_data.get("sender"),
            "subject": subject,
            "assigned_category": assigned_category,
            "urgency_level": urgency_level,
            "recommended_action": self._get_action(assigned_category)
        }

    def _get_action(self, category: str) -> str:
        """
        Private helper method to map categories to recommended actions.
        """
        if category == "BILLING":
            return "Route to Finance & Refund Team"
        elif category == "TECHNICAL_SUPPORT":
            return "Route to Hardware Diagnostics Team"
        elif category == "SPAM":
            return "Auto-archive and mark as Spam"
        else:
            return "Route to Customer Service Helpdesk"


# ------------------------------------------------------------------------------
# LOCAL LAPTOP EXECUTION ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Print demonstration header to console.
    print("==========================================================")
    print("  RUNNING LESSON 1B: SIMPLE EMAIL & TICKET CLASSIFIER AGENT")
    print("==========================================================")

    # Step 1: Instantiate the SimpleEmailClassifierAgent object.
    classifier_agent = SimpleEmailClassifierAgent("NovaSmart Email Classifier")

    # Step 2: Iterate through all dummy emails in the simulated inbox.
    for index, sample_email in enumerate(DUMMY_EMAILS, start=1):
        # Process email through agent.
        result = classifier_agent.classify_email(sample_email)
        
        # Print pretty-printed JSON result to console.
        print(f"\n--- Email {index} Classification Output ---")
        print(json.dumps(result, indent=2))
