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

def assistant(state: State):

    response = llm.invoke(state["messages"])

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

import chainlit as cl

@cl.on_message
async def main(message: cl.Message):

    result = app.invoke(
        {
            "messages": [
                ("user", message.content)
            ]
        },
        config=config
    )

    answer = result["messages"][-1].content

    await cl.Message(content=answer).send()