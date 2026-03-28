import os
import asyncio
from gemini_agent import GeminiAgent
from google.genai import types

async def test_agent():
    print("Testing GeminiAgent...")
    agent = GeminiAgent()
    
    # Mock a request
    # Since it's an AdkAgent, we can test it using the ADK runner or just call the model if we had credentials.
    # But we can at least check if it initializes and has the correct instructions.
    
    print(f"Agent name: {agent.name}")
    print(f"Agent model: {agent.model}")
    
    if "狗" in agent.instruction or "dog" in agent.instruction.lower():
        print("Instruction contains dog/狗 (A2UI Colorful Weather App rule).")
    else:
        print("Warning: Instruction might be missing A2UI Colorful Weather App rules.")

    if "---a2ui_JSON---" in agent.instruction:
        print("Instruction contains A2UI delimiter.")
    else:
        print("Warning: Instruction missing A2UI delimiter.")

    if "valueStruct" in agent.instruction:
        print("Instruction contains valueStruct (A2UI Schema rule).")
    else:
        print("Warning: Instruction missing valueStruct.")

if __name__ == "__main__":
    asyncio.run(test_agent())
