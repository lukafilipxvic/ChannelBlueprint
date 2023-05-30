import streamlit as st
import pandas as pd
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

st.set_page_config(
    layout="wide",
    page_title="Transcript Downloader",
    page_icon="📄",
)

# Heading of App
st.write("# Transcript Downloader 📄")

# Type in video URL
video_id = st.text_input("Enter Youtube video ID")

if "https://" in video_id or "youtu" in video_id:
    st.warning("Please enter video ID only")

if st.button("Get Transcript"):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    formatter = TextFormatter()

    # .format_transcript(transcript) turns the transcript into a JSON string.
    txt_transcript = formatter.format_transcript(transcript)

    # Columns to sort informative info annd download button
    col1, col2, col3 = st.columns([3,1,1], gap="small")
    # Download txt_transcript as a txt file
    col1.download_button(
        label="Download txt file",
        data=txt_transcript.encode('utf-8'),
        file_name="transcript.txt",
        mime="text/plain")
    
    # Count the number of words in txt_transcript
    word_count = len(txt_transcript.split())
    col2.write(f'Word count: {word_count}')

    # Print text formatted transcript
    st.write(txt_transcript)