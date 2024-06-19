import streamlit as st
from os import path
from src.config import Config

class Project:
    """Project section class"""

    def __init__(self):
        self.config = Config()
        self.git_path = self.config.vars.git_png # Blue GitHub logo path
        self.git2_path = self.config.vars.git2_png # Red GitHub logo path

    def project(self):
        """Project section generator function
           return: None
        """
        # Set the project section style
        st.markdown(self.config.project_style, unsafe_allow_html=True)

        # Section title
        st.markdown("<h1 style='text-align: center;'>‎ ‎ ‎ ‎ ‎ ‎ ‎ Equipe do Cirrosifier</h1>", unsafe_allow_html=True)
        
        st.markdown("---")

        # Leaders containers        
        blank1, c1, c2, blank2 = st.columns([2,2,2,2], gap="small")
        leaders_columns_list = [c1, c2]

        for i, column in enumerate(leaders_columns_list):
            key = list(self.config.vars.leaders_links.keys())[i]
            with column:
                st.markdown(f"""
                            <div class='container2'>{key}<br>
                            <a href={self.config.vars.leaders_links[key][0]}><img class='git' src={self.git2_path} style='width:42px;height:42px;' alt='GitHub'></a>
                            <br>
                            {self.config.vars.leaders_links[key][1]}
                            """, unsafe_allow_html=True)

        # Members containers   
        c3, c4, c5, c6, c7 = st.columns([2,2,2,2,2], gap="small")
        members_columns_list = [c3, c4, c5, c6, c7]

        for i, column in enumerate(members_columns_list):
            key = list(self.config.vars.members_links.keys())[i]
            with column:
                st.markdown(f"""
                            <div class='container1'>{key}<br>
                            <a href={self.config.vars.members_links[key]}><img class='git' src={self.git_path} style='width:42px;height:42px;' alt='GitHub'></a>
                            <br>
                            Membro
                            """, unsafe_allow_html=True)

        st.markdown("---")

        # Project section content
        st.header("Sobre a Motivação e o Desenvolvimento")
        st.markdown("""
                    O projeto tem como tema a cirrose pois durante a busca por datasets o Liver Cirrhosis Stage Classification foi o que melhor se encaixou com os nossos requisitos, fazer uma análise de dados (EDA) e a aplicação de modelos de machine learning. Ainda, a cirrose é a doença colestática (em outras palavras, doença que afeta o fígado) mais comum do Brasil, então ficamos interessados em saber como os indicadores da doença se comportam.

                    Para saber mais sobre como o trabalho foi desenvolvido, as tecnologias utilizadas e as conclusões feitas, publicamos um artigo no Medium explicando tudo detalhadamente. O projeto também conta com um repositório no GitHub com a EDA e as aplicações dos modelos de classificação.

                    Este site faz parte de um projeto da TAIL (Technology and Artificial Intelligence League), uma liga estudantil da UFPB (Universidade Federal da Paraíba) formada, como o nome sugere, por amantes da tecnologia e da Inteligência Artificial.
                    """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Project section links
        st.header("Links Importantes")
        c8, c9, c10 = st.columns([2,2,2], gap="small")
        sites_columns_list = [c8, c9, c10]
        
        subtitles = ["Artigo do Medium", "Repositório no GitHub", "Site da TAIL"]

        for i, (logo, link) in enumerate(zip(self.config.vars.sites_logos, self.config.vars.sites_links)):
            logo_path = path.join(self.config.vars.img_dir,logo)
            sites_columns_list[i].image(logo_path)
            sites_columns_list[i].markdown(f"<a href={link}>{subtitles[i]}</a>", unsafe_allow_html=True)