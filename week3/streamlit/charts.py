import streamlit as st
import pandas as pd
df=pd.DataFrame({
    "Sales":[2,5,3,6,7,8,9]
})
st.line_chart(df)


st.title("Main Page")

choice = st.sidebar.selectbox(
    "Menu",
    ["Home","About","Contact"]
)

st.write(choice)

col1, col2, col3 = st.columns(3)

with col1:
    st.button("A")

with col2:
    st.button("B")

with col3:
    st.button("C")

count = 0

if st.button("Increment"):
    count += 1

st.write(count)