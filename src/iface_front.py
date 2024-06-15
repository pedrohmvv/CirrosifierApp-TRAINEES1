from os import path
import streamlit as st
from streamlit_extras.stylable_container import stylable_container 
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from joblib import load
from numpy import array, argmax

from src.iface_config import Config

class FrontEnd:
    """iface_frontend"""

    def __init__(self):
        """Initialize instance"""
        self.config = Config()
        self.logo_path = path.join(self.config.vars.img_dir, self.config.vars.project_logo)

    def __repr__(self):
        """Basic instance representation"""
        return "FrontEnd class"
    
    def __str__(self):
        """Print instance representation"""
        return "FrontEnd class"

    def basic_layout(self):
        """Streamlit Page Layout"""
        st.set_page_config(self.config.vars.project_name, page_icon=self.logo_path, layout="wide")
        st.markdown(
            """
            <style>
            .stApp {
                background: linear-gradient(to bottom right, #00008B, #FF0000);
                background-image: url('img/fundo.png'); 
                background-size: cover;
                background-repeat: no-repeat;
                color: black;
            }
            h1, h2, h3 {
                color: white;
            }
            .css-1v0mbdj {
                background-color: #1b2442; /* Cor de fundo da barra de navegação */
            }
            .css-10trblm {
                color: white; /* Cor do texto da barra de navegação */
            }
            .css-1v0mbdj a {
                color: white; /* Cor do link da barra de navegação */
            }
            .css-1v0mbdj .css-10trblm {
                font-size: 1.2em; /* Tamanho da fonte dos itens do menu */
            }
            </style>
            """,
            unsafe_allow_html=True  
        )
        
        c1, c2, c3 = st.columns([5, 5, 5])

        with c2:
            st.image(self.logo_path, caption='Cirrosifier Logo', use_column_width=True)
        
        c1, c2, c3 = st.columns(3)

        c1.markdown(
            f"""
            <div style="padding-top: 0px; padding-bottom: 0px;">
                <h1 style="margin: 0; text-align: left;">{self.config.vars.project_name}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )    
    
        st.markdown(
            """<hr style="height:2px;border:none;color:grey;background-color:#1b2442;" />""",
            unsafe_allow_html=True
        )
        
        st.write("#")
        st.write("#")

    def menu(self):
        """Streamlit nav menu"""
        selector = option_menu(
            menu_title="",
            options=["Home", "Projeto", "Dados", "Classificação"],
            default_index=0,
            icons=["house", "project-diagram", "database", "brain"],
            orientation="horizontal",
            styles={
                "container": {"padding": "0px", "background-color": "#1b2442", 'border-radius': '5px'},
                "icon": {"color": "white", "font-size": "20px"}, 
                "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#4b6584", 'border-radius': '5px'},
            }
        )
        
        st.markdown(self.config.input_style, unsafe_allow_html=True)
        st.markdown(self.config.button_style, unsafe_allow_html=True)

        if selector == "Home":
            st.markdown(
                """
                <style>
                .stApp {
                    background-image: url('img/fundo.jpeg'), linear-gradient(#002E48, #4A1C25);
                    background-attachment: fixed;
                    background-size: cover;
                    background-repeat: no-repeat;
                    color: black;
                }
                p {
                    color: black;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.write("#")
            st.write('Home')

        if selector == "Projeto":
            st.write("#")
            st.write('Projeto')

        if selector == "Dados":
            st.write("#")
            st.write('Dados')

        if selector == "Classificação":
            death_classes = {0: 'Morte', 1: 'Sobreviveu', 2: 'Transplante'}
            st.write("#")
            st.spinner("Loading your model")
            c1, c2, c3, c4, c5 = st.columns([4, 4, 4, 4, 4])
            categoric_labels = [label for label, key in self.config.vars.death_labels.items() if key == 'text']
            int_labels = [label for label, key in self.config.vars.death_labels.items() if key == 'int']
            labels = [label for label, key in self.config.vars.death_labels.items() if key == 'label']
            categoric_answers = {'Sim': 1, 'Não': 0}
            input_array = []
            model_path = path.join(self.config.vars.models_dir, self.config.vars.death_model)
            scaler_path = path.join(self.config.vars.scalers_dir, self.config.vars.death_scaler)
            model = load(model_path)
            scaler = load(scaler_path)

            for i, label in enumerate(self.config.vars.death_labels):
                formatted_label = label.replace('_', ' ')

                if i <= 4:
                    column = c2
                else:
                    column = c4

                if label in categoric_labels:
                    answer = column.selectbox(f'Informe: {label}', categoric_answers.keys())
                    answer = categoric_answers[answer]
                elif label in int_labels:
                    answer = column.number_input(f'Insira sua {formatted_label}: ', min_value=0, step=1, key=f'{label}_death')
                elif label in labels:
                    answer = column.number_input(f'Insira sua {formatted_label}: ', min_value=1, max_value=3, step=1, key=f'{label}_death')
                else:
                    answer = column.number_input(f'Insira sua taxa de {formatted_label}: ', min_value=0, key=f'taxa_{label}_death')

                input_array.append(answer)
            
            col1, col2, col3 = st.columns([1, 1, 1])
            try:
                with col2:
                    st.write('#')
                    st.write('#')
                    if st.button('Realizar Predição', key='submit'):
                        input_array = array(input_array).reshape(1, -1)
                        input_array = scaler.transform(input_array)
                        predict_class = model.predict(input_array)
                        st.write(f'<div style="text-align: center;"><h2 style="color: #1b2442">Classe prevista: {death_classes[argmax(predict_class)]}</h2></div>', unsafe_allow_html=True)
            except ValueError:
                st.markdown(
                    """
                    p {color: black}
                    """
                )
                st.warning('Por favor responda todas para realizar a predição')

        if selector == "Classificador de Estágio":
            st.write("#")
            st.spinner("Loading your model")
            c1, c2, c3, c4, c5 = st.columns([4, 4, 4, 4, 4])
            categoric_labels = [label for label, key in self.config.vars.stage_labels.items() if key == 'text']
            int_labels = [label for label, key in self.config.vars.stage_labels.items() if key == 'int']
            categoric_answers = {'Sim': 1, 'Não': 0}
            input_array = []
            model_path = path.join(self.config.vars.models_dir, self.config.vars.stage_model)
            scaler_path = path.join(self.config.vars.scalers_dir, self.config.vars.stage_scaler)
            model = load(model_path)
            scaler = load(scaler_path)

            for i, label in enumerate(self.config.vars.stage_labels):
                formatted_label = label.replace('_', ' ')

                if i <= 4:
                    column = c2
                elif 4 < i <= 9:
                    column = c3
                else:
                    column = c4

                if label in categoric_labels:
                    answer = column.selectbox(f'Informe: {label}', categoric_answers.keys())
                    answer = categoric_answers[answer]
                elif label in int_labels:
                    answer = column.number_input(f'Insira sua {formatted_label}: ', min_value=0, step=1, key=f'{label}_stage')
                else:
                    answer = column.number_input(f'Insira sua taxa de {formatted_label}: ', min_value=0, key=f'taxa_{label}_stage')

                input_array.append(answer)
            
            col1, col2, col3 = st.columns([1, 1, 1])
            try:
                with col2:
                    st.write('#')
                    st.write('#')
                    if st.button('Realizar Predição', key='submit'):
                        input_array = array(input_array).reshape(1, -1)
                        input_array = scaler.transform(input_array)
                        predict_class = model.predict(input_array)
                        st.write(f'<div style="text-align: center;"><h2 style="color: #1b2442">Classe prevista: {predict_class[0]}</h2></div>', unsafe_allow_html=True)
            except ValueError:
                st.markdown(
                    """
                    p {color: black}
                    """
                )
                st.warning('Por favor responda todas para realizar a predição')
