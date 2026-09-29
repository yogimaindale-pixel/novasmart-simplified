# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 1C: SIMPLE IN-MEMORY FAQ RETRIEVAL AGENT
# ==============================================================================
# File: examples/01c_faq_retrieval_agent.py
# Level: Beginner / Junior Developer Friendly
# Purpose: Demonstrates a simple AI agent that searches an in-memory list of FAQ
#          question-answer pairs using dummy data. Zero external tools needed!
# Run on local laptop: python3 01c_faq_retrieval_agent.py
# ==============================================================================

# Import built-in JSON module for structured formatting.
import json

# Import typing annotations for clear method signatures.
from typing import Dict, Any, List, Optional


# ------------------------------------------------------------------------------
# DUMMY FAQ DATASET (KNOWLEDGE STORE)
# ------------------------------------------------------------------------------

# Define a list of dummy FAQ records representing a company help center knowledge base.
DUMMY_FAQ_DATABASE = [
    {
        "faq_id": "FAQ-01",
        "question": "What is the return policy for NovaSmart items?",
        "answer": "You can return any undamaged product within 30 days of purchase for a full refund.",
        "tags": ["return", "refund", "policy", "30 days"]
    },
    {
        "faq_id": "FAQ-02",
        "question": "How do I track my shipped order?",
        "answer": "Check your confirmation email for the tracking number or log into your NovaSmart account page.",
        "tags": ["track", "tracking", "shipment", "shipping", "order"]
    },
    {
        "faq_id": "FAQ-03",
        "question": "What warranty comes with NovaSmart products?",
        "answer": "All NovaSmart electronic products include a 1-year limited manufacturer warranty.",
        "tags": ["warranty", "repair", "defect", "1 year"]
    }
]


# ------------------------------------------------------------------------------
# SIMPLE FAQ RETRIEVAL AGENT CLASS
# ------------------------------------------------------------------------------

class SimpleFAQAgent:
    """
    A simple AI Agent that searches an in-memory list of FAQ dictionaries for a user's question,
    calculates match confidence, and returns the best matching answer.
    """

    def __init__(self, agent_name: str, faq_store: List[Dict[str, Any]]):
        """
        Constructor initializing agent identity and FAQ dataset.
        
        Args:
            agent_name (str): The name of this FAQ search agent.
            faq_store (List[Dict[str, Any]]): List of FAQ dictionaries to search over.
        """
        # Store agent name.
        self.agent_name = agent_name
        # Store in-memory FAQ dataset reference.
        self.faq_store = faq_store

    def find_answer(self, user_question: str) -> Dict[str, Any]:
        """
        Searches the FAQ dataset for the closest matching question or tag.

        Args:
            user_question (str): Question string typed by user.

        Returns:
            Dict[str, Any]: Structured output dictionary containing status, match score, and answer.
        """
        # Clean user input question string.
        cleaned_question = user_question.strip().lower()
        # Split user question into individual word tokens.
        query_words = set(cleaned_question.split())
        
        best_match = None
        highest_score = 0
        
        # Loop through each FAQ record in the dummy dataset.
        for faq in self.faq_store:
            # Combine question text and tags into a lowercased searchable string.
            searchable_text = (faq["question"] + " " + " ".join(faq["tags"])).lower()
            
            # Count how many query word tokens appear in the searchable text.
            match_score = 0
            for word in query_words:
                if len(word) > 2 and word in searchable_text:  # Ignore short words like 'is', 'a'
                    match_score += 1
                    
            # Update best match if this FAQ scored higher than previous entries.
            if match_score > highest_score:
                highest_score = match_score
                best_match = faq

        # Check if a valid match was found (at least 1 matching keyword).
        if best_match and highest_score > 0:
            return {
                "agent_name": self.agent_name,
                "status": "ANSWER_FOUND",
                "user_question": user_question,
                "matched_faq_id": best_match["faq_id"],
                "matched_question": best_match["question"],
                "confidence_score": f"{highest_score} keyword match(es)",
                "answer": best_match["answer"]
            }
        else:
            # Fallback output when no keywords match.
            return {
                "agent_name": self.agent_name,
                "status": "NO_MATCH_FOUND",
                "user_question": user_question,
                "confidence_score": "0 keyword matches",
                "answer": "I'm sorry, I could not find an answer in our FAQ. Please contact support."
            }


# ------------------------------------------------------------------------------
# LOCAL LAPTOP EXECUTION ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Print demonstration header.
    print("==========================================================")
    print("  RUNNING LESSON 1C: SIMPLE IN-MEMORY FAQ RETRIEVAL AGENT")
    print("==========================================================")

    # Step 1: Instantiate SimpleFAQAgent passing dummy dataset.
    faq_agent = SimpleFAQAgent("NovaSmart FAQ Assistant", DUMMY_FAQ_DATABASE)

    # Step 2: Test query 1 (Return policy question).
    result_1 = faq_agent.find_answer("How many days do I have for returns?")
    print("\n--- Test Query 1 Output ---")
    print(json.dumps(result_1, indent=2))

    # Step 3: Test query 2 (Order tracking question).
    result_2 = faq_agent.find_answer("Where can I track my shipment order?")
    print("\n--- Test Query 2 Output ---")
    print(json.dumps(result_2, indent=2))

    # Step 4: Test query 3 (Unmatched question).
    result_3 = faq_agent.find_answer("What is the weather today?")
    print("\n--- Test Query 3 Output ---")
    print(json.dumps(result_3, indent=2))
