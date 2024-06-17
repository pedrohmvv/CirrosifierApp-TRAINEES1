import streamlit as st
from streamlit_option_menu import option_menu # Para usar a barra de navegação

import src.classification
import src.data, src.home, src.project # As outras páginas

# Configurações gerais da página
st.set_page_config(
        page_title="Cirrosifier",
        page_icon="img/project_logo.png",
        layout="wide"
        )
img = "img/project_logo.png"

class MultiApp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        # Markdown para estilizar a barra lateral
        st.markdown( # Eu nem sei se essa importação da fonte da TAIL tá dando certo de verdade
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');
            html {
                font-family: "Inter";
            }
            .block-container {
                padding-top: 4rem;
            }
            .sidebar .sidebar-content {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            [data-testid=stSidebar] [data-testid=stImage] {
                text-align: center;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
            }
            .stImage {
                border-radius: 3px;
                box-shadow: 0 0 2px rgba(255,255,255, 0.6);
            }
            .st-emotion-cache-ubko3j {
                display: none;
            }
            .container {
                    display: flex;
                    align-items: center;
                    justify-content: center
                    }
            
        </style>
        """,
        unsafe_allow_html=True
    )

    # Carregar a barra lateral e os botões
    with st.sidebar:
        st.sidebar.markdown("<div class='container'><img src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/main/img/project_logo.png' style='width:200px;height:200px'; alt='GitHub'></div>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center;'>Cirrosifier</h1>", unsafe_allow_html=True)
        app = option_menu(
            menu_title="Páginas",
            icons=["house", "code", "bar-chart", "sliders"],
            options=["Home", "Projeto", "Dados", "Classificação"],
            styles={
                "menu-title": {"text-align": "center"},
                "nav-link": {"--hover-color": "#262730", "text-align": "center"},
                "nav-link-selected": {"background-color": "#95003d"},
            }
        )

    # Condições para checar qual botão o usuário clicou
    if app == "Home":
        src.home.app()
    if app == "Projeto":
        src.project.app()
    if app == "Dados":
        src.data.app()
    if app == "Classificação":
        src.classification.app()

    # Rodar o site
    run()