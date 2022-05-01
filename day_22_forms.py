import streamlit as st

st.header("st.form")

st.write("Typically a streamlit app updates whenever any single widget is modified.")

st.write(
    "Using forms allows you to 'batch' all of the widget changes together in a single update"
)

code_string = """
with st.form("my_form"):
    st.write("Pick some values")

    age = st.slider("How old are you", 0, 100, 50)
    my_colour = st.selectbox(
        "What is your favourite colour", ["red", "blue", "pink", "yellow"]
    )

    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(age)
    st.write(my_colour)
    st.write(submitted)
"""

st.code(code_string)

st.write("form example:")

with st.form("my_form"):
    st.write("Pick some values")

    age = st.slider("How old are you", 0, 100, 50)
    my_colour = st.selectbox(
        "What is your favourite colour", ["red", "blue", "pink", "yellow"]
    )

    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(age)
    st.write(my_colour)
    st.write(submitted)
