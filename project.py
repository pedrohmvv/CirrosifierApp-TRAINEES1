import streamlit as st

def app():
    st.markdown(
    """
    <style>
        header {
            text-align: center;
        }
        div[data-testid="column"]
        {
            text-align: center;
        }
        .container1 {
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .container2 {
            border: 2px solid #a60d4e;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 20px;
        }
    </style>
    """,unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>‎ ‎ ‎ ‎ ‎ ‎ ‎ Equipe do Cirrosifier</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    blank1, c1, c2, blank2 = st.columns([2,2,2,2], gap="small")
    with c1:
        st.markdown("""
                    <div class='container2'>Davi Ribeiro<br>
                    <a href='https://github.com/davirpp'><img src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git2.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Diretor
                    """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
                    <div class='container2'>Rodrigo Veríssimo<br>
                    <a href='https://github.com/rodrigo0567'><img src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git2.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Líder
                    """, unsafe_allow_html=True)
    
    c3, c4, c5, c6, c7 = st.columns([2,2,2,2,2], gap="small")
    with c3:
        st.markdown("""
                    <div class='container1'>Gabriele Targino<br>
                    <a href='https://github.com/gabitargino'><img src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/1cafc56d47f1d9e64af41138165180e5fdf12744/img/git.svg' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
                    <div class='container1'>Joyce Ribeiro<br>
                    <a href='https://github.com/Joyce-Ribeiro'><img src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/1cafc56d47f1d9e64af41138165180e5fdf12744/img/git.svg' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)
    with c5:
        st.markdown("""
                    <div class='container1'>Luis Henrique<br>
                    <a href='https://github.com/luyluish'><img src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/1cafc56d47f1d9e64af41138165180e5fdf12744/img/git.svg' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)
    with c6:
        st.markdown("""
                    <div class='container1'>Pedro Henrique<br>
                    <a href='https://github.com/ricktherunner'><img src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/1cafc56d47f1d9e64af41138165180e5fdf12744/img/git.svg' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)
    with c7:
        st.markdown("""
                    <div class='container1'>Rafael Henrique<br>
                    <a href='https://github.com/rafaelhenrique-ra'><img src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/1cafc56d47f1d9e64af41138165180e5fdf12744/img/git.svg' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)

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