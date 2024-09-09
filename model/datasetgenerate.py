import pandas as pd
import numpy as np

# Definir o número de pacientes
num_pacientes = 1000

# Gerar dados sintéticos dentro das faixas reais
dados = {
    "Paciente": [f"Paciente_{i}" for i in range(1, num_pacientes + 1)],
    "Hemoglobina": np.random.uniform(12.0, 17.5, num_pacientes),
    "Hematócrito": np.random.uniform(36, 50, num_pacientes),
    "Leucócitos": np.random.uniform(2000, 30000, num_pacientes),  # Leucócitos com faixa maior
    "Plaquetas": np.random.uniform(100000, 450000, num_pacientes),  # Plaquetas com faixa maior
    "VCM": np.random.uniform(80, 100, num_pacientes),
    "HCM": np.random.uniform(27, 31, num_pacientes),
    "CHCM": np.random.uniform(32, 36, num_pacientes),
    "Linfócitos": np.random.uniform(1500, 4000, num_pacientes),
    "Neutrófilos": np.random.uniform(2500, 7500, num_pacientes),
    "Monócitos": np.random.uniform(200, 800, num_pacientes),
    "Glicemia": np.random.uniform(70, 126, num_pacientes),
    "HbA1c": np.random.uniform(5.0, 6.5, num_pacientes),
    "Colesterol Total": np.random.uniform(150, 240, num_pacientes),
    "LDL": np.random.uniform(70, 190, num_pacientes),
    "HDL": np.random.uniform(30, 70, num_pacientes),
    "Triglicerídeos": np.random.uniform(100, 300, num_pacientes),
    "ALT": np.random.uniform(7, 56, num_pacientes),
    "AST": np.random.uniform(10, 40, num_pacientes)
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Definir condições para risco de leucemia
def definir_risco_leucemia(linha):
    leucocitos = linha["Leucócitos"]
    plaquetas = linha["Plaquetas"]
    hemoglobina = linha["Hemoglobina"]

    # Definir risco de leucemia com base em valores anormais
    if leucocitos > 20000 or leucocitos < 3000:  # Leucócitos muito altos ou muito baixos
        return 1  # Risco alto
    elif plaquetas < 100000:  # Plaquetas muito baixas
        return 1
    elif hemoglobina < 10.0:  # Hemoglobina muito baixa
        return 1
    else:
        return 0  # Sem risco

# Aplicar a função ao DataFrame
df["Risco_Leucemia"] = df.apply(definir_risco_leucemia, axis=1)

# Salvar CSV
df.to_csv("hemogramas_completos_sinteticos_com_risco2.csv", index=False)

print("Dados sintéticos de hemogramas completos com risco de leucemia gerados!")
