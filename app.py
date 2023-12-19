import os
import streamlit as st

st.markdown("# Gregory S Davis")
st.markdown("## What I'm working on....")
st.markdown("""
    I've created a few small Data Science, Python, R and related projects. 
    
    Find me on Google Scholar
    [page](https://scholar.google.com/citations?user=DB6vA7gAAAAJ&hl=en).    
    
    Check out the named entity extraction tool [here](http://website-97957.appspot.com/)
    
    
    
    
""")

with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("Relaxing.jpg")

    with text_col:
        st.subheader("ChatGPT")
        st.write("""Ask the chatbot questions and interact with OpenAI's ChatGPT
            """)
        st.markdown("[here](https://covid-19-001.herokuapp.com/)")

