from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    number: int

def multiply_by_two(state: State):
    return {
        "number": state["number"] * 2
    }

def add_three(state: State):
    return {
        "number": state["number"] + 3
    }

graph = StateGraph(State)

graph.add_node(
    "multiply",
    multiply_by_two
)

graph.add_node(
    "add",
    add_three
)

graph.add_edge(
    START,
    "multiply"
)

graph.add_edge(
    "multiply",
    "add"
)

graph.add_edge(
    "add",
    END
)

app = graph.compile()

result = app.invoke(
    {"number": 5}
)

print(result)