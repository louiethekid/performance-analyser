import pandas as pd

# 1. Carregar os dados
df = pd.read_csv('campanhas.csv')

# 2. Calcular KPIs (Métricas de Performance)
# ROAS = Receita / Investimento
df['ROAS'] = df['receita'] / df['investimento']

# CTR = (Cliques / Impressões) * 100
df['CTR'] = (df['cliques'] / df['impressoes']) * 100

# CPA = Investimento / Conversões
df['CPA'] = df['investimento'] / df['conversoes']

# 3. Filtrar as Top Campanhas (ROAS > 4)
top_performers = df[df['ROAS'] > 4]

print("--- RELATÓRIO DE PERFORMANCE ---")
print(df[['nome_campanha', 'ROAS', 'CTR', 'CPA']])
print("\n--- CAMPANHAS PARA ESCALAR (MARKET SHARE) ---")
print(top_performers['PMAXING WORLDVIEW'])

# Adicionar todos os arquivos (exceto o que estiver no .gitignore)
git add .

# Criar o ponto de restauração
git commit -m "feat: calculo de ROAS, CTR e CPA concluido"