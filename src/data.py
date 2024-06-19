import streamlit as st
from os import path
from streamlit_echarts import st_echarts
from pandas import read_csv

from src.config import Config

class Data:
    """Data section class"""

    def __init__(self):
        self.config = Config()
        self.data_path = path.join(self.config.vars.data_dir, self.config.vars.data_csv) # CSV data file path
        self.df_cirrose = read_csv(self.data_path) # Load the cirrhosis dataset

    def stage_means(self, column: str) -> object:
        """Calculate the mean of a column by stage
           column: str - column name
           return: DataFrame
        """
        return self.df_cirrose.groupby('Estágio')[column].mean().tolist()

    def data(self) -> None:
        """Data visualization section geneator function
           return: None
        """

        # Selection Menu
        option = st.selectbox(
            "Selecione o Gráfico",
            ("Bilirrubina", 
            "Expectativa de Vida",
            "Mortalidade por Estágio",
            "Mortalidade por Sexo")
        )

        if option == "Bilirrubina":
            # Calculate the average bilirubin for each stage
            albValues = self.stage_means('Bilirrubina(mg/dl)')
            stages = ["Estágio 1", "Estágio 2", "Estágio 3"]

            # chart configuration
            option_bilirrubina = {
                "xAxis": {
                    "type": "category",
                    "data": stages,
                    "axisLabel": {
                        "color": "#ffffff"  # X axis text color
                    },
                    "nameTextStyle": {
                        "color": "#ffffff"  # X axis name color
                    }
                },
                "yAxis": {
                    "type": "value",
                    "min": 0,
                    "max": 5,
                    "axisLabel": {
                        "color": "#ffffff"  # Y axis text color
                    },
                    "nameTextStyle": {
                        "color": "#ffffff"  # Y axis name color
                    }
                },
                "series": [
                    {
                        "name": "Média de Bilirrubina (mg/dl)",
                        "data": albValues,
                        "type": "bar",
                        "itemStyle": {
                            "color": "#d94c21"  # Green color for "Média de Bilirrubina (mg/dl)"
                        }
                    },
                ],
                "legend": {"data": ["Média de Bilirrubina (mg/dl)"],
                        "textStyle": {
                                "color": 'white'
                            }},
                "backgroundColor": "rgb(14, 17, 23)"
            }

            # Plot chart
            st.title("Qtd. Média de Bilirrubina em Cada Estágio da Cirrose")
            st_echarts(options=option_bilirrubina, height="600px")

        if option == "Expectativa de Vida":
            # Calculate the average death time for each stage
            deathTime1 = self.df_cirrose.loc[(self.df_cirrose['Situação'] == 'Morte') & (self.df_cirrose['Estágio'] == 1), 'Numero_dias'].mean()
            deathTime2 = self.df_cirrose.loc[(self.df_cirrose['Situação'] == 'Morte') & (self.df_cirrose['Estágio'] == 2), 'Numero_dias'].mean()
            deathTime3 = self.df_cirrose.loc[(self.df_cirrose['Situação'] == 'Morte') & (self.df_cirrose['Estágio'] == 3), 'Numero_dias'].mean()

            # Chart configuration
            option_tempo_morte = {
                "xAxis": {
                    "type": "category",
                    "data": ["Estágio 1", "Estágio 2", "Estágio 3"],
                    "axisLabel": {
                        "color": "#ffffff"  # X axis text color
                    },
                    "nameTextStyle": {
                        "color": "#ffffff"  # X axis name color
                    }
                },
                "yAxis": {
                    "type": "value",
                    "axisLabel": {
                        "color": "#ffffff"  #  X axis text color
                    },
                    "nameTextStyle": {
                        "color": "#ffffff"  # X axis name color
                    }
                },
                "series": [
                    {
                        "name": "Tempo médio de morte (dias)",
                        "data": [deathTime1, deathTime2, deathTime3],
                        "type": "bar",
                        "itemStyle": {
                            "color": "#b02238"  # Red color for "tempo médio de morte"
                        }
                    },
                ],

                "legend": {"data": ["Tempo médio de morte (dias)"],
                        "textStyle": {
                                "color": 'white'
                                },
                            },
                "backgroundColor": "rgb(14, 17, 23)"
            }

            # Plot chart
            st.title("Tempo Médio para Morte em Cada Estágio da Cirrose")
            st_echarts(options=option_tempo_morte, height="600px")

        if option == "Mortalidade por Estágio":
            # Deaths for stage
            df_filtrado = self.df_cirrose[self.df_cirrose['Situação'] != 'Transplante']
            contagem_por_estagio = df_filtrado.groupby(['Estágio', 'Situação']).size().unstack()

            # Chart configuration
            option_estagio = {
                "xAxis": {
                    "type": "category",
                    "data": contagem_por_estagio.index.tolist(),
                    "axisLabel": {
                        "color": "#ffffff"  # X axis text color
                    },
                    "nameTextStyle": {
                        "color": "#ffffff"  # X axis name color
                    }
                },
                "backgroundColor": "rgb(14, 17, 23)",
                "yAxis": {
                    "type": "value",
                    "axisLabel": {
                        "color": "#ffffff"  # X axis text color
                    },
                    "nameTextStyle": {
                        "color": "#ffffff"  # X axis name color
                    }
                },
                "series": [
                    {
                        "name": "Morte",
                        "data": contagem_por_estagio['Morte'].tolist(),
                        "type": "bar",
                        "itemStyle": {
                            "color": "#b02238"  # Red color for "Morte"
                        }
                    },
                    {
                        "name": "Sobreviveu",
                        "data": contagem_por_estagio['Sobreviveu'].tolist(),
                        "type": "bar",
                        "itemStyle": {
                            "color": "#4682B4"  # Blue color for "Sobreviveu"
                        }
                    },
                ],
                "legend": {"data": ["Morte", "Sobreviveu"],
                        "textStyle": {
                                "color": 'white'
                                },
                            }
            }

            # Plot chart
            st.title("Distribuição de Sobreviventes e Óbitos por Estágio da Cirrose")
            st_echarts(options=option_estagio, height="600px")

        if option == "Mortalidade por Sexo":
            # Deaths for Gender considering 'Transplante' as 'Sobreviveu'
            self.df_cirrose['Situação'] = self.df_cirrose['Situação'].replace('Transplante', 'Sobreviveu')

            # Grouping the dataset
            contagem_por_sexo = self.df_cirrose.groupby(['Sexo', 'Situação']).size().unstack()

            # Chart configuration
            option_sexo = {
                "xAxis": {
                    "type": "category",
                    "data": contagem_por_sexo.index.tolist(),
                    "axisLabel": {
                        "color": "#ffffff"  # X axis text color
                    },
                    "nameTextStyle": {
                        "color": "#ffffff"  # X axis name color
                    }
                },
                "yAxis": {
                    "type": "value",
                    "axisLabel": {
                        "color": "#ffffff"  # Y axis text color
                    },
                    "nameTextStyle": {
                        "color": "#ffffff"  # Y axis name color
                    }
                },
                "series": [
                    {
                        "name": "Mortos",
                        "data": contagem_por_sexo['Morte'].tolist(),
                        "type": "bar",
                        "itemStyle": {
                            "color": "#b02238"  # Red color for "Mortos"
                        }
                    },
                    {
                        "name": "Sobreviventes/Transplantados",
                        "data": contagem_por_sexo['Sobreviveu'].tolist(),
                        "type": "bar",
                        "itemStyle": {
                            "color": "#4682B4"  # Blue color for "Sobreviventes/Transplantados"
                        }
                    },
                ],
                "legend": {"data": ["Mortos", "Sobreviventes/Transplantados"],
                        "textStyle": {
                                "color": 'white'
                                },
                                },
                "backgroundColor": "rgb(14, 17, 23)",
            }

            # Plot chart
            st.title("Quantidade de Mortos e Sobreviventes/Transplantados por Sexo")
            st_echarts(options=option_sexo, height="600px")
