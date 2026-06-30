from ollama import chat

while True:
    user_input=input("you : ")
    if user_input.lower()=="exit":
        break
    response=chat(
        model="gemma3",
        messages=[
            {
                "role":"user",
                "content":user_input
            }
        ]
    )
    print("\nBot:", response["message"]["content"])
    print()