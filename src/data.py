import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_option_menu import option_menu
import pandas as pd

def stage_means(column):
    # Função para calcular a média por estágio
    df_cirrose = pd.read_csv('data/liver_cirrhosis_v1.csv')
    return df_cirrose.groupby('Estágio')[column].mean().tolist()

def app():
    # Carregamento do arquivo CSV (substitua pelo seu caminho e nome de arquivo)
    df_cirrose = pd.read_csv('data/liver_cirrhosis_v1.csv')

    # Menu de seleção
    option = option_menu(
        "Selecione o Gráfico",
        ("Bilirrubina", 
         "Expectativa de Vida",
         "Mortalidade por Estágio",
         "Mortalidade por Sexo")
    )

    if option == "Bilirrubina":
        # Configuração do gráfico ECharts para média de bilirrubina por estágio
        albValues = stage_means('Bilirrubina(mg/dl)')
        stages = ["Estágio 1", "Estágio 2", "Estágio 3"]

        option_bilirrubina = {
            "xAxis": {
                "type": "category",
                "data": stages,
            },
            "yAxis": {
                "type": "value",
                "min": "0",
                "max": "5"
            },
            "series": [
                {
                    "name": "Média de Bilirrubina (mg/dl)",
                    "data": albValues,
                    "type": "bar",
                    "itemStyle": {
                        "color": "#3CB371"  # Green color for "Média de Bilirrubina (mg/dl)"
                    }
                },
            ],
            "legend": {"data": ["Média de Bilirrubina (mg/dl)"]},
        }

        # Exibindo o gráfico ECharts de média de bilirrubina por estágio
        st.title("Qtd. Média de Bilirrubina em Cada Estágio da Cirrose")
        st_echarts(options=option_bilirrubina, height="600px")

    elif option == "Expectativa de Vida":
        # Calcular tempo médio para morte em cada estágio
        deathTime1 = df_cirrose.loc[(df_cirrose['Situação'] == 'Morte') & (df_cirrose['Estágio'] == 1), 'Numero_dias'].mean()
        deathTime2 = df_cirrose.loc[(df_cirrose['Situação'] == 'Morte') & (df_cirrose['Estágio'] == 2), 'Numero_dias'].mean()
        deathTime3 = df_cirrose.loc[(df_cirrose['Situação'] == 'Morte') & (df_cirrose['Estágio'] == 3), 'Numero_dias'].mean()

        # Configuração do gráfico ECharts para tempo médio de morte por estágio
        option_tempo_morte = {
            "xAxis": {
                "type": "category",
                "data": ["Estágio 1", "Estágio 2", "Estágio 3"],
            },
            "yAxis": {"type": "value"},
            "series": [
                {
                    "name": "Tempo médio de morte (dias)",
                    "data": [deathTime1, deathTime2, deathTime3],
                    "type": "bar",
                    "itemStyle": {
                        "color": "#b02238"  # Red color for tempo médio de morte
                    }
                },
            ],
            "legend": {"data": ["Tempo médio de morte (dias)"]},
        }

        # Exibindo o gráfico ECharts de tempo médio de morte por estágio
        st.title("Tempo Médio para Morte em Cada Estágio da Cirrose")
        st_echarts(options=option_tempo_morte, height="600px")

    elif option == "Mortalidade por Estágio":
        # Configuração do gráfico ECharts para contagem por Estágio e Situação
        df_filtrado = df_cirrose[df_cirrose['Situação'] != 'Transplante']
        contagem_por_estagio = df_filtrado.groupby(['Estágio', 'Situação']).size().unstack()

        option_estagio = {
            "xAxis": {
                "type": "category",
                "data": contagem_por_estagio.index.tolist(),
            },
            "yAxis": {"type": "value"},
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
            "legend": {"data": ["Morte", "Sobreviveu"]},
        }

        # Exibindo o gráfico ECharts de contagem por Estágio e Situação
        st.title("Distribuição de Sobreviventes e Óbitos por Estágio da Cirrose")
        st_echarts(options=option_estagio, height="600px")

    elif option == "Mortalidade por Sexo":
        # Considerando o valor de "Transplante" como "Sobreviveu"
        df_cirrose['Situação'] = df_cirrose['Situação'].replace('Transplante', 'Sobreviveu')

        # Filtrando e agrupando o DataFrame para contagem por Sexo e Situação
        contagem_por_sexo = df_cirrose.groupby(['Sexo', 'Situação']).size().unstack()

        # Configuração do gráfico ECharts para contagem por Sexo e Situação
        option_sexo = {
            "xAxis": {
                "type": "category",
                "data": contagem_por_sexo.index.tolist(),
            },
            "yAxis": {"type": "value"},
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
            "legend": {"data": ["Mortos", "Sobreviventes/Transplantados"]},
        }

        # Exibindo o gráfico ECharts de contagem por Sexo e Situação
        st.title("Quantidade de Mortos e Sobreviventes/Transplantados por Sexo")
        st_echarts(options=option_sexo, height="600px")

# Executando o aplicativo
if __name__ == "__main__":
    app()
