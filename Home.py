import streamlit as st

st.set_page_config(
    page_title="World Cities",
    page_icon="🌍",
    layout="centered",
)

st.title("🌍 World Cities")
st.write("Welcome to the World Cities app! Explore cities and discover information about them.")

if st.button("Go to the app", type="primary"):
    st.switch_page("pages/app.py")
