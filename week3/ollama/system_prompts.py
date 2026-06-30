from ollama import chat
response = chat(
    model="gemma3",
    messages=[
        {
            "role":"system",
            "content":"You are an expert Python mentor teaching beginners."
        },
        {
            "role":"user",
            "content":"What is Python?"
        }
    ]
)
print(response["message"]["content"])