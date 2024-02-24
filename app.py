import os
import streamlit as st

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("Relaxing.jpg")
st.markdown("# Gregory S Davis")
st.markdown("## What I'm working on....")
st.markdown("""
Here are a few ideas I've been working on: 
      
Check out the named entity extraction tool 
    [here](http://website-97957.appspot.com/)
    
Try out Google's Gemini Large Language Model (LLM) 
    [here](https://gsd-gemini-2e8b5ea02d39.herokuapp.com/)

Ask Open AI to analyze a graph or image [here](https://gsd-graph-analysis-d87538823918.herokuapp.com/)

Chatbot written by Open AI's ChatGPT [here](https://covid-19-001.herokuapp.com/)

If you need a bad joke, give this a try [here](https://gsd-joke-abd69206d90b.herokuapp.com/)  
  
    
""")





