import streamlit as st

st.header("Secrets")

st.write("contents of the _.streamlit/secrets.toml_")

st.code("""

# Everything in this section will be available as an environment variable 
db_username = "Jane"
db_password = "12345qwerty"

[some_creds]
a_secret = "lost money"
phone_number = "12345678"
pin = "0909"
""")

st.write("The following code can be used to access the variables in the _.streamlit/secrets.toml_ file")

st.code("st.write(st.secrets['message'])")

st.write(st.secrets['db_username'])


st.markdown("---")


st.write("Alternatively the variables can be accessed by accessing environment variables")

st.code("""
import os
st.write(os.environ["db_username"])
""")

import os
st.write(os.environ["db_username"])


st.markdown("---")

st.write("Another way of accessing the variables:")

st.code("""

st.write(st.secrets.some_creds.phone_number)

""")

st.write(st.secrets.some_creds.phone_number)