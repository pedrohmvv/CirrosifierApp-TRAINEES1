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
    img_dir: str
    project_logo: str
    models_dir: str
    scalers_dir: str
    stage_model: str
    death_model: str
    stage_scaler: str
    death_scaler: str
    death_labels: list
    stage_labels: list


class Config:
    """Basic Config class"""

    def __init__(self):
        """Initialize instance"""

        self.project_dir = abspath(dirname(dirname(__file__)))
        data = {}
        with open(
            join(dirname(abspath(__file__)), 'env.yaml'), encoding = 'utf-8'
        ) as file:
            data = load(file, Loader=SafeLoader)
        self.vars = Variables(
            project_name=data.get('project_name'),
            filename=data.get('filename'),
            data_dir=data.get('data_dir'),
            img_dir=data.get('img_dir'),
            project_logo=data.get('project_logo'),
            models_dir=data.get('models_dir'),
            scalers_dir=data.get('scalers_dir'),
            stage_model=data.get('stage_model'),
            death_model=data.get('death_model'),
            stage_scaler=data.get('stage_scaler'),
            death_scaler=data.get('death_scaler'),
            stage_labels=data.get('stage_labels'),
            death_labels=data.get('death_labels')
        )
        self.button_style ="""
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