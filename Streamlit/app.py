import streamlit as st
import pandas as pd
import plotly.express as px
import os
from engine import processar_janelas_deslizantes, diagnosticar_anomalia

# Configuração da UI
st.set_page_config(page_title="SIDE-O | Diagnóstico Deep Tech", layout="wide")
st.title("🖥️ SIDE-O: Framework de Complexidade-Entropia")
st.markdown("Monitoramento de Emissões Offshore via Dinâmica Não-Linear")
st.markdown("---")

# Variável principal de dados
df_bruto = None
caminho_csv = "sensor_gas_dataset.csv"

# Layout de entrada de dados
col1, col2 = st.columns(2)

with col1:
    st.write("📥 **Modo Avaliador: Upload Manual**")
    uploaded_file = st.file_uploader("Subir série temporal (.csv)", type=["csv"])
    if uploaded_file is not None:
        df_bruto = pd.read_csv(uploaded_file)

with col2:
    st.write("🚀 **Modo Demonstração (Auto-Load)**")
    if os.path.exists(caminho_csv):
        st.success(f"Dataset calibrado '{caminho_csv}' detectado no ambiente!")
        # Botão para carregar automaticamente sem precisar de upload
        if st.button("Executar Diagnóstico com Dados de Simulação"):
            df_bruto = pd.read_csv(caminho_csv)
    else:
        st.warning("Arquivo 'sensor_gas_dataset.csv' não encontrado. Gere o dataset ou faça upload manual.")

# ---------------------------------------------------------
# SÓ RODA SE TIVER DADOS CARREGADOS (Evita tela em branco)
# ---------------------------------------------------------
if df_bruto is not None:
    # Captura a segunda coluna (o sinal do sensor)
    coluna_sinal = df_bruto.columns[1]
    sinal = df_bruto[coluna_sinal].values
    
    st.markdown("---")
    st.header("Imersão do Sinal Bruto")
    
    # Exibe o sinal original
    fig_sinal = px.line(df_bruto, x=df_bruto.columns[0], y=coluna_sinal, title="Série Temporal do Ativo (PPM)")
    fig_sinal.update_traces(line_color='gray')
    st.plotly_chart(fig_sinal, use_container_width=True)

    # 1. Processamento Matemático (Chamando o Engine)
    df_hc = processar_janelas_deslizantes(sinal, tamanho_janela=100, passo=20)
    
    # 2. Visualização Dinâmica
    st.header("Plano de Causalidade Complexidade-Entropia ($H \\times C$)")
    
    fig_plano = px.scatter(
        df_hc, 
        x="Entropia (H)", 
        y="Complexidade (C)", 
        text="Janela",
        color="Complexidade (C)",
        color_continuous_scale="Reds",
        title="Trajetória Causal e Detecção de Transição de Fase"
    )
    fig_plano.update_traces(mode='lines+markers', marker=dict(size=12, line=dict(width=1.5, color='DarkSlateGrey')))
    st.plotly_chart(fig_plano, use_container_width=True)
    
    # 3. Diagnóstico e Alerta
    st.markdown("---")
    st.header("⚙️ Motor de Diagnóstico e Auditoria")
    
    # Limiar ajustado para o dataset que geramos (0.15 é um bom gatilho para a anomalia simulada)
    alertas = diagnosticar_anomalia(df_hc, limiar_complexidade=0.15) 
    
    if alertas is not None:
        janela_critica = alertas.iloc[0]['Janela']
        valor_c = alertas.iloc[0]['Complexidade (C)']
        st.error(f"🚨 **ALERTA PREVENTIVO:** Quebra de simetria ordinal detectada a partir da janela **{janela_critica}**.")
        st.write(f"**Parecer Técnico:** A complexidade estatística escalou para $C = {valor_c:.4f}$, indicando transição de ruído de fundo estocástico para um padrão determinístico (assinatura de microemissão na linha offshore).")
    else:
        st.success("✅ **Status:** Sistema Operacional Normal. Regime estacionário mantido.")