import streamlit as st

st.header("Layout")

# columns

col1, col2, col3 = st.columns(3)

with col1:
    st.write("This is column 1")

with col2:
    st.write("This is column 2")