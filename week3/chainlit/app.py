import chainlit as cl
from ollama import chat

@cl.on_message
async def main(message: cl.Message):

    response = chat(
        model="qwen3:4b",   
        messages=[
            {

                "role": "user",
                "content": message.content
            }
        ]
    )

    print(response)
    await cl.Message(
        content=response.message.content
    ).send()