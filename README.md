# Hacker-News-Active-Discussion-
<img src="https://github.com/arghanilhub/Hacker-News-Active-Discussion-/blob/main/hc.png" alt="Y combinator"
 style="width:50px;height:60px;">  
Giving users to know on which latest submissions- most disucssions are going on in the Hacker News. 
<br />

### Tech stack used : 
* Python (used for scripting) and HTML (for UI) <br /> 
* 3rd party libraries used : Request( for API calling), Plotly (for visualization), Streamlit (for deployment of this data app on cloud) 
<br />

### Context of the webpage : 
* This web page will provide you a visual for first 10 submissions on Hacker News and from that you will able to know, **on which submission most active discussions are going on**, which gives user a better reading experience, as they can click on the submission titles and reach to that actual discussion page for that submission. <br />
* It gives you the updated data(near real time)
<br />

 ### Concepts used : 
 * ETL framework used here, where extraction of Hacker News submission data from their **top stories** and **each submission** API endpoints. <br />
 * Processed those data to build datasets and load into visualization scipt. <br />
 * Made an Interactive chart with **plotly express** from those datasets . <br /> 
 * Wrap the whole script under **Streamlit framework** for deploying the data app, in their community clounds and also for UI purposes. <br />
 * Solved the slow loading in streamlit servers, by using the **catching** concept in the script. 
  
