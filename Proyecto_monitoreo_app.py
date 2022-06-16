import streamlit as st
import pandas as pd
import numpy as np
import urllib.request

print('Beginning file download with urllib2...')

@st.experimental_memo
def download_data():
  url = 'https://files.minsa.gob.pe/s/eRqxR35ZCxrzNgr/download'
  filename = 'data.csv'
  urllib.request.urlretrieve(url, 'data.csv')
  return filename


st.write(download_data())


n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)
