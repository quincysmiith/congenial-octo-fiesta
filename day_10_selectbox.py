import streamlit as st

st.header("st.selectbox")

# Selectbox 1
selectbox_code_string = '''
my_selectbox = st.selectbox(
    "What is your favourite colour", ["red", "blue", "pink", "yellow"]
)
'''

st.code(selectbox_code_string)

my_selectbox = st.selectbox(
    "What is your favourite colour", ["red", "blue", "pink", "yellow"]
)

st.write(f"So **{my_selectbox}** is your favourite colour")

st.markdown("---")


# Selectbox 2

fighter_selection = st.selectbox("Who would win in a fight", ["The Hulk", "Superman"])

st.write(fighter_selection)
