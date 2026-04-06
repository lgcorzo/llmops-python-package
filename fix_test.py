import asyncio
from agent_framework_openai import OpenAIChatCompletionClient
from mocogpt import gpt_server

async def test_it():
    server = gpt_server(12306)
    server.chat.completions.request(prompt="Hola").response(content="Cómo puedo ayudarte?")
    with server:
        # Create an AsyncOpenAI client
        from openai import AsyncOpenAI

        c = OpenAIChatCompletionClient(model="gpt-4", api_key="sk-123456789", base_url="http://localhost:12306/v1")

        from agent_framework import Message as ChatMessage
        msg = ChatMessage(text="Hola", role="user")
        try:
            resp = await c.get_response(messages=[msg])
            print("Success")
        except Exception as e:
            import traceback
            traceback.print_exc()

asyncio.run(test_it())
