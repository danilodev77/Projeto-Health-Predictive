def gerar_diagnostico(resultados):
    diagnostico = []
    if resultados['Hemoglobina'] == "Baixo":
        diagnostico.append("Anemia")
        diagnostico.append("Recomendar Suplementação de Ferro")
    if resultados['Leucócitos'] == "Alto":
        diagnostico.append("Possível Infecção")
        diagnostico.append("Recomendar antibiótico e Exame Adicional")

    if not diagnostico:
        diagnostico.append("Resultados Normais")

    return diagnostico

def detectar_diabetes(resultados):
    if 'Glicemia' in resultados and resultados['Glicemia']['valor'] > 126:
        return "Alto risco de Diabetes"
    elif 'HbA1c' in resultados and resultados['HbA1c']['valor'] >= 6.5:
        return "Alto risco de Diabetes"
    else:
        return "Sem risco aparente de Diabetes"


def detectar_doencas_cardiacas(resultados):
    riscos = []
    if 'LDL' in resultados and resultados['LDL']['valor'] > 160:
        riscos.append("Alto LDL - Risco de Doenças Cardíacas")
    if 'HDL' in resultados and resultados['HDL']['valor'] < 40:
        riscos.append("Baixo HDL - Risco de Doenças Cardíacas")
    if 'Triglicerídeos' in resultados and resultados['Triglicerídeos']['valor'] > 200:
        riscos.append("Alto Triglicerídeos - Risco de Doenças Cardíacas")

    return riscos if riscos else ["Sem risco aparente de Doenças Cardíacas"]


def detectar_disfuncao_hepatica(resultados):
    riscos = []
    if 'ALT' in resultados and resultados['ALT']['valor'] > 40:
        riscos.append("ALT elevada - Risco de Disfunção Hepática")
    if 'AST' in resultados and resultados['AST']['valor'] > 40:
        riscos.append("AST elevada - Risco de Disfunção Hepática")

    return riscos if riscos else ["Sem risco aparente de Disfunção Hepática"]

