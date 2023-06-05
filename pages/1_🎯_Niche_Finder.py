import streamlit as st
import pandas as pd
from pytrends.request import TrendReq

st.set_page_config(
    layout="wide",
    page_title="Niche Finder",
    page_icon="🎯",
)

# Heading of App
st.write("# Niche Finder 🎯")
st.write("Haven't made your channel yet? Start by finding your Youtube niche.")
 
 # Create pytrends instance
pytrends = TrendReq()

# Get user to type in a number of hobbies in a single textbox
keywords_input = st.text_input('Enter 5-8 interests/hobbies separated by commas to start finding your niche', "finance, coding, streamlit, photography, python")

if keywords_input:
    keywords = [keyword.strip() for keyword in keywords_input.split(',')]
    if len(keywords) < 5:
        st.warning('Enter 5 or more areas of hobbies/interest')
    if len(keywords) > 8:
        st.warning('Enter 8 or fewer areas of hobbies/interest')
    if len(keywords) != len(set(keywords)):
        st.warning('Enter unique hobbies/interest')
    
    # Create an editable df to rank the hobbies by interest level
    st.divider()
    st.write("Assign an interest level to your hobbies/interest:")
    interests_df = pd.DataFrame({"interests": keywords, "interest_level": ""})
    edited_interests_df = st.data_editor(interests_df, column_config={
        "interests": st.column_config.Column("Interests/Hobbies", 
        width="medium", required=True),
        "interest_level": st.column_config.NumberColumn("Your rating",
            help="What is your interest level in this topic?",
            min_value=1, max_value=5, step=1, required=True),
            }, disabled=["interests"], hide_index=True)
    st.divider()

    # Add a button to the app
    if st.button('Get Youtube search interest of your hobbies'):
        # Make pytrends API request
        pytrends.build_payload(keywords, gprop="youtube")
        interest_over_time = pytrends.interest_over_time()

        # Remove the isPartial column
        kw_interest_over_time = interest_over_time.drop(columns=['isPartial'])

        # Display the results
        if not interest_over_time.empty:
            st.line_chart(kw_interest_over_time)
        else:
            st.write('No data available for the given keywords.')