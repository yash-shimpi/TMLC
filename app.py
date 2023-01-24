import streamlit as st
import pandas as pd
import numpy as np
from gan import GAN



st.set_page_config(page_icon="📊", page_title="CSV Wrangler", layout = "wide")

with open('style.css') as f:
     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)
     
st.markdown("<h1 style='text-align: center;'>Synthetic Data Generator App 🗂️</h1>", unsafe_allow_html=True)

def main():
    uploaded_file = st.file_uploader(
            "",
            key="1",
            help="To activate 'wide mode', go to the hamburger menu > Settings > turn on 'wide mode'",
        )

    if uploaded_file is not None:
            file_container = st.expander("Check your uploaded .csv")
            shows = pd.read_csv(uploaded_file)
            uploaded_file.seek(0)
            file_container.write(shows)

    else:
            st.info(
                f"""
                    👆 Upload a .csv file first. Sample to try: [biostats.csv](https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv)
                    """
            )

            st.stop()

    df = pd.read_csv(
        uploaded_file, 
        na_values=['NA', '?'])

    with st.form('Data Information'):
        st.subheader("Enter following information for your data:")

        Columns = st.text_input(label='Columns to be used including Target column (Ex: col1, col2, col3, ... )')
        Target = st.text_input(label='Target Column')

        submit = st.form_submit_button(label='Submit')

    if submit:
        # print(Columns.dtype)
        List_col = Columns.split(", ")
        List_tar = Target.split(",")
        gen_data = GAN(df, List_col, List_tar)
        # gen_data.to_csv('file.csv')
        # st.download_button()

        st.download_button(label = 'Download CSV', data = gen_data.to_csv(), file_name = 'gen.csv')
            # st.write('Thanks for downloading!')

if __name__ == '__main__':
    main()

#Data visualization metric
#developed by .... 
# Name,"Sex","Age","Height (in)","Weight (lbs)" 