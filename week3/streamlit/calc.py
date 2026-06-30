import streamlit as st

st.title("Calculator")

num1 = st.number_input("First Number")

num2 = st.number_input("Second Number")

operation = st.selectbox(
    "Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):

    if operation == "Add":
        result = num1 + num2

    elif operation == "Subtract":
        result = num1 - num2

    elif operation == "Multiply":
        result = num1 * num2

    else:
        result = num1 / num2

    st.success(result)