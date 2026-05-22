import numpy as np
import pandas as pd
import ordpy

def calcular_metricas_hc(sinal, dx=3):
    """
    Calcula a Entropia de Permutação (H) e Complexidade Estatística (C) 
    utilizando a abstração de Bandt-Pompe para séries temporais.
    """
    # A função complexity_entropy calcula ambas as métricas de forma otimizada
    # retornando uma tupla: (Entropia_normalizada, Complexidade_estatística)
    h, c = ordpy.complexity_entropy(sinal, dx=dx)
    return h, c

def processar_janelas_deslizantes(sinal, tamanho_janela=100, passo=20):
    """
    Aplica uma janela deslizante (Sliding Window) sobre a série temporal 
    para rastrear a evolução da dinâmica do ativo ao longo do tempo.
    """
    resultados = []
    # Garante que o sinal seja um array numpy unidimensional
    sinal_array = np.asarray(sinal).flatten()
    
    for i in range(0, len(sinal_array) - tamanho_janela, passo):
        sub_sinal = sinal_array[i : i + tamanho_janela]
        h, c = calcular_metricas_hc(sub_sinal)
        
        resultados.append({
            'Tempo_Inicio': i,
            'Tempo_Fim': i + tamanho_janela,
            'Janela': f'T{i//passo}',
            'Entropia (H)': h,
            'Complexidade (C)': c
        })
        
    return pd.DataFrame(resultados)

def diagnosticar_anomalia(df_resultados, limiar_complexidade=0.3):
    """
    Analisa as trajetórias no espaço de fase para detectar a quebra de simetria ordinal.
    Retorna o dataframe da janela anômala, se existir.
    """
    anomalias = df_resultados[df_resultados['Complexidade (C)'] > limiar_complexidade]
    return anomalias if not anomalias.empty else None