import streamlit as st
from pytrends.request import TrendReq

st.set_page_config(
    layout="centered",
    page_title="ChannelBlueprint",
    page_icon="📺",
)

st.sidebar.success("Select a page above.")

# Heading of App
st.write("# Channel Blueprint 📺")

# Get the three pillars from the user
pillar1 = st.text_input("Enter Pillar 1:")
pillar2 = st.text_input("Enter Pillar 2:")
pillar3 = st.text_input("Enter Pillar 3:")

# Create a pytrends object
pytrends = TrendReq()

