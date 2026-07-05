import asyncio
import os
from agent_framework_openai import OpenAIChatCompletionClient
from mocogpt import gpt_server

async def test_it():
    server = gpt_server(12306)
    server.chat.completions.request(prompt="Hola").response(content="Cómo puedo ayudarte?")
    with server:
        # Create an AsyncOpenAI client
        api_key = os.getenv("TEST_API_KEY", "sk-123456789")
        c = OpenAIChatCompletionClient(model="gpt-4", api_key=api_key, base_url="http://localhost:12306/v1")

        from agent_framework import Message as ChatMessage
        msg = ChatMessage(text="Hola", role="user")
        try:
            await c.get_response(messages=[msg])
            print("Success")
        except Exception:
            print("An error occurred during test execution.")

asyncio.run(test_it())
