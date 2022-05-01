import streamlit as st

st.header("A video")

code_string = "st.video('https://www.youtube.com/watch?v=Yk-unX4KnV4')"

st.code(code_string, language="python")

st.video("https://www.youtube.com/watch?v=Yk-unX4KnV4")


# --------------------------------------
# sidebar with selector
# --------------------------------------

st.header("A sidebar")

sidebar_string_01 = (
    """st.sidebar.selectbox("Choose one", ("this one", "or maybe this one"))"""
)

sidebar_string_02 = """
with st.sidebar:
    st.selectbox("Another one", ("DeeJay", "Khalid"))
"""

st.write("Sidebar selector number 1")
st.code(sidebar_string_01, language="python")

st.write("Sidebar selector number 2")
st.code(sidebar_string_02, language="python")

# my_selectbox = st.selectbox("Choose one", ("this one", "or maybe this one"))

st.sidebar.selectbox("Choose one", ("this one", "or maybe this one"))

# Alternatively

with st.sidebar:
    st.selectbox("Another one", ("DeeJay", "Khalid"))
