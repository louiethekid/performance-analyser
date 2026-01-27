import pandas as pd
import matplotlib.pyplot as plt

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
print(top_performers['nome_campanha'])
# 4. Gerar Gráfico de Barras
df.plot(kind='bar', x='nome_campanha', y='ROAS', color='skyblue')
plt.title('Performance: ROAS por Campanha')
plt.ylabel('Retorno (ROAS)')
plt.xticks(rotation=45)
plt.tight_layout()

# Salva a imagem na pasta do projeto
plt.savefig('resultado_performance.png')
print("\nGráfico salvo como 'resultado_performance.png'!")