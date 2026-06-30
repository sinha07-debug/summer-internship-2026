from ollama import chat

response = chat(
    model="gemma3",
    messages=[
        {
            "role": "user",
            "content": "Explain Ollama in 2 lines"
        }
    ]
)

print(response["message"]["content"])