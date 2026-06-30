import chainlit as cl
from ollama import chat


@cl.on_message
async def main(message: cl.Message):

    # get previous conversation history
    history = cl.chat_context.to_openai()

    response = chat(
        model="gemma3:4b",
        messages=history + [
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