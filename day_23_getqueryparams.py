import streamlit as st

st.header("st.experimental_get_query_params")

st.write(
    "This function allows the streamlit application to access and use the query parameters in a straightforward manner"
)

st.write("Contents of query parameters")

st.code("""st.write(st.experimental_get_query_params())""")

st.write(st.experimental_get_query_params())

st.write("---")

st.write("Query parameters can also be accessed by the key value pairs")

st.code(
    """
firstname = st.experimental_get_query_params()['name'][0]
st.write(firstname)

"""
)

firstname = st.experimental_get_query_params()["name"][0]
st.write(firstname)


st.code(
    """
surname = st.experimental_get_query_params()['surname'][0]
st.write(surname)

"""
)

surname = st.experimental_get_query_params()["surname"][0]
st.write(surname)

st.write("---")
st.code("""st.write(f'Hello **{firstname} {surname}**, how are you?')""")
st.write(f"Hello **{firstname} {surname}**, how are you?")
