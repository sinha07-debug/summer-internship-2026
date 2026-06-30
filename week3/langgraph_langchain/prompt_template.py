from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="gemma3")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a programming teacher. Explain concepts in simple language."
    ),
    (
        "human",
        "Explain {topic}"
    )
])

chain = prompt | llm | StrOutputParser()

while True:
    topic = input("Enter topic: ")

    if topic.lower() == "exit":
        break

    print("\n")
    print(chain.invoke({"topic": topic}))
    print("\n")