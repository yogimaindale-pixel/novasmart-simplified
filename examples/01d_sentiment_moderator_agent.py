# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 1D: SIMPLE SENTIMENT & CONTENT MODERATOR AGENT
# ==============================================================================
# File: examples/01d_sentiment_moderator_agent.py
# Level: Beginner / Junior Developer Friendly
# Purpose: Demonstrates a simple AI agent that analyzes product review sentiment
#          and screens for inappropriate content using dummy data. Zero tools needed!
# Run on local laptop: python3 01d_sentiment_moderator_agent.py
# ==============================================================================

# Import built-in JSON module for structured serialization.
import json

# Import typing hints for parameters and returns.
from typing import Dict, Any, List


# ------------------------------------------------------------------------------
# DUMMY PRODUCT REVIEWS DATASET
# ------------------------------------------------------------------------------

# Define a list of dummy customer product review records.
DUMMY_REVIEWS = [
    {
        "review_id": "REV-201",
        "product_name": "NovaSmart 4K Monitor",
        "user": "tech_guy99",
        "review_text": "Awesome display! Extremely sharp colors and fantastic build quality. Highly recommended!"
    },
    {
        "review_id": "REV-202",
        "product_name": "NovaSmart Wireless Earbuds",
        "user": "music_lover",
        "review_text": "Battery life is terrible and the left earbud stopped working after 2 days. Very disappointed."
    },
    {
        "review_id": "REV-203",
        "product_name": "NovaSmart Keyboard",
        "user": "troll_user",
        "review_text": "This product is trash spam buy cheap fake items at scammart.com!"
    }
]


# ------------------------------------------------------------------------------
# SIMPLE SENTIMENT & MODERATION AGENT CLASS
# ------------------------------------------------------------------------------

class SimpleModeratorAgent:
    """
    A simple AI Agent that evaluates product review text for sentiment (POSITIVE,
    NEUTRAL, NEGATIVE) and screens for offensive/spam keywords.
    """

    def __init__(self, agent_name: str):
        """
        Constructor initializing agent identity and dictionary rule lists.
        """
        self.agent_name = agent_name
        
        # Word lists for simple sentiment scoring.
        self.positive_words = ["awesome", "sharp", "fantastic", "recommended", "great", "love", "excellent"]
        self.negative_words = ["terrible", "disappointed", "bad", "broken", "stopped", "worst", "poor"]
        
        # Word list for content moderation flags.
        self.moderation_blocked_words = ["trash", "spam", "fake", "scammart.com", "hate"]

    def analyze_review(self, review_data: Dict[str, str]) -> Dict[str, Any]:
        """
        Analyzes review text sentiment score and moderation safety status.

        Args:
            review_data (Dict[str, str]): Dictionary containing review_id, user, review_text.

        Returns:
            Dict[str, Any]: Structured output dictionary.
        """
        review_id = review_data.get("review_id")
        text = review_data.get("review_text", "")
        lowercased_text = text.lower()
        
        # Calculate sentiment score counts.
        pos_count = sum([1 for w in self.positive_words if w in lowercased_text])
        neg_count = sum([1 for w in self.negative_words if w in lowercased_text])
        
        # Determine overall sentiment classification.
        if pos_count > neg_count:
            sentiment = "POSITIVE"
        elif neg_count > pos_count:
            sentiment = "NEGATIVE"
        else:
            sentiment = "NEUTRAL"

        # Check moderation safety flags.
        blocked_found = [w for w in self.moderation_blocked_words if w in lowercased_text]
        is_flagged = len(blocked_found) > 0
        moderation_status = "FLAGGED_FOR_REVIEW" if is_flagged else "APPROVED"

        # Return structured audit output payload.
        return {
            "agent_name": self.agent_name,
            "status": "ANALYZED",
            "review_id": review_id,
            "product_name": review_data.get("product_name"),
            "sentiment": sentiment,
            "positive_signal_count": pos_count,
            "negative_signal_count": neg_count,
            "moderation_status": moderation_status,
            "flagged_keywords": blocked_found if is_flagged else []
        }


# ------------------------------------------------------------------------------
# LOCAL LAPTOP EXECUTION ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Print demonstration banner.
    print("==========================================================")
    print("  RUNNING LESSON 1D: SIMPLE SENTIMENT & MODERATOR AGENT")
    print("==========================================================")

    # Step 1: Instantiate SimpleModeratorAgent.
    moderator_agent = SimpleModeratorAgent("NovaSmart Review Moderator")

    # Step 2: Analyze all sample product reviews.
    for sample_review in DUMMY_REVIEWS:
        result = moderator_agent.analyze_review(sample_review)
        print(f"\n--- Review {sample_review['review_id']} Analysis ---")
        print(json.dumps(result, indent=2))
