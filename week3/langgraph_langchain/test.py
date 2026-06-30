from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3")

prompt = PromptTemplate(
    template="Explain {topic} in simple words",
    input_variables=["topic"]
)

chain = prompt | llm

response = chain.invoke(
    {"topic":"LangChain"}
)

print(response.content)