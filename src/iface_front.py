import streamlit as st
from streamlit_option_menu import option_menu
from os import path

from src.config import Config
from src.classification import Classification
from src.data import Data
from src.home import Home
from src.project import Project

class FrontEnd():
    """FrontEnd class"""

    def __init__(self):
        self.home = Home() # Home section class
        self.project = Project() # Project section class
        self.data = Data() # Data section class
        self.classification = Classification() # Classification section class
        self.config = Config() # Config class
        self.project_logo = self.config.vars.project_logo # Project logo path
        self.project_name = self.config.vars.project_name # Project name

    def __home(self):
        """Generates home section"""
        return self.home.home()
    
    def __project(self):
        """Generates project section"""
        return self.project.project()
    
    def __data(self):
        """Generates data section"""
        return self.data.data()
    
    def __classification(self):
        """Generates classification section"""
        return self.classification.classification()
    
    def main(self):
        """Main generator function"""

        # Set the page config
        st.set_page_config(
            page_title=self.project_name,
            page_icon=self.project_logo,
            layout="wide"
            )

        # Set the main style
        st.markdown(self.config.main_style,unsafe_allow_html=True)

        # Set the sidebar
        with st.sidebar:
            st.sidebar.markdown(f"<div class='container'><img src={self.project_logo} style='width:200px;height:200px'; alt='GitHub'></div>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='text-align: center;'>{self.project_name}</h1>", unsafe_allow_html=True)
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

        # Generates sections
        if app == "Home":
            return self.__home()
        if app == "Projeto":
            return self.__project()
        if app == "Dados":
            return self.__data()
        if app == "Classificação":
            return self.__classification()
