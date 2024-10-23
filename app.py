import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go

df_casos_anos = pd.DataFrame({
  'Ano': [2020, 2021, 2022, 2023, 2024],
  'Dengue': [6766, 16443, 29253, 7240, 13370],
  'Chikungunya': [2024, 10783, 18858, 1449, 1544],
  'Zika': [359, 1834, 638, 111, 86]
})

df_classificacao = pd.DataFrame({
  'Classificação': ['Confirmado', 'Suspeito', 'Descartado'],
  'Casos': [12115, 37898, 22898]
})

df_faixa_etaria = pd.DataFrame({
  'Faixa Etária': ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60+'],
  'Masculino': [500, 800, 1000, 1200, 1100, 900, 700],
  'Feminino': [600, 900, 1100, 1300, 1200, 1000, 800]
})

app = dash.Dash(__name__)

# Layout do App com duas colunas
app.layout = html.Div([

    html.H1("CENÁRIO EPIDEMIOLÓGICO DAS ARBOVIROSES NA PARAÍBA ", style={'textAlign': 'center'}),

    # Criando a estrutura de duas colunas
    html.Div([
        # Primeira coluna
        html.Div([
            # Casos Prováveis nos Últimos 5 anos (Gráfico de Barras)
            html.H3("Casos Prováveis de Dengue, Chikungunya e Zika - Últimos 5 Anos"),
            dcc.Graph(
                id='casos-5-anos',
                figure=px.bar(df_casos_anos, x='Ano', y=['Dengue', 'Chikungunya', 'Zika'],
                              title='Evolução de Casos Prováveis (2020-2024)',
                              labels={'value': 'Casos', 'variable': 'Doenças'},
                              barmode='group')
            ),

            # Casos Prováveis de Dengue por Faixa Etária e Sexo (Gráfico)
            html.H3("Casos Prováveis de Dengue por Faixa Etária e Sexo - 2024"),
            dcc.Graph(
                id='faixa-etaria-sexo',
                figure=go.Figure(data=[
                    go.Bar(name='Masculino', x=df_faixa_etaria['Faixa Etária'], y=df_faixa_etaria['Masculino']),
                    go.Bar(name='Feminino', x=df_faixa_etaria['Faixa Etária'], y=df_faixa_etaria['Feminino'])
                ]).update_layout(barmode='group', title='Casos por Faixa Etária e Sexo (2024)',
                                 xaxis_title='Faixa Etária', yaxis_title='Casos')
            )
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'}),

        # Segunda coluna
        html.Div([
          # Classificação dos Casos de Arboviroses (Gráfico de Pizza)
            html.H3("Classificação dos Casos de Arboviroses - 2024"),
            dcc.Graph(
                id='classificacao-arboviroses',
                figure=px.pie(df_classificacao, values='Casos', names='Classificação',
                              title='Classificação dos Casos de Arboviroses (2024)')
            ),
            
        ], style={'width': '50%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'display': 'flex', 'flex-direction': 'row'})    
])

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run_server(host='0.0.0.0', port=port)



