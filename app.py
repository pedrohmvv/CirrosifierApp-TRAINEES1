import streamlit as st
from streamlit_option_menu import option_menu

import project, data, classification, home

class MultiApp:
    
    def __init__(self):
        self.apps = []
        st.set_page_config(
        page_title="Cirrosifier",
        page_icon="img/project_logo.png"
        )

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            align-items: center;
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

    with st.sidebar:
        st.sidebar.image("img/asd.png", width=200)
        st.markdown("<h1 style='text-align: center;'>Cirrosifier</h1>", unsafe_allow_html=True)
        app = option_menu(
            menu_title="Páginas",
            icons="",
            options=["Home", "Projeto", "Dados", "Classificação"]
        )

    if app == "Home":
        home.app()
    if app == "Projeto":
        project.app()
    if app == "Dados":
        data.app()
    if app == "Classificação":
        classification.app()

    run()