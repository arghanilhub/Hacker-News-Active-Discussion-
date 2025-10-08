<img src="https://github.com/arghanilhub/Hacker-News-Active-Discussion-/blob/main/hc.png" alt="Y combinator"
 style="width:60px;height:60px;"> 
 ## Instantly Find the Hottest, Real-Time Discussions on Hacker News 
 [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://hackernewsdiscussions.streamlit.app/)  
Shows which recent Hacker News submissions are generating the hottest, **near-real time discussions**, giving readers a direct entry point to actively participate in the most **current trending topics**. 
<br />
### Tech stack used :
* Python (for scripting and data processing) <br /> 
* 3rd party libraries used : Requests( for API calling), Plotly (for visualization), Streamlit (for deploying data app in cloud and UI)   
<br />

### Context of the webpage :
* This web page will provide you a visual for first 10 submissions on Hacker News and from that you will able to know, **on which submission most active discussions are going on**, which gives user a better reading experience, as they can click on the submission titles and reach to that actual discussion page for that submission. <br />
* It gives you the updated data(near real time)
<br />

 ### Concepts used :
 * ETL framework used here, where extraction of Hacker News submission data from their **top stories** and **each submission** API endpoints. <br />
 * Processed those data to build datasets on no. of comments they got, interactive submission titles and hover texts for upvotes. <br />
 * Made an Interactive chart with **plotly express** from those datasets . <br /> 
 * Wrap the whole script under **Streamlit framework** for deploying the data app, in their community clounds and also for UI purposes, used streamlit markdown and html tags. <br />
 * Solved the slow loading in streamlit servers, by using the **catching** concept in the script. 
   
