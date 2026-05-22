import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

from engine import (
    processar_janelas_deslizantes,
    diagnosticar_anomalia
)

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="SIDE-O | Diagnóstico Deep Tech",
    layout="wide"
)

# =========================================================
# HEADER
# =========================================================

st.title("🖥️ SIDE-O: Framework de Complexidade-Entropia")
st.markdown(
    """
    ### Sistema Inteligente de Diagnóstico de Emissões Offshore

    Monitoramento de emissões via Dinâmica Não-Linear,
    Complexidade Estatística e Teoria da Informação.
    """
)

st.markdown("---")

# =========================================================
# PATHS ROBUSTOS (FUNCIONA LOCAL + STREAMLIT CLOUD)
# =========================================================

BASE_DIR = Path(__file__).parent

CSV_PATH = BASE_DIR / "sensor_gas_dataset.csv"

# =========================================================
# SIDEBAR DEBUG / AMBIENTE
# =========================================================

with st.sidebar:
    st.header("⚙️ Ambiente")
    st.write(f"📁 Diretório Base:")
    st.code(str(BASE_DIR))

    st.write("📄 Dataset Detectado:")
    st.code(str(CSV_PATH.exists()))

# =========================================================
# VARIÁVEL PRINCIPAL
# =========================================================

df_bruto = None

# =========================================================
# ENTRADA DE DADOS
# =========================================================

col1, col2 = st.columns(2)

# ---------------------------------------------------------
# MODO MANUAL
# ---------------------------------------------------------

with col1:

    st.subheader("📥 Upload Manual")

    uploaded_file = st.file_uploader(
        "Subir série temporal (.csv)",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:
            df_bruto = pd.read_csv(uploaded_file)

            st.success("Dataset carregado com sucesso!")

        except Exception as e:

            st.error(f"Erro ao carregar arquivo: {e}")

# ---------------------------------------------------------
# MODO DEMONSTRAÇÃO
# ---------------------------------------------------------

with col2:

    st.subheader("🚀 Modo Demonstração")

    if CSV_PATH.exists():

        st.success(
            f"Dataset calibrado '{CSV_PATH.name}' detectado!"
        )

        if st.button("Executar Diagnóstico com Dataset Simulado"):

            try:
                df_bruto = pd.read_csv(CSV_PATH)

                st.success("Dataset de demonstração carregado!")

            except Exception as e:

                st.error(f"Erro ao carregar dataset: {e}")

    else:

        st.warning(
            "Arquivo 'sensor_gas_dataset.csv' não encontrado."
        )

# =========================================================
# PROCESSAMENTO PRINCIPAL
# =========================================================

if df_bruto is not None:

    try:

        # -------------------------------------------------
        # EXTRAÇÃO DO SINAL
        # -------------------------------------------------

        coluna_tempo = df_bruto.columns[0]
        coluna_sinal = df_bruto.columns[1]

        sinal = df_bruto[coluna_sinal].values

        # -------------------------------------------------
        # VISUALIZAÇÃO DO SINAL BRUTO
        # -------------------------------------------------

        st.markdown("---")
        st.header("📈 Imersão do Sinal Bruto")

        fig_sinal = px.line(
            df_bruto,
            x=coluna_tempo,
            y=coluna_sinal,
            title="Série Temporal do Ativo (PPM)"
        )

        fig_sinal.update_traces(
            line_color="gray"
        )

        st.plotly_chart(
            fig_sinal,
            use_container_width=True
        )

        # -------------------------------------------------
        # PROCESSAMENTO H × C
        # -------------------------------------------------

        st.markdown("---")
        st.header("🧠 Processamento Dinâmico")

        with st.spinner(
            "Executando análise de Complexidade-Entropia..."
        ):

            df_hc = processar_janelas_deslizantes(
                sinal,
                tamanho_janela=100,
                passo=20
            )

        st.success("Processamento concluído.")

        # -------------------------------------------------
        # PLANO H × C
        # -------------------------------------------------

        st.header(
            "🌌 Plano de Causalidade Complexidade-Entropia ($H \\times C$)"
        )

        fig_plano = px.scatter(
            df_hc,
            x="Entropia (H)",
            y="Complexidade (C)",
            text="Janela",
            color="Complexidade (C)",
            color_continuous_scale="Reds",
            title="Trajetória Causal e Detecção de Transição de Fase"
        )

        fig_plano.update_traces(
            mode="lines+markers",
            marker=dict(
                size=12,
                line=dict(
                    width=1.5,
                    color="DarkSlateGrey"
                )
            )
        )

        st.plotly_chart(
            fig_plano,
            use_container_width=True
        )

        # -------------------------------------------------
        # DIAGNÓSTICO
        # -------------------------------------------------

        st.markdown("---")
        st.header("⚙️ Motor de Diagnóstico e Auditoria")

        alertas = diagnosticar_anomalia(
            df_hc,
            limiar_complexidade=0.15
        )

        # -------------------------------------------------
        # ALERTA DETECTADO
        # -------------------------------------------------

        if alertas is not None and not alertas.empty:

            janela_critica = alertas.iloc[0]["Janela"]

            valor_c = alertas.iloc[0]["Complexidade (C)"]

            st.error(
                f"""
                🚨 ALERTA PREVENTIVO

                Quebra de simetria ordinal detectada
                a partir da janela {janela_critica}.
                """
            )

            st.markdown(
                f"""
                ### Parecer Técnico

                A complexidade estatística escalou para:

                ## C = {valor_c:.4f}

                indicando transição de ruído de fundo
                estocástico para um padrão determinístico,
                compatível com assinatura de microemissão
                na linha offshore.
                """
            )

        # -------------------------------------------------
        # SEM ALERTAS
        # -------------------------------------------------

        else:

            st.success(
                """
                ✅ STATUS OPERACIONAL NORMAL

                Regime estacionário mantido.
                Nenhuma assinatura determinística
                crítica foi identificada.
                """
            )

        # -------------------------------------------------
        # TABELA RESULTADOS
        # -------------------------------------------------

        st.markdown("---")
        st.header("📊 Resultados Analíticos")

        st.dataframe(
            df_hc,
            use_container_width=True
        )

    # =====================================================
    # ERRO GLOBAL
    # =====================================================

    except Exception as e:

        st.error("Erro durante execução do pipeline.")

        st.exception(e)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    """
    SIDE-O • Sistema Inteligente de Diagnóstico de Emissões Offshore
    
    Framework Chaos-Aware para Monitoramento Ambiental
    
    Desenvolvido por Gabriel Christino
    """
)
