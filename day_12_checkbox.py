import streamlit as st

st.header("st.checkbox")

st.write("In Streamlit each checkbox is its own object")
st.write("This means multiple select boxes can be checked at the same time")

st.markdown("---")

st.write("Which roles best describe your role in data")

data_analyst = st.checkbox("Data Analyst")
data_engineer = st.checkbox("Data Engineer")
data_scientist = st.checkbox("Data Scientist")
data_operations = st.checkbox("Data Operations")
data_vis = st.checkbox("Data Visualisation")
data_whisperer = st.checkbox("Data Whisperer")
data_janitor = st.checkbox("Data Janitor")

if data_analyst:
    st.markdown(":100:")

if data_engineer:
    st.markdown(":rainbow:")

if data_scientist:
    st.markdown(":ocean:")

if data_operations:
    st.markdown(":repeat:")

if data_vis:
    st.markdown(":bar_chart:")

if data_whisperer:
    st.markdown(":speaking_head_in_silhouette:")

if data_janitor:
    st.markdown(":fairy:")
