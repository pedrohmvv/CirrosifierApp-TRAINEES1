import streamlit as st
from streamlit_option_menu import option_menu # Para usar a barra de navegação
import project, data, classification, home # As outras páginas

# Configurações gerais da página
st.set_page_config(
        page_title="Cirrosifier",
        page_icon="img/project_logo.png",
        layout="wide"
        )

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
        st.markdown(
        """
        <style>
            .block-container {
                padding-top: 4rem;
            }
            .sidebar .sidebar-content {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            [data-testid="stSidebarContent"] {
                background-image: url("https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/bola.png");
            }
            [data-testid=stSidebar] [data-testid=stImage] {
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Carregar a barra lateral e os botões
    with st.sidebar:
        st.sidebar.image("img/asd.png", width=200)
        st.markdown("<h1 style='text-align: center;'>Cirrosifier</h1>", unsafe_allow_html=True)
        app = option_menu(
            menu_title="Páginas",
            icons="",
            options=["Home", "Projeto", "Dados", "Classificação"]
        )

    # Condições para checar qual botão o usuário clicou
    if app == "Home":
        home.app()
    if app == "Projeto":
        project.app()
    if app == "Dados":
        data.app()
    if app == "Classificação":
        classification.app()

    # Rodar o site
    run()