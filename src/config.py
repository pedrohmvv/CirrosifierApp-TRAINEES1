from dataclasses import dataclass
from yaml import load
from yaml.loader import SafeLoader
from os.path import join, dirname, abspath

@dataclass
class Variables:
    """Store config data class"""

    project_name: str
    filename: str
    data_dir: str
    data_csv: str
    img_dir: str
    project_logo: str
    sites_logos: list
    sites_links: list
    logo_gif: str
    linhas_gif: str
    git_png: str
    git2_png: str
    leaders_links: dict
    members_links: dict
    models_dir: str
    scalers_dir: str
    stage_model: str
    death_model: str
    stage_scaler: str
    death_scaler: str
    death_labels: dict
    stage_labels: dict


class Config:
    """Basic Config class"""

    def __init__(self):
        """Initialize instance"""

        self.project_dir = abspath(dirname(dirname(__file__)))
        data = {}
        with open(join(dirname(abspath(__file__)), 'env.yaml'), encoding='utf-8') as file:
            data = load(file, Loader=SafeLoader)
        self.vars = Variables(
            project_name=data.get('project_name'),
            filename=data.get('filename'),
            data_dir=data.get('data_dir'),
            data_csv=data.get('data_csv'),
            img_dir=data.get('img_dir'),
            project_logo=data.get('project_logo'),
            sites_logos=data.get('sites_logos'),
            sites_links=data.get('sites_links'),
            logo_gif=data.get('logo_gif'),
            git_png=data.get('git_png'),
            git2_png=data.get('git2_png'),
            linhas_gif=data.get('linhas_gif'),
            leaders_links=data.get('leaders_links'),
            members_links=data.get('members_links'),
            models_dir=data.get('models_dir'),
            scalers_dir=data.get('scalers_dir'),
            stage_model=data.get('stage_model'),
            death_model=data.get('death_model'),
            stage_scaler=data.get('stage_scaler'),
            death_scaler=data.get('death_scaler'),
            stage_labels=data.get('stage_labels'),
            death_labels=data.get('death_labels')
        )

        self.button_style = """
                            <style>
                            .stButton > button {
                                background-color: #b02238; /* Cor de fundo */
                                color: white; /* Cor do texto */
                                padding: 10px 20px; /* Ajuste o padding conforme necessário */
                                border: none; /* Remove a borda do botão */
                                cursor: pointer; /* Muda o cursor ao passar por cima */
                                display: inline-block; /* Permite centralizar usando text-align */
                                margin: auto; /* Centraliza horizontalmente */
                            }
                            .stButton > button:hover {
                                background-color: #6d0019; /* Cor de fundo ao passar o mouse */
                            }
                            </style>
                            """
        
        self.input_style = """
                            <style>
                            .stSelectbox > div, .stNumberInput > div {
                                width: 100% !important;
                            }
                            .stSelectbox label, .stNumberInput label {  
                                white-space: nowrap !important;
                                overflow: visible; /* Garante que o conteúdo visível não seja cortado */
                                text-overflow: ellipsis;
                                display: block;
                                color: white;
                            }
                            </style>
                            """
        
        self.classification_style = """
                                    <style>
                                        header {
                                            text-align: center;
                                        }
                                        div[data-testid="column"] {   
                                            text-align: center;
                                            justify-content: center;
                                        }
                                        .st-emotion-cache-ubko3j {
                                            display: none;
                                        }
                                    </style>
                                    """
        
        self.home_style = """
                            <style>
                                div[data-testid="column"]:nth-of-type(2) {
                                    display: flex;
                                    justify-content: center;
                                    text-align: left;
                                }
                                div[data-testid="column"]:nth-of-type(1),
                                div[data-testid="column"]:nth-of-type(3),
                                div[data-testid="column"]:nth-of-type(4) {
                                    display: flex;
                                    justify-content: center;
                                }
                                .container {
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;
                                }
                                img {
                                    max-width: 100%;
                                    max-height: 100%;
                                }
                                .text {
                                    font-size: 20px;
                                    padding-left: 20px;
                                }
                            </style>
                            """

        self.project_style = """
                            <style>
                                header {
                                    text-align: center;
                                }
                                div[data-testid="column"] {
                                    text-align: center;
                                    justify-content: center;
                                }
                                [data-testid="column"] [data-testid=stImage] {
                                    text-align: center;
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;
                                    margin-left: auto;
                                    margin-right: auto;
                                    width: 100%;
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
                                .git:hover {
                                    border: 1px solid white;
                                    border-radius: 30px;
                                    box-shadow: 0 0 2px rgba(255,255,255, 0.6);
                                }
                            </style>
                            """
        
        self.main_style = """
                            <style>
                                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');
                                html {
                                    font-family: "Inter";
                                }
                                .block-container {
                                    padding-top: 4rem;
                                }
                                .sidebar .sidebar-content {
                                    display: flex;
                                    flex-direction: column;
                                    align-items: center;
                                }
                                [data-testid=stSidebar] [data-testid=stImage] {
                                    text-align: center;
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;
                                    margin-left: auto;
                                    margin-right: auto;
                                    width: 100%;
                                }
                                .stImage {
                                    border-radius: 3px;
                                    box-shadow: 0 0 2px rgba(255,255,255, 0.6);
                                }
                                .st-emotion-cache-ubko3j {
                                    display: none;
                                }
                                .container {
                                    display: flex;
                                    align-items: center;
                                    justify-content: center;
                                }
                            </style>
                            """
