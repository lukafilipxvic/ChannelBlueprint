import streamlit as st
import pandas as pd
from pytrends.request import TrendReq


st.set_page_config(
    layout="centered",
    page_title="Keyword Research",
    page_icon="🔎",
)

# Heading of App
st.write("# Keyword Research 🔎")
st.write('Enter a keyword to get search interest over time.')

# Create pytrends instance
pytrends = TrendReq()

# Get user input
keyword = st.text_input('Enter a keyword to get search interest over time.', 'chatgpt')

# Make pytrends API request
pytrends.build_payload([keyword])
interest_over_time = pytrends.interest_over_time()

# Display the results
if not interest_over_time.empty:
    st.line_chart(interest_over_time[keyword])
else:
    st.write('No data available for the given keyword.')
