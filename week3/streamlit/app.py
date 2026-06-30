import streamlit as st
import pandas as pd

df=pd.DataFrame({
    "Name":["mansi","jyati","vani"],
    "age":[20,20,16]
})
st.table(df)

file=st.file_uploader(
    "upload an img",
    type=["jpg","png"]
)
if file:
    st.image(file)
