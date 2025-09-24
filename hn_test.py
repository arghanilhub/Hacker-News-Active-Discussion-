# Showing *active disucessed* submission present on the home page of HACKER NEWS. 

import streamlit as st 
import requests
import plotly.express as px



#-----1. Catched data fetching ----------
@st.cache_data(ttl=600)   # cache for 10 minutes 
def fetch_top_stories(limit=10):
    """Fetch top Hacker News submissions (with details)"""
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    r = requests.get(url) 
    print(f"Status code : {r.status_code}") 
    submission_ids = r.json()  # processing the response 


    article_links, article_comments, hover_texts = [], [], []
    for submission_id in submission_ids[:limit]:
        # Make API call for each submission_id 
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json" 
        r = requests.get(url) 
        print(f"id :{submission_id}\tstatus code: {r.status_code}") 
        response_dict = r.json()  

        
        # Process each article_dict to extract certain data to *create datasets* for visualization
        # Shorten titles
        title = response_dict['title'] 
        if len(title)> 30:
            title = title[:30] + "..." 

        # Clickable links 
        hn_url =  f"https://news.ycombinator.com/item?id={submission_id}" 
        article_link = f"<a href='{hn_url}'>{title}</a>" 
        article_links.append(article_link) 

        # comments  
        article_comments.append(response_dict['descendants']) 

        # hover_text
        ar_name = response_dict['title']
        upvotes = response_dict['score']
        hover_text = f"{ar_name}<br />upvotes: {upvotes}" 
        hover_texts.append(hover_text) 
    
    return article_links, article_comments, hover_texts 



# ------2. Streamlit UI -----------
# Web-page Title 
st.markdown(
    "<h3>Top 10 Active Discussions on "
    "<span style='background-color:red; color:white; border:2px solid black; padding:2px;'>Hacker News</span>"
    "</h3>",
    unsafe_allow_html=True
) 

# Context of the page 
st.write(
    "See the top 10 posts from Hacker News, with a quick visual cue showing where the active discussions are happening."
)

# chart-interactive context 
st.markdown(
    "<p style='color:green; font-size:16px;'> You can also click on a submission title to view the discussion page</p>", 
            unsafe_allow_html=True 
    ) 

article_links, article_comments, hover_texts = fetch_top_stories()   # call the function  


#------ 3. Visualization ------------------
#title = '' 
labels = {'x' :'Submissions', 'y' :'No. of Comments'}
fig = px.bar(x=article_links, y=article_comments, labels=labels, hover_name=hover_texts)

fig.update_layout(xaxis_title_font_size=20, yaxis_title_font_size=20) 
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6, hoverlabel=dict(
    bgcolor="blue",
    bordercolor="black",
    font_size=14,
    font_color="white"
))

# Show chart in streamlit 
st.plotly_chart(fig, use_container_width=True)  

