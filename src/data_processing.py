#src/data_processing.py
import pandas as pd

def ler_hemogramas(caminho_arquivo):
    return pd.read_csv("C:/Users/User/Desktop/Projeto Health Predictive Model/data/hemograma_pacientes.csv", delimiter=';')
