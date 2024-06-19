import streamlit as st
from os import path
from src.config import Config

class Home:
    """Home section class"""

    def __init__(self):
        self.config = Config()
        self.logo_gif_path = self.config.vars.logo_gif # Logo gif path
        self.linhas_gif_path = self.config.vars.linhas_gif # Lines gif path

    def home(self):
        """Home section generator function
           return: None
        """

        # Set the home section style
        st.markdown(self.config.home_style, unsafe_allow_html=True)
        
        # Home container
        st.markdown(f"""
                    <div class='container'>
                        <img src={self.logo_gif_path} style='width:200px;height:200px;' alt='GitHub'>
                            <div class='text'>
                                <h1>{self.config.vars.project_name}</h1>
                                <h2>Classificando a Cirrose</h2>
                                <h3>Um projeto por Trainees 1<br>TAIL - 2024.1</h3>
                            </div>
                    </div>
                    """
                    , unsafe_allow_html=True)

        st.markdown("---")

        # Home content
        st.header("Bem Vindo!")
        st.markdown(f"""
                    Você já tinha pensado em juntar **Cirrose**, **Inteligência Artificial** e **Análise de Dados**? Ainda não? 
                    Agora, para te ajudar a visualizar melhor esse cenário temos o *<strong>{self.config.vars.project_name}</strong>*, um projeto que integra essas três áreas. Focado na Cirrose Biliar Primária (CBP), o Cirrosfier contém análise de dados e aplicação de modelos de classificação a fim de “prever” a possível situação (sobrevivente, morte ou transplante) e o possível estágio (1, 2, ou 3) do paciente.
                    
                    Neste site, ao informar alguns dados de taxas e a presença ou não de fatores agravantes, você poderá simular a situação e o estágio de um paciente. O modelo que fará as classificações durante a simulação será o <u>Light Gradient-Boosting Machine (LGBM)</u>, pois ao longo do projeto desenvolvido foi o que apresentou a melhor precisão dos resultados. Vale ressaltar que o dataset usado para o treino e o teste do modelo foi o *Liver Cirrhosis Stage Classification* disponível no Kaggle. 

                    """, unsafe_allow_html=True)
        
        st.markdown("---")

        # Navigation
        st.header("Navegação")
        st.markdown("Clique nos botões da barra lateral para navegar pelo site:")
        st.markdown("""
                    * <strong>Home:</strong> Onde você se encontra!
                    * <strong>Projeto:</strong> Aqui você verá mais informações sobre o nosso projeto
                    * <strong>Dados:</strong> Aqui você verá alguns gráficos gerados durante a análise do dataset e da aplicação dos modelos de machine learning.
                    * <strong>Classificação:</strong> Aqui você poderá fazer uma simulação para descobrir a previsão da situação e do estágio do paciente.
                    """, unsafe_allow_html=True)
        st.markdown(f"<div class='container'><img src={self.linhas_gif_path} alt='GitHub'></div>", unsafe_allow_html=True)