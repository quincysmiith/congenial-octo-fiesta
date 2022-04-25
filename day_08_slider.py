import streamlit as st
from datetime import time, datetime

st.header("st.slider")

# -------------------------------------
# Single value slider
# -------------------------------------

st.subheader("Single value slider")

st.code("""age = st.slider("How old are you", 0, 100, 50)""")

age = st.slider("How old are you", 0, 100, 50)

st.write(age)

st.write(f"I tell people I am **{age}** years old")

st.markdown("---")


# -------------------------------------
# Range slider
# -------------------------------------

st.subheader("Range slider")

st.code("""my_range = st.slider("choose a range", 0.0, 100.0, (10.0, 75.0))""")

my_range = st.slider("choose a range", 0.0, 100.0, (10.0, 75.0))

st.write("a range slider returns a tuple")
st.write(my_range)

st.markdown("---")


# -------------------------------------
# Time slider
# -------------------------------------

st.subheader("Time slider")

st.code("""appointment = st.slider("Pick a time", value=(time(7, 30), time(12, 45)))""")

appointment = st.slider("Pick a time", value=(time(7, 30), time(12, 45)))

st.write(appointment)
st.write(f"Start time: {appointment[0]}")
st.write(f"End time: {appointment[1]}")

st.markdown("---")


# -------------------------------------
# Date slider
# -------------------------------------

st.subheader("Date slider")

st.code(
    """my_datetime = st.slider("Pick a date", value=datetime(2022, 4, 11), format = "YYYY-MM-DD")"""
)

# my_datetime = st.slider("Pick a date", value=datetime(2022, 4, 11, 12, 30 ), format = "MM/DD/YY - hh:mm")

my_datetime = st.slider("Pick a date", value=datetime(2022, 4, 11), format="YYYY-MM-DD")

st.write(my_datetime)

st.write(f"Date picked: {my_datetime.date()}")
