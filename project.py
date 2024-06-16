import streamlit as st

def app():
    st.header("Equipe do Cirrosifier")
    st.markdown("**fotos, nomes e cargos!!!")

    st.markdown("---")

    st.header("Sobre a Motivação e o Desenvolvimento")
    st.markdown("""
                O projeto tem como tema a cirrose pois durante a busca por datasets o Liver Cirrhosis Stage Classification foi o que melhor se encaixou com os nossos requisitos, fazer uma análise de dados (EDA) e a aplicação de modelos de machine learning. Ainda, a cirrose é a doença colestática (em outras palavras, doença que afeta o fígado) mais comum do Brasil, então ficamos interessados em saber como os indicadores da doença se comportam.

                Para saber mais sobre como o trabalho foi desenvolvido, as tecnologias utilizadas e as conclusões feitas, publicamos um artigo no Medium explicando tudo detalhadamente. O projeto também conta com um repositório no GitHub com a EDA e as aplicações dos modelos de classificação.

                Este site faz parte de um projeto da TAIL (Technology and Artificial Intelligence League), uma liga estudantil da UFPB (Universidade Federal da Paraíba) formada, como o nome sugere, por amantes da tecnologia e da Inteligência Artificial.
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.header("Links Importantes")
    st.markdown("**colocar link pro github e pro medium!!")