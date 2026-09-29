# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 7: RAG KNOWLEDGE RETRIEVAL AGENT
# ==============================================================================
# File: examples/07_rag_knowledge_agent.py
# Level: Enterprise / Junior Developer Friendly
# Purpose: Demonstrates Retrieval-Augmented Generation (RAG) over policy documents.
# Run on local laptop: python3 07_rag_knowledge_agent.py
# ==============================================================================

# Import built-in JSON module for structured serialization.
import json

# Import typing hints for parameters and returns.
from typing import Dict, Any, List, Tuple


# ------------------------------------------------------------------------------
# IN-MEMORY KNOWLEDGE BASE DOCUMENTS
# ------------------------------------------------------------------------------

POLICY_DOCUMENTS = [
    {
        "doc_id": "DOC-001",
        "title": "NovaSmart 30-Day Return Policy",
        "content": "Customers can return undamaged items within 30 days of delivery for a full refund to original payment method. Shipping costs are non-refundable."
    },
    {
        "doc_id": "DOC-002",
        "title": "NovaSmart Price Match Guarantee",
        "content": "NovaSmart matches prices from authorized retail competitors. The item must be identical in model, color, and in stock at competitor store."
    },
    {
        "doc_id": "DOC-003",
        "title": "NovaSmart Warranty Policy",
        "content": "All electronic products include a 1-year limited warranty covering hardware defects. Physical liquid damage or user drops are excluded."
    }
]


# ------------------------------------------------------------------------------
# RAG KNOWLEDGE SEARCH AGENT
# ------------------------------------------------------------------------------

class RAGKnowledgeAgent:
    """
    An AI agent that retrieves relevant documentation chunks using term frequency similarity
    and synthesizes cited answers.
    """

    def __init__(self, agent_name: str, documents: List[Dict[str, str]]):
        """
        Constructor initializing knowledge base documents.
        """
        self.agent_name = agent_name
        self.documents = documents

    def retrieve_chunks(self, query: str, top_k: int = 2) -> List[Tuple[Dict[str, str], float]]:
        """
        Retrieval Step: Computes term match relevance score for query across documents.
        """
        query_words = set(query.lower().split())
        scored_docs = []
        
        for doc in self.documents:
            doc_text = (doc["title"] + " " + doc["content"]).lower()
            doc_words = doc_text.split()
            
            # Count keyword occurrences in document text.
            match_score = sum([1 for w in doc_words if w in query_words])
            if match_score > 0:
                scored_docs.append((doc, float(match_score)))
                
        # Sort documents by relevance score descending.
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        return scored_docs[:top_k]

    def answer_query(self, user_query: str) -> Dict[str, Any]:
        """
        Augment & Generate Step: Retrieves document context and formats cited response.
        """
        print(f"\n[{self.agent_name}] RAG processing query: '{user_query}'")
        
        # Step 1: Retrieve top document chunks.
        retrieved = self.retrieve_chunks(user_query, top_k=2)
        
        if not retrieved:
            return {
                "agent_name": self.agent_name,
                "status": "NO_RELEVANT_DOCS",
                "query": user_query,
                "reply": "I could not find policy documents relevant to your query.",
                "citations": []
            }
            
        citations = []
        synthesized_text_parts = []
        
        # Step 2: Augment context with citations.
        for doc, score in retrieved:
            citations.append({
                "doc_id": doc["doc_id"],
                "title": doc["title"],
                "relevance_score": score
            })
            synthesized_text_parts.append(f"Per [{doc['title']}]: {doc['content']}")

        # Combine synthesized parts.
        synthesized_answer = " ".join(synthesized_text_parts)
        
        return {
            "agent_name": self.agent_name,
            "status": "SUCCESS",
            "query": user_query,
            "reply": synthesized_answer,
            "citations": citations
        }


# ------------------------------------------------------------------------------
# LOCAL LAPTOP EXECUTION ENTRYPOINT
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    print("==========================================================")
    print("  RUNNING LESSON 7: RAG KNOWLEDGE RETRIEVAL AGENT")
    print("==========================================================")

    # Instantiate RAG Agent.
    rag_agent = RAGKnowledgeAgent("NovaSmart Policy RAG Agent", POLICY_DOCUMENTS)

    # Test Case 1: Return policy query.
    res_1 = rag_agent.answer_query("How many days do I have to return an item?")
    print("\n--- Test Case 1 Output ---")
    print(json.dumps(res_1, indent=2))

    # Test Case 2: Warranty coverage query.
    res_2 = rag_agent.answer_query("Does warranty cover liquid damage?")
    print("\n--- Test Case 2 Output ---")
    print(json.dumps(res_2, indent=2))
