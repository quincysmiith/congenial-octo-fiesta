import streamlit as st

st.header("st.multiselect")

my_multiselect = st.multiselect(
    "Pick your favourite football players",
    [
        "Pele",
        "Maradona",
        "Ronaldinho",
        "Zidane",
        "Neymar",
        "Ronaldo R9",
        "Ronaldo",
        "Messi",
    ],
    ["Pele", "Messi"],
)

st.write(my_multiselect)

for i in my_multiselect:
    st.write(i)