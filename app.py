import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="Performance Analyser", layout="wide")

# 1. Carregar Dados
df = pd.read_csv('campanhas.csv')

# 2. Lógica de Performance (KPIs)
df['ROAS'] = df['receita'] / df['investimento']
df['CPA'] = df['investimento'] / df['conversoes']
df['CTR'] = (df['cliques'] / df['impressoes']) * 100

# Cálculos para os Cartões
total_investido = df['investimento'].sum()
roas_medio = df['ROAS'].mean()
cpa_medio = df['CPA'].mean()

# --- INTERFACE ---
st.title("📊 Performance Analyser Dashboard")

# Sidebar com Filtro de Campanha
st.sidebar.header("Configurações")
campanhas_selecionadas = st.sidebar.multiselect(
    "Filtrar por Campanha",
    options=df['nome_campanha'].unique(),
    default=df['nome_campanha'].unique()
)

# Filtrando o dataframe com base na seleção
df_filtrado = df[df['nome_campanha'].isin(campanhas_selecionadas)]

# Cartões de Métricas Dinâmicos
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="ROAS Médio", value=f"{roas_medio:.2f}x")
with col2:
    st.metric(label="CPA Médio", value=f"R$ {cpa_medio:.2f}")
with col3:
    st.metric(label="Investimento Total", value=f"R$ {total_investido:,.2f}")

st.divider()

# Gráficos e Tabelas
tab1, tab2 = st.tabs(["Performance Visual", "Tabela de Dados"])

with tab1:
    st.subheader("ROAS por Campanha")
    # Gráfico nativo do Streamlit (mais rápido e interativo)
    st.bar_chart(data=df_filtrado, x='nome_campanha', y='ROAS', color='#29b5e8')

with tab2:
    st.subheader("Detalhamento dos Dados")
    st.dataframe(df_filtrado, use_container_width=True)