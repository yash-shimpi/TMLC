import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from gan import GAN

st.set_page_config(page_icon="chart_with_upwards_trend", page_title="Data Generator", layout="centered")

# with open('style.css') as f:
#      st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

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
                    👆 Upload a .csv file first. Sample to try: [auto-mpg.csv](https://drive.google.com/file/d/1szGbzgfhqyOhNISkEoIH-q_mKzto9irY/view?usp=sharing)
                    """
            )

            st.stop()

    df = pd.read_csv(
        uploaded_file, 
        na_values=['NA', '?'])
    # for col in df.columns:    
    st.write("Columns in uploaded Dataset: ")         
    st.write(list(df.columns))
    with st.form('Data Information'):
        st.subheader("Enter following information for your data:")

        Columns = st.multiselect('Columns to be used: ', list(df.columns))
        Target = st.multiselect('Target Column: ', list(df.columns))

        submit = st.form_submit_button(label='Submit')

    if submit:
        List_col = Columns
        List_tar = Target
        gen_data = GAN(df, List_col, List_tar)

        st.download_button(label = 'Download CSV', data = gen_data.to_csv(), file_name = 'gen.csv')
        
        file_container_gen = st.expander("Check your Generated data")
        file_container_gen.write(gen_data)

        c1,c2=st.columns(2)

        c1.subheader("Original Data Summary")
        c1.write(df.describe())

        c2.subheader("Generated Data Summary")
        c2.write(gen_data.describe())

        df_corr = df.corr() # Generate correlation matrix
        fig = go.Figure()
        fig.add_trace(
            go.Heatmap(
                x = df_corr.columns,
                y = df_corr.index,
                z = np.array(df_corr)
            )
        )
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()

#Data visualization metric
#developed by .... 
# Name,"Sex","Age","Height (in)","Weight (lbs)" 