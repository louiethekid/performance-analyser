import streamlit as st
import pandas as pd

# 1. Configuração da Página
st.set_page_config(page_title="Performance Analyser", layout="wide")

# 2. Sidebar - Upload e Configurações
st.sidebar.header("⚙️ Configurações")
uploaded_file = st.sidebar.file_uploader("1. Suba seu CSV de campanhas", type=["csv"])

# 3. Lógica Principal (Só roda se o arquivo existir)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
 
    # Cálculos Base
    df['ROAS'] = df['receita'] / df['investimento']
    df['CPA'] = df['investimento'] / df['conversoes']
    df['CTR'] = (df['cliques'] / df['impressoes']) * 100
   
    # 2. Input de Meta Dinâmica
    st.sidebar.divider()
    meta_roas = st.sidebar.slider("2. Defina a Meta de ROAS", 0.0, 10.0, 2.0)

    # Filtro de Campanha
    st.sidebar.divider()
    campanhas = st.sidebar.multiselect(
        "3. Filtrar Campanhas",
        options=df['nome_campanha'].unique(),
        default=df['nome_campanha'].unique()
    )
    
    df_filtrado = df[df['nome_campanha'].isin(campanhas)]

    # --- INTERFACE ---
    st.title("📊 Performance Analyser Dashboard")

    # Cálculos das Métricas
    roas_atual = df_filtrado['ROAS'].mean()
    delta_roas = roas_atual - meta_roas # Diferença para a meta

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="ROAS Médio", 
            value=f"{roas_atual:.2f}x",
            delta=f"{delta_roas:.2f} vs Meta",
            delta_color="normal" # Fica verde se > meta, vermelho se < meta
        )
    with col2:
        st.metric(label="CPA Médio", value=f"R$ {df_filtrado['CPA'].mean():.2f}")
    with col3:
        st.metric(label="Investimento Total", value=f"R$ {df_filtrado['investimento'].sum():,.2f}")

    # Alerta Visual de Status
    if roas_atual < meta_roas:
        st.error(f"⚠️ Performance abaixo da meta ({meta_roas:.1f}x)")
    else:
        st.success(f"✅ Performance batendo a meta!")

    st.divider()

    # Abas de Visualização
    tab1, tab2 = st.tabs(["Gráficos", "Dados Brutos"])

    with tab1:
        st.subheader("Análise Visual de ROAS")
        st.bar_chart(data=df_filtrado, x='nome_campanha', y='ROAS', color='#29b5e8')

    with tab2:
        st.subheader("Exploração de Dados")
        st.dataframe(df_filtrado, use_container_width=True)

else:
    # Tela de Boas-vindas (Zero State)
    st.title("📊 Performance Analyser")
    st.info("👋 Olá! Comece arrastando o arquivo CSV das suas campanhas na barra lateral.")