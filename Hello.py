import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Alex's SideProject",
    page_icon=":necktie:"
)

st.write("# Welcome to myPage! 👋")

st.sidebar.success("Select a page to visit.")

st.markdown(
    """
    ### The pages within this App tell the story about how I used some libraries in Python :snake: to aquire data, analyze it and implement a model on it.  
    **👈 Select a Page for you to explore!
    ### Sections to explore in this App  
    - About BAFA :football: This page has some information about the British American Football Association (BAFA)
    - Data Collection and Questions :computer: Here one can find a brief explanation on how the data was collected and integrated 
    - Findings :mag_right: :bar_chart: Some findings about the data (this page contains a good number of graphs it may take long to show) 
    - Dashboard :bulb: Here one can make their own queries on the data to get some insights 
    - Models :chart_with_upwards_trend:

    ### The overall approach was
    - Webscrapping and API's
    - Data Integration 
    - Data Analysis
    - ML
"""
)


with st.expander('About Me'):
    
    st.markdown(
        """
        #### PhD Candidate on management science at Strathclyde University Business School. Currently working on bi-level optimization.
        #### AFHEA, MBA, M.Eng, Industrial Engineer 
        ##### Interests:
        - Linear Optimization
        - Mixed Integer Linear Optimization
        - Discrete Network Optimization
        - Data Analysis
        - Teaching  

    """
    )

    st.markdown(
        """ 
        ### Contact Details
        - e-mail : alexander_vindel@gmail.com
        - LinkedIn : [alexander-vindel](https://www.linkedin.com/in/alexander-vindel/)
        - GitHub : [@j-alex-vindel](https://github.com/j-alex-vindel)

        """)
