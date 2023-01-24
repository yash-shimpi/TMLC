import streamlit as st
import pandas as pd
import numpy as np
# from gan import GAN



st.set_page_config(page_icon="chart_with_upwards_trend", page_title="Data Generator", layout="centered")

with open('style.css') as f:
     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

# st.markdown("<h1 style='text-align: center;'>Instructions</h1>", unsafe_allow_html=True)

st.title('Instructions')