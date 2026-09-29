# ==============================================================================
# NOVASMART AGENT TUTORIAL - LESSON 1: SIMPLE SINGLE-PURPOSE AGENT
# ==============================================================================
# File: examples/01_simple_agent.py
# Level: Beginner / Junior Developer
# Purpose: Demonstrates how to create a basic AI Agent without external tools.
# ==============================================================================

# Import built-in JSON library to format python dictionaries into readable JSON output.
import json

# Import typing annotations for parameters and return types to ensure clean code contracts.
from typing import Dict, Any


# Define the SimpleAgent class to encapsulate basic prompt processing logic.
class SimpleAgent:
    """
    A simple AI Agent that processes text prompts and returns formatted answers.
    """

    def __init__(self, agent_name: str, system_instruction: str):
        """
        Constructor method that runs when a new SimpleAgent object is created.
        
        Args:
            agent_name (str): The name of this agent (e.g. 'Greeting Agent').
            system_instruction (str): Guidelines instructing the agent how to act.
        """
        # Store the agent's name in an instance variable.
        self.agent_name = agent_name
        
        # Store the system prompt instruction in an instance variable.
        self.system_instruction = system_instruction

    def generate_response(self, user_prompt: str) -> Dict[str, Any]:
        """
        Processes an incoming user text prompt and produces a structured result.

        Args:
            user_prompt (str): Text message typed by the user.

        Returns:
            Dict[str, Any]: Dictionary containing status, agent name, and response text.
        """
        # Step 1: Clean and normalize user input by stripping surrounding whitespace.
        cleaned_prompt = user_prompt.strip()
        
        # Step 2: Check if the user prompt is empty.
        if not cleaned_prompt:
            # Return an error dictionary if prompt was empty.
            return {
                "agent_name": self.agent_name,
                "status": "ERROR",
                "message": "Prompt cannot be empty."
            }

        # Step 3: Simple rule-based template logic representing model generation.
        if "hello" in cleaned_prompt.lower() or "hi" in cleaned_prompt.lower():
            # Formulate greeting response.
            reply_text = f"Hello! I am {self.agent_name}. How can I assist you with NovaSmart today?"
        elif "hours" in cleaned_prompt.lower() or "time" in cleaned_prompt.lower():
            # Formulate store hours information response.
            reply_text = "NovaSmart customer support is available 24/7 online."
        else:
            # Default fallback response.
            reply_text = f"I received your request: '{cleaned_prompt}'. Thank you for contacting NovaSmart!"

        # Step 4: Package response in a clean, structured dictionary.
        response_payload = {
            "agent_name": self.agent_name,
            "system_instruction": self.system_instruction,
            "status": "SUCCESS",
            "reply": reply_text
        }

        # Step 5: Return the structured payload to the caller.
        return response_payload


# Execution block that runs when executing this file directly from terminal.
if __name__ == "__main__":
    # Print header message for terminal demonstration.
    print("==================================================")
    print("  RUNNING LESSON 1: SIMPLE SINGLE-PURPOSE AGENT")
    print("==================================================")

    # Step 1: Instantiate a SimpleAgent instance with persona instructions.
    simple_agent = SimpleAgent(
        agent_name="NovaSmart Support Greeter",
        system_instruction="You are a polite retail support assistant."
    )

    # Step 2: Test the agent with a greeting prompt.
    test_result_1 = simple_agent.generate_response("Hi there!")
    # Print pretty-printed JSON output to the console.
    print("\n--- Test Prompt 1 Result ---")
    print(json.dumps(test_result_1, indent=2))

    # Step 3: Test the agent with an inquiry prompt.
    test_result_2 = simple_agent.generate_response("What are your support hours?")
    # Print pretty-printed JSON output to the console.
    print("\n--- Test Prompt 2 Result ---")
    print(json.dumps(test_result_2, indent=2))
