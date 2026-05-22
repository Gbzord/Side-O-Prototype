import numpy as np
import pandas as pd

def gerar_dataset_calibrado(nome_arquivo="sensor_gas_dataset.csv"):
    np.random.seed(42) # Semente fixa para reprodutibilidade
    
    tamanho_total = 1000
    tempo = np.linspace(0, 100, tamanho_total)
    
    # FASE 1: Operação Normal (Ruído Estocástico -> Alta Entropia, Baixa Complexidade)
    # Simula o vento, ondas e vibração natural da plataforma offshore
    fase_normal = np.random.normal(loc=0.5, scale=0.1, size=600)
    
    # FASE 2: Transição e Vazamento Crítico (Sinal Determinístico -> Quebra de Simetria)
    # Simula a pluma de gás alterando a dinâmica do sensor
    fase_anomalia = np.random.normal(loc=0.5, scale=0.1, size=400) + np.sin(np.linspace(0, 20, 400)) * 0.4
    
    # Concatena o sinal
    sinal_completo = np.concatenate([fase_normal, fase_anomalia])
    
    # Cria o DataFrame e exporta
    df = pd.DataFrame({
        "Tempo_segundos": tempo,
        "Concentracao_CH4_ppm": sinal_completo
    })
    
    df.to_csv(nome_arquivo, index=False)
    print(f"✅ {nome_arquivo} gerado com sucesso! Transição de fase injetada no ponto T600.")

if __name__ == "__main__":
    gerar_dataset_calibrado()