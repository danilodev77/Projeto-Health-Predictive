def comparar_com_indices_normais(hemograma):
    indices_normais = {
        "Hemoglobina": (12.0, 16.0),
        "Hematocrito": (37.0, 47.0),
        "Leucócitos": (4000, 11000),
        "Plaquetas": (150000, 450000),
        "Glicemia": (70, 100),                # mg/dL
        "HbA1c": (4.0, 5.6),                  # %
        "Colesterol Total": (150, 200),       # mg/dL
        "LDL": (80, 160),                     # mg/dL
        "HDL": (40, 100),                     # mg/dL
        "Triglicerídeos": (50, 150),          # mg/dL
        "ALT": (7, 56),                       # U/L
        "AST": (5, 40)                        # U/L
    }

    resultados = {}
    for exame, valor in hemograma.items():
        if exame in indices_normais:
            min_val, max_val = indices_normais[exame]
            if valor < min_val:
                resultados[exame] = {"Classificação": "Baixo", "valor": valor}
            elif valor > max_val:
                resultados[exame] = {"Classificação": "Alto", "valor": valor}
            else:
                resultados[exame] = {"Classificação": "Normal", "valor": valor}
    return resultados
