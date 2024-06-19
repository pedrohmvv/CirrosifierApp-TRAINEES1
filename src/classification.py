import streamlit as st
from os import path
import streamlit as st
from streamlit_extras.stylable_container import stylable_container 
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from joblib import load
from numpy import array, argmax

from src.config import Config

class Classification:
    """Classifications section class"""

    def __init__(self):
        self.config = Config()
        self.stage_model = load(path.join(self.config.vars.models_dir,self.config.vars.stage_model)) # Load the stage model
        self.stage_scaler = load(path.join(self.config.vars.scalers_dir,self.config.vars.stage_scaler)) # Load the stage scaler
        self.death_model = load(path.join(self.config.vars.models_dir,self.config.vars.death_model)) # Load the death model
        self.death_scaler = load(path.join(self.config.vars.scalers_dir,self.config.vars.death_scaler)) # Load the death scaler
        
    def classification(self) -> None:
        """Classification section generator function
           return: None
        """

        # Set the classification section style
        st.markdown(self.config.classification_style, unsafe_allow_html=True)

        # Set the inputs style
        st.markdown(self.config.input_style, unsafe_allow_html=True)
        
        # Classification selection
        st.header("Classificação")
        option = st.selectbox(
            "Selecione a Análise",
            ("Estágio", 
            "Situação" ))
        
        st.write("Classificação:", option)

        if (option == "Estágio"):
            st.spinner("Loading your model")
            c1, c2, c3, c4, c5, c6, c7 = st.columns([5, 5, 5, 5, 5, 5, 5], gap="small")
            categoric_labels = [label for label, key in self.config.vars.stage_labels.items() if key =='text'] # Get the categoric inputs
            int_labels = [label for label, key in self.config.vars.stage_labels.items() if key =='int'] # Get the integer inputs
            categoric_answers = {'Sim':1, 'Não':0} # Map the categoric answers values
            input_array = []

            for i, label in enumerate(self.config.vars.stage_labels):
                formatted_label = label.replace('_', ' ')

                if (i <= 4):
                    column = c2
                elif (4 < i <= 9):
                    column = c4
                else:
                    column = c6

                if (label in categoric_labels):
                    answer = column.selectbox(f'Informe: {label}',categoric_answers.keys())
                    answer = categoric_answers[answer]
                elif (label in int_labels):
                    answer = column.number_input(f'Insira sua {formatted_label}: ', min_value=0, step=1, key=f'{label}_stage')
                else:
                    answer = column.number_input(f'Insira sua taxa de {formatted_label}: ', min_value=0.0, key=f'taxa_{label}_stage', format="%.2f")

                input_array.append(answer)
            
            
            col1, col2, col3 = st.columns([1,1,1])
            try:
                with col2:
                    st.write("<br>", unsafe_allow_html=True)
                    if st.button('Realizar Predição', key='submit'):
                        input_array = array(input_array).reshape(1, -1)
                        input_array = self.stage_scaler.transform(input_array) # Input array trasnform
                        predict_class = self.stage_model.predict(input_array) # Input prediction
                        st.write(f'<div style="text-align: center;"><h2 style="color: #3498db">Classe prevista: Estágio {argmax(predict_class) + 1}</h2></div>', unsafe_allow_html=True)
            except ValueError:
                st.markdown(
                    """
                    p {color: black}
                    """
                )
                st.warning('Por favor responda todas para realizar a predição')
        
        if (option == "Situação"):
            death_classes = {0: 'Morte', 1:'Sobreviveu', 2:'Transplante'} # Remap the situation labels
            st.spinner("Loading your model")
            c1, c2, c3, c4, c5 = st.columns([4, 4, 4, 4, 4])
            categoric_labels = [label for label, key in self.config.vars.death_labels.items() if key =='text'] # Get the categoric inputs
            int_labels = [label for label, key in self.config.vars.death_labels.items() if key =='int'] # Get the integer inputs
            labels = [label for label, key in self.config.vars.death_labels.items() if key =='label'] # Get the labels
            categoric_answers = {'Sim':1, 'Não':0} # Map the categoric answers values
            input_array = []

            for i, label in enumerate(self.config.vars.death_labels):
                formatted_label = label.replace('_', ' ')

                if (i <= 4):
                    column = c2
                else:
                    column = c4

                if (label in categoric_labels):
                    answer = column.selectbox(f'Informe: {label}',categoric_answers.keys())
                    answer = categoric_answers[answer]
                elif (label in int_labels):
                    answer = column.number_input(f'Insira sua {formatted_label}: ', min_value=0, step=1, key=f'{label}_death')
                elif (label in labels):
                    answer = column.number_input(f'Insira seu {formatted_label}: ', min_value=1,max_value=3, step=1, key=f'{label}_death')
                else:
                    answer = column.number_input(f'Insira sua taxa de {formatted_label}: ', min_value=0.0, key=f'taxa_{label}_death', format="%.2f")

                input_array.append(answer)
            
            col1, col2, col3 = st.columns([2,2,2])
            st.markdown(self.config.classification_style,unsafe_allow_html=True
            )
            try:
                with col2:
                    st.write("<br>", unsafe_allow_html=True)
                    if st.button('Realizar Predição', key='submit'):
                        input_array = array(input_array).reshape(1, -1)
                        input_array = self.death_scaler.transform(input_array) # Input array trasnform
                        predict_class = self.death_model.predict(input_array) # Input prediction
                        st.write(f'<div style="text-align: center;"><h2 style="color: #3498db">Classe prevista: {death_classes[argmax(predict_class)]}</h2></div>', unsafe_allow_html=True)
            except ValueError:
                st.warning('Por favor responda todas para realizar a predição')