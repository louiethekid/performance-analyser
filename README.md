📊 Performance Analyser: Dashboard Interativo de Marketing
Este projeto é uma solução Full-Stack Data focada em marketing digital e manutenção de Market Share. A aplicação transforma dados brutos de campanhas em um dashboard interativo, automatizando a análise de performance e o cálculo de métricas essenciais para a tomada de decisão.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](performance-analyser-2026.streamlit.app)


🎯 Objetivo
Otimizar o tempo de análise de gestores de tráfego, identificando rapidamente campanhas com ROAS (Return on Ad Spend) acima da média e controlando o CPA (Custo por Aquisição) de forma granular.

🛠️ Tecnologias Utilizadas
Python: Linguagem core para processamento de dados.

Pandas: Engine de manipulação de dados para limpeza e cálculo de métricas.

Streamlit: Framework de interface web para visualização interativa em tempo real.

Git/GitHub: Versionamento de código e CI/CD.

🚀 Funcionalidades do Dashboard
Cálculo Automatizado de KPIs:

ROAS: Receita gerada por valor investido.

CPA: Custo real de cada conversão.

CTR: Taxa de clique sobre impressões (eficiência do criativo).

Filtros Dinâmicos: Sidebar interativa para selecionar campanhas específicas e atualizar os gráficos e cartões de métricas instantaneamente.

Visualização Visual: Gráficos de barras interativos que facilitam a comparação rápida entre diferentes fontes de tráfego.

Tabela de Dados Brutos: Acesso rápido ao dataframe processado para conferência detalhada.

📋 Como Executar o Projeto
Para rodar este dashboard localmente, siga os passos:

Clone o repositório:

Bash
git clone https://github.com/louiethekid/performance-analyser.git
Ative seu ambiente virtual e instale as dependências:

Bash
pip install streamlit pandas
Execute a aplicação:

Bash
streamlit run app.py
