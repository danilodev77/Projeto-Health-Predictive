import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data():
    # Carregar dados (dataset)
    data = pd.read_csv("C:/Users/User/Desktop/Projeto Health Predictive Model/data/hemogramas_completos_sinteticos_com_risco2.csv")
    
    # Remover a coluna 'Paciente'
    data = data.drop(columns=['Paciente'])
    
    # Separar features e rótulo
    X = data.drop(columns=['Risco_Leucemia'])
    y = data['Risco_Leucemia']
    
    # Dividir em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Normalizar os dados
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test

