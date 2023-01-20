# # Definições Gerais
# import warnings
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# # Warnings ignoradas
# warnings.filterwarnings('ignore')


# Leitura dos arquivos da base de dados e da base de dados complementar para atribuir os continentes.
mortes = pd.read_csv('cause_of_deaths.csv')
data_continent = pd.read_csv('Paises_X_Doencas/gapminder.tsv', sep='\t')


# Criação de uma nova coluna 'Continent' por meio do dataset obtido em 'gapminder.tsv' 
paises = list(data_continent['country'])
continentes = list(data_continent['continent'])
associacao = dict(zip(paises,continentes))

for i in mortes.index:
    if mortes.loc[i, 'Country/Territory'] in associacao:
        mortes.loc[i, 'Continent'] = associacao[mortes.loc[i, 'Country/Territory']]


# Obtendo os dados em relação aos continentes
somatorio_doencas_continente = mortes.groupby('Continent').sum()
maiores_causas_continentes = somatorio_doencas_continente.idxmax(axis=1)
print(maiores_causas_continentes)


# Obtendo os dados em relação aos países
somatorio_doencas_paises = mortes.groupby(['Country/Territory']).sum().drop('Year', axis=1)
maiores_causas_paises = somatorio_doencas_paises.idxmax(axis=1)
print(maiores_causas_paises.head(30))


# Selecionando os dados referentes ao Brasil
mask_brasil = mortes['Country/Territory'] == 'Brazil'
dados_brasil = mortes.loc[mask_brasil, :] #Dados Completos do Brasil
dados_brasil_reduzido = mortes.iloc[750:780, 3:-1] #Dados reduzidos, pegando apenas as doenças

somatorio_doencas_brasil = dados_brasil_reduzido.sum() # Quantidade total de mortes no Brasil por causa durante os anos 1990 até 2019

# Geração do gráfico que exibe as 10 maiores causas de morte no Brasil durante os anos 1990-2019
eixo_x = somatorio_doencas_brasil.sort_values(ascending=False)[:10].index
eixo_y = somatorio_doencas_brasil.sort_values(ascending=False)[:10].values
plt.figure(figsize=(15,12))
plt.barh(eixo_x, eixo_y, color='crimson')
plt.xlabel('Causas de Mortalidade')
plt.ylabel('Qtde de Mortes')
plt.title('10 maiores causas de morte no Brasil durante o período 1990-2019')
plt.show()