import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from st_aggrid import AgGrid

st.header("Components")
st.subheader("Ag Grid and Pandas Profiling")

my_sidebar = st.sidebar.selectbox(
    "Did you bring your own data?", ("No, I don't have any", "Yes")
)

if my_sidebar == "No, I don't have any":
    button1 = st.button("Create profile from Penguins data")
    if button1:
        df = pd.read_csv(
            "https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv"
        )
        AgGrid(df)
        pr = df.profile_report()
        st_profile_report(pr)

if my_sidebar == "Yes":
    uploaded_file = st.file_uploader(label="Load a csv file", type=["csv"],)

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        AgGrid(df)
        pr = df.profile_report()
        st_profile_report(pr)

        st.download_button(
            label="Download report",
            data=pr._html,
            file_name="report.html",
            mime="text/html",
        )
