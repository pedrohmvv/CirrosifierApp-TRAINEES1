import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_option_menu import option_menu

def app():
    option = st.selectbox(
        "Selecione o Gráfico",
        ("Bilirrubina", 
         "Albumina", 
         "Expectativa de Vida",
         "Mortalidade por Estágio",
         "Mortalidade por Sexo"))

        
    st.write("Gráfico:", option)
    option = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
    }
    st.header("Placeholder, colocar uns 5 6 graficos massa aqui")
    st_echarts(
        options=option, height="400px"
    )