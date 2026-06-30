import streamlit as st
from ollama import chat

st.title("My AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages=[]

user_input = st.text_input("Ask me anything")

if st.button("Send"):

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )
    response = chat(
        model="gemma3",
        messages=st.session_state.messages
    )

    reply=response["message"]["content"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

for msg in st.session_state.messages:
    st.write(f"{msg['role']} : {msg['content']}")