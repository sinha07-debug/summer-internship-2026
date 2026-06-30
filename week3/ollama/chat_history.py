from ollama import chat

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = chat(
        model="gemma3",
        messages=messages
    )

    assistant_reply = response["message"]["content"]

    print("\nAssistant:", assistant_reply)
    print()

    messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )