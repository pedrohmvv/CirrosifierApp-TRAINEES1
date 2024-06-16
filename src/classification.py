import streamlit as st
from os import path
import streamlit as st
from streamlit_extras.stylable_container import stylable_container 
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from joblib import load
from numpy import array, argmax

from src.config import Config

config = Config()

def app():
    st.header("Classificação")
    option = st.selectbox(
        "Selecione a Análise",
        ("Estágio", 
         "Situação" ))
    
    st.write("Classificação:", option)

    if (option == "Estágio"):
        st.markdown(
        """
        <style>
            header {
                text-align: center;
            }
            div[data-testid="column"]
            {   
                text-align: center;
                justify-content: center;
            }
            .st-emotion-cache-ubko3j {
                display: none;
            }
        </style>
        """,unsafe_allow_html=True
        )
        st.write(config.input_style, unsafe_allow_html=True)
        st.spinner("Loading your model")
        c1, c2, c3, c4, c5, c6, c7 = st.columns([5, 5, 5, 5, 5, 5, 5], gap="small")
        categoric_labels = [label for label, key in config.vars.stage_labels.items() if key =='text']
        int_labels = [label for label, key in config.vars.stage_labels.items() if key =='int']
        categoric_answers = {'Sim':1, 'Não':0}
        input_array = []
        model_path = path.join(config.vars.models_dir,config.vars.stage_model)
        scaler_path = path.join(config.vars.scalers_dir,config.vars.stage_scaler)
        model = load(model_path)
        scaler = load(scaler_path)

        for i, label in enumerate(config.vars.stage_labels):
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
                    input_array = scaler.transform(input_array)
                    predict_class = model.predict(input_array)
                    st.write(f'<div style="text-align: center;"><h2 style="color: #3498db">Classe prevista: Estágio {argmax(predict_class) + 1}</h2></div>', unsafe_allow_html=True)
        except ValueError:
            st.markdown(
                """
                p {color: black}
                """
            )
            st.warning('Por favor responda todas para realizar a predição')
    
    if (option == "Situação"):
        st.markdown(config.input_style, unsafe_allow_html=True)
        death_classes = {0: 'Morte', 1:'Sobreviveu', 2:'Transplante'}
        st.spinner("Loading your model")
        c1, c2, c3, c4, c5 = st.columns([4, 4, 4, 4, 4])
        categoric_labels = [label for label, key in config.vars.death_labels.items() if key =='text']
        int_labels = [label for label, key in config.vars.death_labels.items() if key =='int']
        labels = [label for label, key in config.vars.death_labels.items() if key =='label']
        categoric_answers = {'Sim':1, 'Não':0}
        input_array = []
        model_path = path.join(config.vars.models_dir,config.vars.death_model)
        scaler_path = path.join(config.vars.scalers_dir,config.vars.death_scaler)
        model = load(model_path)
        scaler = load(scaler_path)

        for i, label in enumerate(config.vars.death_labels):
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
        st.markdown(
        """
        <style>
            
            header {
                text-align: center;
            }
            div[data-testid="column"]
            {
                text-align: center;
                justify-content: center;
            }
            .st-emotion-cache-ubko3j {
                display: none;
            }
        </style>
        """,unsafe_allow_html=True
        )
        try:
            with col2:
                st.write("<br>", unsafe_allow_html=True)
                if st.button('Realizar Predição', key='submit'):
                    input_array = array(input_array).reshape(1, -1)
                    input_array = scaler.transform(input_array)
                    predict_class = model.predict(input_array)
                    st.write(f'<div style="text-align: center;"><h2 style="color: #3498db">Classe prevista: {death_classes[argmax(predict_class)]}</h2></div>', unsafe_allow_html=True)
        except ValueError:
            st.warning('Por favor responda todas para realizar a predição')