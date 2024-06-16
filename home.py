import streamlit as st

def app():
    st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(2)
        {
            text-align: left;
        }
        div[data-testid="column"]:nth-of-type(1)
        {
            display: flex;
            justify-content: flex-end;
        }
        div[data-testid="column"]:nth-of-type(3)
        {
            display: flex;
            justify-content: flex-start;
        }
        div[data-testid="column"]:nth-of-type(4)
        {
            display: flex;
            justify-content: flex-start;
        }
    </style>
    """,unsafe_allow_html=True
)
    # Dividir em duas células, a logo e o titulo
    c1, c2 = st.columns([2,2], gap="small")
    with c1:
        st.image("img/spinning_logo.gif")
    with c2:
        st.title("CIRROSIFIER")
        st.header("Classificando a Cirrose")
        st.markdown("Um projeto por Trainees 1")
        st.markdown("Rotação 2024.1")

    st.markdown("---")

    st.header("Bem Vindo!")
    st.markdown("""
                O Cirrosfier é um projeto que integra Inteligência Artificial, Ciência de Dados e Saúde. Focado na Cirrose Biliar Primária (CBP), o Cirrosfier contém análise de dados e aplicação de modelos de classificação a fim de “prever” a possível situação (sobrevivente, morte ou transplante) e o possível estágio (1, 2, ou 3) do paciente.
                
                Neste site, ao informar alguns dados de taxas e a presença ou não de fatores agravantes, você poderá simular a situação e o estágio do paciente cirrótico. O modelo que fará as classificações durante a simulação será o Light Gradient-Boosting Machine (LGBM), pois ao longo do projeto desenvolvido foi o que apresentou a melhor precisão dos resultados. Vale ressaltar que o dataset usado para o treino e o teste do modelo foi o Liver Cirrhosis Stage Classification. 
                """, unsafe_allow_html=True)
    
    st.markdown("---")

    st.header("Navegação")
    st.markdown("Clique nos botões da barra lateral para navegar pelo site:")
    st.markdown("""
                * <strong>Home:</strong> Onde você se encontra!
                * <strong>Projeto:</strong> Aqui você verá mais informações sobre o nosso projeto
                * <strong>Dados:</strong> Aqui você verá alguns gráficos gerados durante a análise do dataset e da aplicação dos modelos de machine learning.
                * <strong>Classificação:</strong> Aqui você poderá fazer uma simulação para descobrir a previsão da situação e do estágio do paciente.
                """, unsafe_allow_html=True)
    c3, c4, c5 = st.columns([1, 1, 1], gap="small")
    
    with c4:
        st.image("img/linhas2t.gif")