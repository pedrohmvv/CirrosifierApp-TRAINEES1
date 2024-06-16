import streamlit as st

st.sidebar.selectbox('Gráfico', options=['Análise 1', 'Análise 2'], index=0)

def app():
    st.write("Projeto")