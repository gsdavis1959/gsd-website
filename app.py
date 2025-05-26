import os
import streamlit as st

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("Relaxing.jpg", width=200, height=200)
st.markdown("# Gregory S Davis")
st.markdown("## What I'm working on....")
st.markdown("""
Here are a few ideas I've been working on: 
      
Check out the named entity extraction tool 
    [here](http://website-97957.appspot.com/)
    
Try out Google's Gemini Large Language Model (LLM) 
    [here](https://gsd-gemini-2e8b5ea02d39.herokuapp.com/)

Try this AI enabled personality assessment 
    [here](https://gsd-survey-efa034351121.herokuapp.com/)

Chatbot written by Open AI's ChatGPT [here](https://covid-19-001.herokuapp.com/)

Vibe coded flight simulator created with the help of Gemini's Code Assist in VS Code [here](https://gsd-flight-sim-c2069160ff95.herokuapp.com/)

Use this tool to describe upsetting situations and feelings. Get suggestions from a chatbot based on Cognitive Behavioral Therapy (CBT) [here](https://gsd-database-535d80a01016.herokuapp.com/)  
  
    
""")





