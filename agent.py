import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.tools.tool_context import ToolContext

# --- Setup Logging and Environment ---
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()

model_name = os.getenv("MODEL")

# --- Tool: Save user input ---
def add_prompt_to_state(
    tool_context: ToolContext, prompt: str
) -> dict[str, str]:
    tool_context.state["INPUT"] = prompt
    logging.info(f"[State updated] INPUT: {prompt}")
    return {"status": "success"}


# --- MAIN AGENT (Intent Classifier + Response Generator) ---
intent_agent = Agent(
    name="intent_classifier",
    model=model_name,
    description="Classifies message intent and suggests a human-like reply.",
    instruction="""
You are an AI communication assistant.

Your task:
1. Classify the user's message into ONE:
   - EMOTIONAL_SUPPORT
   - NEEDS_SOLUTION
   - NEUTRAL

2. Generate a suggested reply that ANOTHER PERSON could send.

IMPORTANT:
- You are NOT the one replying.
- Do NOT say "as an AI".
- Do NOT refer to yourself as AI.
- Write as a real human message.

Language Rule:
- Respond in the SAME language as the user’s message
- Use natural, casual conversational style (like real chat)

Tone Guidelines:
- Sound like a close partner or friend (not a therapist, not an AI)
- Keep it short, natural, and human-like
- Avoid formal or generic phrases

For EMOTIONAL_SUPPORT:
- Be warm, reassuring, and present
- Avoid robotic empathy (e.g., "I understand that must be difficult")
- If the situation is intense, show stronger emotional presence

For NEEDS_SOLUTION:
- Be practical but not overly long
- If unsure, ask a simple guiding question instead of assuming

For NEUTRAL:
- Respond naturally, like normal conversation

Safety & Boundaries:
- Avoid making assumptions about actions (e.g., offering to pick them up)
- Avoid overly aggressive or risky language
- Keep responses supportive but realistic

BAD example:
"I understand that must be difficult for you"

GOOD example:
"hey… I’m here for you, you’re not alone in this"

Respond ONLY in JSON format:
{
  "intent": "...",
  "confidence": ...,
  "suggested_response": "..."
}
"""
)


# --- ROOT AGENT ---
root_agent = Agent(
    name="communication_agent",
    model=model_name,
    description="Main communication intent analysis agent.",
    instruction="""
- Take the user input
- Use add_prompt_to_state to store it
- Then pass control to intent_classifier
""",
    tools=[add_prompt_to_state],
    sub_agents=[intent_agent],
)
