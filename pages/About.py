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

st.subheader('Technology used: ')

st.write(
    '''
    The core technology used behind Synthetic data generation is CTGANs (Conditional Tabular Generative Adversarial Networks).
    CTGANs are basically GAN models modified for accepting and generating tabular data. GANs are generative models used to generate images,
    sound, text and now tabular data. GANs are made from combining two Neural Networks models and training them against each other. One is Generator
    and other is Discriminator. Generator's task is to generate fake data that can resemble the real data such that it can fool the Discriminator model
    while Discriminator model's task is to Discriminate between real and generated fake data. Generator is penalised if fake data is detected by discriminator.
    Both these models are trained simultaneously, where generator becomes better and better in generating fake data such that it can fool the discriminator.
    '''
)

st.subheader('About the project: ')

st.write(
    '''
    This webapp is developed by Yash Shimpi under the guidance of TMLC ([The Machine Learning Co.](https://themlco.com/)) Fellowship Programme. 
    '''
    '''
    Reference Links:
    1. Generative Adversarial Networks - [**GANs**](https://arxiv.org/pdf/1406.2661.pdf)
    2. Conditional Tabular GANs - [**CTGAN**](https://proceedings.neurips.cc/paper/2019/file/254ed7d2de3b23ab10936522dd547b78-Paper.pdf)
    3. TabGANs by diyago - [Github](https://github.com/Diyago/GAN-for-tabular-data)
    '''
)
c1, c2, c3 = st.columns(3)
with c1:
    st.info('**LinkedIn: [Yash Shimpi](https://www.linkedin.com/in/yash-shimpi-42328b1b9/)**', icon="💻")
with c2:
    st.info('**GitHub: [@yash-shimpi](https://github.com/yash-shimpi)**', icon="🐱")
with c3:
    st.info('**shimpiyash573@gmail.com**', icon="📩")

