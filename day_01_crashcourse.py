import streamlit as st

st.title("A Streamlit Crash Course")

st.write("Collection of videos covering various aspects of Streamlit")

st.markdown("### What is Streamlit Introduction")

c1, c2 = st.columns(2)

with c1:
    st.video("https://youtu.be/R2nr1uZ8ffc")
    st.video("https://www.youtube.com/watch?v=VtrFjkSGgKM")

with c2:
    st.video("https://www.youtube.com/watch?v=sxLNCDnqyFc")
    st.video("https://www.youtube.com/watch?v=z8vgmvtgxCs")


st.markdown("### The Streamlit Epic Walkthrough")

c1, c2 = st.columns(2)

with c1:

    st.video("https://www.youtube.com/watch?v=vIQQR_yq-8I")

with c2:
    st.video("https://www.youtube.com/watch?v=nnmBdpvN6u8")


st.markdown("""
---

### Machine Learning Web App with Streamlit

""")

st.video("https://www.youtube.com/watch?v=xl0N7tHiwlw")


st.markdown("""
---

### Build 12 data science apps with Streamlit

""")

st.video("https://www.youtube.com/watch?v=JwSS70SZdyM")


st.markdown("""
---

### Deploy Streamlit to Google Cloud Run

""")

st.video("https://www.youtube.com/watch?v=LxwoCKM1Qik")