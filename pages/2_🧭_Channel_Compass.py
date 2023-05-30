import streamlit as st
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

st.set_page_config(
    layout="centered",
    page_title="Channel Compass",
    page_icon="🧭",
)

# Heading of App
st.write("# Channel Compass 🧭")

# Get the three pillars from the user
st.markdown("## Channel Pillars")
p1, p2, p3 = st.columns(3, gap="small")
pillar1 = p1.text_input("Enter Pillar 1:", "Finance")
pillar2 = p2.text_input("Enter Pillar 2:", "Personal Development")
pillar3 = p3.text_input("Enter Pillar 3:", "Film")


# Create a pytrends object
if st.button("Run"):
    st.write("tbd.")