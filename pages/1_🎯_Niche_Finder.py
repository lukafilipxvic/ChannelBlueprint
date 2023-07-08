import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
import scrapetube

st.set_page_config(
    layout="wide",
    page_title="Niche Finder",
    page_icon="🎯",
)

# Heading of App
st.write("# Niche Finder 🎯")
st.write("Haven't made your channel yet? Start by finding your Youtube niche.")

# Create header for Google Trend Request
requests_args = {
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
}

 # Create pytrends instance
pytrends = TrendReq(requests_args=requests_args)

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
    interests_df = pd.DataFrame({"interests": keywords, "interest_level": ""})
    st.divider()

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
    
        # Add a button to the app
    kw = st.radio("Select an interest to search", options=interests_df["interests"].tolist())
    
    if st.button(f'Search Youtube videos for the keyword: {kw}'):
        videos = scrapetube.get_search(kw, limit=10)
        video_list = []
        for video in videos:
            video_dict = {}
            video_dict['Title'] = video['title']['runs'][0]['text']
            video_dict['Channel'] = video['longBylineText']['runs'][0]['text']
            if 'simpleText' in video['viewCountText']:
                video_dict['View Count'] = video['viewCountText']['simpleText']
            else:
                video_dict['View Count'] = 'Live'
            video_dict['Thumbnail'] = video['thumbnail']['thumbnails'][0]['url']            
            video_dict['url'] = f"https://www.youtube.com/watch?v={video['videoId']}"
            video_list.append(video_dict)
        video_df = pd.DataFrame(video_list)
        st.dataframe(video_list, column_config={'Thumbnail': st.column_config.ImageColumn('Video Thumbnail')})