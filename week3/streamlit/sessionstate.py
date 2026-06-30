import streamlit as st

name = st.text_input("Name")

if st.button("Save"):
    st.session_state.saved_name = name

if "saved_name" in st.session_state:
    st.write("Saved:", st.session_state.saved_name)