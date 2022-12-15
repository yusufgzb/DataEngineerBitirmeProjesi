import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 
import os
from google.cloud import bigquery

def bigquery_get_df(query="SELECT * FROM idsadb.idsadb_table"):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'mineral.json'
    client = bigquery.Client()

    table_id = "mineral-rune-365815.idsadb.idsadb_table"
    QUERY = (
        query)
    query_job = client.query(QUERY)  # API request

    rows = query_job.result()  # Waits for query to finish
    row_list=[]
    for row in rows:
            value=[row[0],row[1],row[2],row[3]]
            row_list.append(value)
    df = pd.DataFrame(row_list,columns =['Names','Country','Local Time','Temp'])
       
    return df


# read csv from a github repo
df = bigquery_get_df()

st.set_page_config(
    page_title = 'Real-Time Data Engineer Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time / Live Data Engineer Dashboard")

# top-level filters 

job_filter = st.selectbox("İl Seçin", pd.unique(df['Names']))


# creating a single-element container.
placeholder = st.empty()

# # dataframe filter 

df = df[df['Names']==job_filter]

# near real-time / live feed simulation 

while True: 
    df = bigquery_get_df()
    

    with placeholder.container():



        fig_col1, fig_col2, fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("### Sıcaklık Yaılım Grafiği(Tüm İller)")
            fig = px.density_heatmap(data_frame=df, y = 'Temp', x = 'Names')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame = df[df['Names']==job_filter], x = 'Local Time')
            st.write(fig2)
        with fig_col3:
            st.markdown("### Second Chart")
            fig3 = px.pie(df[df['Names']==job_filter], values='Temp', names='Local Time', title='Population of European continent')
            st.write(fig3)


        st.markdown("### Detailed Data View")
        st.dataframe(df[df['Names']==job_filter],use_container_width = True)
        
        time.sleep(1)
