import streamlit as st
import numpy as np
import pandas as pd

st.header("st.cache")

st.write("st.cache allows for the saving of the output from a function")

st.write(
    "So when the function is called again with the same parameters it uses the saved output rather than running again"
)
