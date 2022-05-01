import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


st.header("st.write")

st.code("st.write('Hello, *world* :100:')")

st.write("Hello, *world* :100:")

st.markdown(
    """
emoji shortcodes for Streamlit available [here](https://share.streamlit.io/streamlit/emoji-shortcodes)

markdown cheatsheet available [here](https://www.markdownguide.org/cheat-sheet)

---
"""
)


st.write("Display a number")

st.code("st.write(5678)")

st.write(5678)

st.markdown("---")


# ---------------------------
# Display a dataframe
# ---------------------------

st.write("Display a dataframe")

st.code("st.write(df)")

df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

st.write(df)


st.write("Put a string and a dataframe in the same st.write function")

st.code("""st.write('Below is a dataframe', df, 'Above is a dataframe')""")

st.write("Below is a dataframe", df, "Above is a dataframe")

st.markdown("---")


# --------------------------------
# Display an Altair chart
# --------------------------------

st.write("Display an Altair chart")

st.code(
    """
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)
"""
)

df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)
