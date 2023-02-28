import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="chart_with_upwards_trend", page_title="Data Generator", layout="centered")

# with open('style.css') as f:
#      st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

# st.markdown("<h1 style='text-align: center;'>Instructions</h1>", unsafe_allow_html=True)

st.title('Instructions')

st.write(
    """
    1. Upload the data in CSV format you want to generate data on.

    2. Mention the column names as they are in the dataframe (include every column you want to generate data on).

    3. Mention the target column (required to mention **one** column)
    """
)

st.subheader('Precautions: ')

st.write(
    '''
    1. Please mention atleast one target/label column 
    '''
)

st.title('Note:')

st.write(
    '''
    1. This data generation technique uses GANs for generating data and each time new data is uploaded, GAN model is trained 
    on the new data and the quality of generated data depends on this training.

    2. Ideally for achieving best results, GAN model should be tuned each time but even without it, can achieve satisfactory results.

    3. Generated data is statistically similar to the original data and not a replica or copy of it.

    4. For more info, do visit the references in the About page. 
    '''
)