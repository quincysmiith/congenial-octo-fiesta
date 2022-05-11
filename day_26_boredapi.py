import streamlit as st
import requests

st.header("Bored API")

st.sidebar.header("Input")

selected_type = st.sidebar.selectbox(
    "Select an activity type", ["education", "recreational", "social", "cooking"]
)

participants = st.sidebar.slider("Number of participants", 1, 3, 1)

suggested_activity_url = f"http://www.boredapi.com/api/activity?type={selected_type}&participants={participants}"

json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

st.write(suggested_activity)

st.info(suggested_activity["activity"])

# structure and content of columns

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(label="Number of Participants", value=participants)


with c2:
    st.metric(label="Activity type", value=suggested_activity["type"])

with c3:
    st.metric(label="Price", value=suggested_activity["price"])
