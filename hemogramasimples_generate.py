import pandas as pd
import random

def gerar_valores_hemograma():
    return {
        "Paciente": f"Paciente {random.randint(1, 100)}",
        "Hemoglobina": round(random.uniform(12.0, 16.0), 1),  # g/dL
        "Hematocrito": round(random.uniform(37.0, 47.0), 1),  # %
        "Leucócitos": random.randint(4000, 11000),            # /µL
        "Plaquetas": random.randint(150000, 450000),          # /µL
        "Glicemia": random.randint(70, 140),                  # mg/dL
        "HbA1c": round(random.uniform(4.0, 6.5), 1),          # %
        "Colesterol Total": random.randint(150, 240),         # mg/dL
        "LDL": random.randint(80, 160),                       # mg/dL
        "HDL": random.randint(40, 100),                       # mg/dL
        "Triglicerídeos": random.randint(50, 200),            # mg/dL
        "ALT": random.randint(7, 56),                         # U/L
        "AST": random.randint(5, 40)                          # U/L
    }

# Gerar hemogramas para 2 pacientes
pacientes = [gerar_valores_hemograma() for _ in range(2)]

# Converter para DataFrame
df = pd.DataFrame(pacientes)

# Salvar em CSV
df.to_csv("hemograma_pacientes.csv", sep=';', index=False)

print("Hemograma gerado com sucesso:")
print(df)
