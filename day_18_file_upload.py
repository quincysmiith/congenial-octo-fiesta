import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


st.title("File Uploader")

st.write("## Input CSV")

a_file = st.file_uploader("Choose a file", type = ["csv"])

if a_file is not None:
    data = pd.read_csv(a_file)
    AgGrid(data)
    st.write(data.describe())
