import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Cirrosifier",
    page_icon="img/project_logo.png"
)

with st.sidebar:
    st.sidebar.image("https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/project_logo.png")
    st.title("Cirrosifier")
    selected = option_menu(
        menu_title="Páginas",
        icons="",
        options=["Home", "Projeto", "Dados", "Classificação"]
    )

    if selected == "Home":
        st.title(f"Você selecionou {selected}")
    if selected == "Projeto":
        st.title(f"Você selecionou {selected}")
    if selected == "Dados":
        st.title(f"Você selecionou {selected}")
    if selected == "Classificação":
        st.title(f"Você selecionou {selected}")

    st.sidebar.selectbox('Gráfico', options=['Análise 1', 'Análise 2'], index=0)

option = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
}
st.title("Média de Bilirrubina por Estágio")
st_echarts(
    options=option, height="400px"
)