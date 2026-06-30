from typing import Annotated
from typing_extensions import TypedDict

from langchain.tools import tool
from langchain_ollama import ChatOllama

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

class State(TypedDict):
    messages: Annotated[list, add_messages]

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@tool
def divide(a: int, b: int) -> float:
    """Divide two numbers."""

    if b == 0:
        return "Cannot divide by zero."

    return a / b

tools = [add, subtract, multiply, divide]

llm = ChatOllama(
    model="qwen3:4b",   
    temperature=0
)

llm = llm.bind_tools(tools)

from langchain_core.messages import SystemMessage


def assistant(state: State):

    messages = [
        SystemMessage(
            content="""
You are a helpful general assistant.

You have calculator tools:
- add
- subtract
- multiply
- divide

Use tools only for arithmetic questions.

For all other questions, answer normally using your own knowledge.
"""
        )
    ] + state["messages"]


    response = llm.invoke(messages)

    return {
        "messages": [response]
    }

graph = StateGraph(State)

graph.add_node("assistant", assistant)

graph.add_node("tools", ToolNode(tools))

graph.add_edge(START, "assistant")

graph.add_conditional_edges(
    "assistant",
    tools_condition
)

graph.add_edge(
    "tools",
    "assistant"
)

graph.add_edge(
    "assistant",
    END
)

memory = MemorySaver()

app = graph.compile(
    checkpointer=memory
)


config = {
    "configurable": {
        "thread_id": "1"
    }
}


print("Calculator Agent")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    result = app.invoke(
        {
            "messages": [
                ("user", user)
            ]
        },
        config=config
    )

    print("\nAssistant:")
    print(result["messages"][-1].content)
    print()