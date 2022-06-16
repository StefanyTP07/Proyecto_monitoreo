import streamlit as st
import pandas as pd
import gdown

@st.experimental_memo
def download_data():
  url = 'https://docs.google.com/uc?id=1tReqZLXKH569JkzNQ7cc8kTFA11UdN6qI2PgvDvE6zs'
  output = 'data.csv'
  gdown.download(url,output, quiet= False)

download_data()
data=pd.read_csv('data.csv', sep=';', nrows=1000000, parse_dates=['Fecha', 'Longitud'])
st.dataframe(data.head(20))
