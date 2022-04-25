import streamlit as st
import time

st.header("st.progress")

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)


st.snow()

st.balloons()