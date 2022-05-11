import streamlit as st
import json
from pathlib import Path


from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo


# use the full screen
st.set_page_config(layout="wide")

# Add details to the sidebar
with st.sidebar:
    st.header("Drag and resize elements")
    st.write("Build a draggable and resizeable dashboard with Streamlit Elements")

    media_url = st.text_input("Media URL", value = "https://www.youtube.com/watch?v=vIQQR_yq-8I")

# Ensure data is part of the session and persists
if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()


# Define dashboard layout
# A dashboard has 12 columns by default
# More info: https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # Editor
    # positioned in coordinates x=0 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("editor", 0, 0, 6, 3),

    # Chart 
    # positioned in coordinates x=6 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("chart", 6, 0, 6, 3),

    # Media
    # positioned in coordinates x=0 and y=3, and takes 6/12 columns and has a height of 4.
    dashboard.Item("media", 0, 2, 12, 4),
]


with elements("demo"):



    with dashboard.Grid(layout, draggableHandle=".draggable"):



        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):


            mui.CardHeader(title="Editor", className="draggable")


            with mui.CardContent(sx={"flex":1, "minHeight":0}):


                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language = "json",
                    onChange=lazy(sync("data"))
                )
