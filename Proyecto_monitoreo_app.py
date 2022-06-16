import streamlit as st
import pandas as pd
import gdown

@st.experimental_memo
def download_data():
  url = "https://drive.google.com/uc?id=17B8hm_07RhiLpL0GPhuvEQumycgzowez"
  output = 'data.csv'
  gdown.download(url,output, quiet= False)

download_data()
st.title('Monitoreo Miraflores')
st.write('Tabla:')
data=pd.read_csv('data.csv', sep=',', nrows=1000000, parse_dates=['Fecha', 'Longitud'])
st.dataframe(data.head(20))

@st.experimental_memo
def download2_data():
  url = "https://drive.google.com/uc?id=1vyN3cnVUN1aUbx_w_r3AiLXRtY4puhty"
  output = 'data2.csv'
  gdown.download(url,output, quiet= False)

download2_data()
st.title('Monitoreo Bonilla')
st.write('Tabla:')
data=pd.read_csv('data2.csv', sep=',', nrows=1000000, parse_dates=['Fecha', 'Longitud'])
st.dataframe(data.head(20))

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import scipy

df_bonilla = pd.read_excel(r'data.csv', sep=',', nrows=1000000, parse_dates=['Fecha', 'Longitud'], header= 0) 
df_miraflores= pd.read_excel(r'data2.csv', sep=',', nrows=1000000, parse_dates=['Fecha', 'Longitud'], header= 0) 

st.title("Análisis Bonilla")
st.header("Tabla de datos")
st.write(df_bonilla)
for i in range(6,15):
    fig = px.histogram(df_bonilla, df_bonilla.columns[i])
    st.plotly_chart(fig, use_container_width=True)

st.title("Análisis Miraflores")
st.header("Tabla de datos")
st.write(df_miraflores)
for i in range(6,15):
    fig = px.histogram(df_miraflores, df_miraflores.columns[i])
    st.plotly_chart(fig, use_container_width=True)

limites_maximos=[1500,1500,1500,1500,1500,1500,1500,1500,1500]
dictionary_names=dict()
for j in range(6,15):
    dictionary_names[df_bonilla.columns[j]]=df_bonilla.columns[j]+" Bonilla"
df_bonilla.rename(columns = dictionary_names, inplace=True)
df_miraflores.columns=(df_miraflores.columns+" Miraflores").values.tolist()


st.title("Comparaciones de valores entre Bonilla y Miraflores")
st.header("Histogramas")

for i in range(6,15):
    fig = ff.create_distplot(
         [df_bonilla.iloc[:, i].values.tolist(),df_miraflores.iloc[:, i].values.tolist()], [df_bonilla.columns[i],df_miraflores.columns[i]])
    st.plotly_chart(fig, use_container_width=True)
st.header("Gráficas")

for i in range(6,15):
    df_concat=[]
    df_concat=pd.concat([df_bonilla.iloc[:, [5,i]], df_miraflores.iloc[:, i]], axis=1)
    fig = px.line(df_concat, x=df_concat.columns[0], y=df_concat.columns[1:],
              hover_data={df_concat.columns[0]: "|%B %d, %Y"},
              title=df_concat.columns[1]+" vs "+df_concat.columns[2])
    print(max(df_concat.iloc[:,1:].max(axis=0)))
    if max(df_concat.iloc[:,1:].max(axis=0)) > limites_maximos[i-6]:
        fig.add_hrect(y0=limites_maximos[i-6], y1=max(df_concat.iloc[:,1:].max(axis=0)), line_width=0, fillcolor="red", opacity=0.2)
    st.plotly_chart(fig, use_container_width=True)
