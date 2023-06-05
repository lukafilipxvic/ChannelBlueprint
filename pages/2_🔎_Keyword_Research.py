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
keywords_input = st.text_input('Enter up to 5 keywords separated by commas to get Youtube search interest over time.', 'chatgpt, finance, ice baths')
keywords = [keyword.strip() for keyword in keywords_input.split(',')]
if len(keywords) > 5:
    st.warning('Please enter 5 or fewer keywords.')
if len(keywords) != len(set(keywords)):
    st.warning('Please enter unique keywords.')

# Create a dictionary to map dropdown options to gprop values, timeframe values
gprop_dict = {'Web Search': '', 'Image Search': 'images', 'News Search': 'news', 'Google Shopping': 'froogle', 'Youtube Search': 'youtube'}
tf_dict = {'Past hour': 'now 1-H', 'Past 4 hours': 'now 4-H', 'Past day': 'now 1-d', 'Past 7 days': 'now 7-d', 'Past 30 days': 'today 1-m','Past 90 days': 'today 3-m', 'Past 12 months': 'today 12-m', 'Past 5 years': 'today 5-y'}

# Create a dropdown menu for selecting the Search Area, Timeframe
gprop_options = list(gprop_dict.keys())
gprop = st.selectbox('Select search area', gprop_options, index=4)
tf_options = list(tf_dict.keys())
timeframe = st.selectbox('Select timeframe of search', tf_options, index=6, )

# Modify gprop and timeframe based on the selected option
gprop = gprop_dict[gprop]
timeframe = tf_dict[timeframe]

# Add a button to the app
if st.button('Get search interest over time'):
    # Make pytrends API request
    pytrends.build_payload(keywords, timeframe=timeframe, gprop=gprop)
    interest_over_time = pytrends.interest_over_time()
    related_queries = pytrends.related_queries()

    # Remove the isPartial column
    kw_interest_over_time = interest_over_time.drop(columns=['isPartial'])

    # Display the results
    st.dataframe(related_queries)
    if not interest_over_time.empty:
        st.line_chart(kw_interest_over_time)
    else:
        st.write('No data available for the given keywords.')