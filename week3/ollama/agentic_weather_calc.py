from ollama import chat

def weather(city):
    return f"{city}temperature is 39*C"

def calculator(expression):
    try:
        result=eval(expression)
        return f"answer = {result}"
    except:
        return "invalid"
    
def agent(query):

    query_lower = query.lower()
 
    if "weather" in query_lower:

        words = query.split()
        city = words[-1]
        result = weather(city)

        return result

    elif any(op in query for op in ["+", "-", "*", "/"]):

        result = calculator(query)
        return result

    else:

        response = chat(
            model="gemma3",
            messages=[
                {
                    "role":"system",
                    "content":
                    "You are a helpful AI assistant"
                },

                {
                    "role":"user",
                    "content":query
                }
            ]

        )

        return response["message"]["content"]

while True:

    query = input("\nAsk: ")
    if query.lower()=="exit":
        break

    answer = agent(query)

    print("\nAI:", answer)