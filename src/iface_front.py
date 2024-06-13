from os import path
import streamlit as st
from streamlit_extras.stylable_container import stylable_container 
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import json
from joblib import load
from numpy import array, argmax

from src.iface_config import Config

class FrontEnd:
    """iface_frontend"""

    def __init__(self):
        """Initialize instance"""
        self.config = Config()
        self.logo_path = path.join(self.config.project_dir.replace(r'src',''), "img", self.config.vars.project_logo)


    def __repr__(self):
        """Basic instance representation"""
        return "FrontEnd class"
    
    def __str__(self):
        """Print instance representation"""
        return "FrontEnd class"

    def basic_layout(self):
        """Streamlit Page Loayout"""
        st.set_page_config(self.config.vars.project_name, page_icon = self.logo_path, layout = "wide")
        st.write(self.logo_path)
        st.markdown(
        """
        <style>
        .stApp {
            background-color: white;
            h1, h2, h3, h4, h5, h6, p, span {color: black;};
        }

        </style>
        """,
        unsafe_allow_html=True  
        )
        
        c1, c2, c3 = st.columns([5, 5, 5])

        with c1:
            st.image(self.logo_path, caption='Cirrosifier Logo', use_column_width=True,)
        c1, c2, c3 = st.columns(3)

        c1.markdown(
            f"""
            <div style="padding-top: 0px; padding-bottom: 0px;">
                <h1 style="margin: 0; text-align: left;">{self.config.vars.project_name}</h1>
            </div>
            """,
            unsafe_allow_html=True
            )    
    
        st.markdown("""<hr style="height:2px;border:none;color:grey;background-color:#1b2442;" /> """,
                unsafe_allow_html=True)
        
        st.write("#")
        st.write("#")

    def menu(self):
        """Streamlit nav menu"""

        selector = option_menu(
            menu_title = "",
            options = ["Gráficos", "Classificador de Estágio"],
            default_index = 0,
            icons = ["bar-chart", "code"],
            orientation = "horizontal",
            styles = {
                "container": {"padding": "0px", 
                              "background-color": "#829da5",
                              'border-radius':'5px'},

                "icon": {"color": "white", "font-size": "20px"}, 

                "nav-link": {"font-size": "20px", "text-align": "center", 
                             "margin":"0px", "--hover-color": "#eee"},

                "nav-link-selected": {"background-color": "#1b2442",
                                      'border-radius':'5px'},
            }
    )
        if selector == "Gráficos":
            st.write("#")
            st.write('Gráficos')

        if selector == "Classificador de Estágio":
            st.write("#")
            st.spinner("Loading your model")
            c1, c2, c3, c4, c5 = st.columns([4, 4, 4, 4, 4])
            categoric_labels = [label for label, key in self.config.vars.stage_labels.items() if key =='text']
            categoric_answers = {'Sim':1, 'Não':0}
            input_array = []
            model_path = path.join(self.config.vars.models_dir,self.config.vars.stage_model)
            scaler_path = path.join(self.config.vars.scalers_dir,self.config.vars.stage_scaler)
            model = load(model_path)
            scaler = load(scaler_path)

            global all_answered 
            all_answered = True

            for i, label in enumerate(self.config.vars.stage_labels):
                formatted_label = label.replace('_', ' ')

                if i <= 8:
                    column = c2
                else:
                    column = c4

                if label in categoric_labels:
                    answer = column.selectbox(f'Informe: {label}',categoric_answers.keys())
                    answer = categoric_answers[answer]
                else:
                    answer = column.number_input(f'Insira sua taxa de {formatted_label}: ', min_value=0, key=f'taxa_{label}_stage')
                
                # Check if answer is None or empty
                if answer is None or answer == '':
                    all_answered = False
                    break

                if answer:
                    input_array.append(answer)

            if all_answered:
                input_array = array(input_array).reshape(1, -1)
                input_array = scaler.transform(input_array)
                predict_class = model.predict(input_array)
                # Escrever a classe prevista com ênfase
                st.write(f'<div style="text-align: center;"><h2 style="color: #1b2442;">Classe prevista: Estágio {argmax(predict_class) + 1}</h2></div>', unsafe_allow_html=True)
            else:
                st.warning('Por favor, responda a todas as perguntas para fazer a previsão.')
            

    