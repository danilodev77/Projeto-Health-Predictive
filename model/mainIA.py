import pandas as pd

# Carregar os dados
data = pd.read_csv("C:/Users/User/Desktop/Projeto Health Predictive Model/data/hemogramas_completos_sinteticos_com_risco2.csv")


# Exibir os nomes das colunas
print(data.columns)


from data_analises import preprocess_data
from model import train_model, evaluate_model

# Carregar e processar os dados
X_train, X_test, y_train, y_test = preprocess_data()

# Treinar o modelo
model = train_model(X_train, y_train)

# Avaliar o modelo
evaluate_model(model, X_test, y_test)
