import streamlit as st
import pandas as pd
import numpy as np
# from gan import GAN



st.set_page_config(page_icon="chart_with_upwards_trend", page_title="Data Generator", layout="centered")

# with open('style.css') as f:
#      st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

# st.markdown("<h1 style='text-align: center;'>Instructions</h1>", unsafe_allow_html=True)

st.title('About')

st.write(
    '''
    In the data science world, the amount of data can play a crucial role in performing various analysis. But in fields such as Mining, Pharmaceutics and Medicine, 
    the amount of data available is very less and recording extra data is very expensive or sometimes just impossible.
    Synthetic Data Generator webapp is useful in developing new data using AI. Synthetically generated data is statistically similar 
    to the original data but is entirely different from the original data. 
    '''
)