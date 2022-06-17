# app.py, run with 'streamlit run app.py'

#import pip
#pip.main(["install", "openpyxl"])
#pip.main(["install", "pandas"])
#import plotly.figure_factory as ff
#pip.main(["install", "matplotlib"])
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import scipy

df_bonilla = pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Bonilla.xlsx', header= 0) 
df_miraflores= pd.read_excel(r'https://www.datosabiertos.gob.pe/sites/default/files/Monitoreo_setiembre_Ov.Miraflores.xlsx', header= 0) 

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
