import streamlit as st

st.header("Streamlit Themes")

st.write(
    "The theme of a streamlit app can be modified by changing the _config.toml_ file"
)

st.write("The _config.toml_ file shoule be saved in a folder called _.streamlit_")

st.write("The contents of the _.streamlit/config.toml_ file should be something like:")

st.code(
    """
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
"""
)

st.write(
    "More details on themes can be found [here](https://docs.streamlit.io/library/advanced-features/theming)"
)

st.write("HTML color picker [here](https://htmlcolorcodes.com/color-picker/)")
