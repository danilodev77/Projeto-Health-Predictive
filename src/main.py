from data_processing import ler_hemogramas
from analysis import comparar_com_indices_normais
from diagnosis import gerar_diagnostico, detectar_diabetes, detectar_doencas_cardiacas, detectar_disfuncao_hepatica
import pyttsx3


def falar_texto(texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(texto)
    engine.runAndWait()


def main():
    # Ler os hemogramas
    hemogramas = ler_hemogramas("C:/Users/User/Desktop/Projeto Health Predictive Model/data/hemograma_pacientes.csv")


    #Exibir as colunas disponíveis
    print("Colunas disponíveis:", hemogramas.columns)


    # Iterar sobre cada hemograma
    for index, hemograma in hemogramas.iterrows():
        # Comparar com os índices normais
        resultados = comparar_com_indices_normais(hemograma)

        # Gerar diagnóstico
        diagnostico = gerar_diagnostico(resultados)

         # Detectar diabetes
        diabetes_risco = detectar_diabetes(resultados)
        
        # Detectar doenças cardíacas
        cardiacas_risco = detectar_doencas_cardiacas(resultados)
        
        # Detectar disfunção hepática
        hepatica_risco = detectar_disfuncao_hepatica(resultados)

                # Exibir Resultados
        print(f"{hemograma['Paciente']}")
        falar_texto(f"{hemograma['Paciente']}")

        print(f"Resultados: {resultados}")
        falar_texto(f"Resultados: {resultados}")

        print(f"Diagnóstico: {diagnostico}")
        falar_texto(f"Diagnóstico: {diagnostico}")

        print(f"Risco de Diabetes: {diabetes_risco}")
        falar_texto(f"Risco de Diabetes: {diabetes_risco}")

        print(f"Risco de Doenças Cardíacas: {cardiacas_risco}")
        falar_texto(f"Risco de Doenças Cardíacas: {cardiacas_risco}")

        print(f"Risco de Disfunção Hepática: {hepatica_risco}")
        falar_texto(f"Risco de Disfunção Hepática: {hepatica_risco}")

        
        print("-" * 30)

if __name__ == "__main__":
    main()
