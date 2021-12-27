# -*- coding: utf-8 -*-
"""semana 4_exercicios de apoio e anotacoes.ipynb

#Anotações das aulas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#histograma (distribuição) que gera 30 valores (sendo 1 por dia) com minutos de 0 a 60
minutos = np.random.randint(0,60,30)

minutos

import seaborn as sns
ax = sns.histplot(data=minutos)
ax.set(xlabel='Minutos Por Dia', ylabel='Quantidade de Vezes')
plt.show()

arquivo ='https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2021.csv' #arquivo que contem dados dos jogos de tenis em 2021

dados = pd.read_csv(arquivo)
dados.head(5)

dados.info

dados.describe(include='all')

dados.isnull()

dados.isnull().sum() #checando dados nulos nas colunas

#Apagar todas as linhas que o atributo "loser_rank" é nulo, porque são poucas ocasioes e isso pode implicar erros nos resultados
dados.dropna(subset=['loser_rank'], inplace=True)

dados

#apagar todas as coluna que apresentam resultados nulos
dados.dropna(axis=1, how= 'all')

dados.duplicated() #identificando duplicados

dados.duplicated().sum()

"""##EDA"""

import sweetviz #biblioteca para análise exploratória

eda = sweetviz.analyze(dados)  # eda = exploratory data analysis
eda.show_html()

"""##Correlação"""

mask = np.triu(np.ones_like(dados.corr(), dtype=bool)) #na correlação de Pearson, o valor 1 é a correlação direta perfeita; -1 é correlação negativa perfeita e valores próximos de zero indicam a falta de existência ou dificuldade de estabelecer correlação

plt.figure(figsize=(20,20))
sns.heatmap(dados.corr(), mask=mask, square = True, annot=True, vmin=-1, vmax=1)
plt.show()

"""#Exercícios"""

#1. Importe os dados de um arquivo CSV com informações de filmes da Marvel, que está disponível em: https://www.kaggle.com/rachit239/mcu-complete-dataset
filmes = pd.read_csv('semana 4_mcu dataset.csv')

filmes.head(5)

#2. Usando a biblioteca Sweetviz, verifique qual foi o valor de orçamento (budget) que aconteceu mais vezes nos filmes da Marvel, e indique qual a porcentagem de vezes que esse valor foi determinado para os filmes.
eda = sweetviz.analyze(filmes)
eda.show_html()

#O valor que apareceu mais vezes de orçamento foi de US$200 milhões e corresponde a 17% dos filmes produzidos

#3. Usando uma correlação de Pearson, verifique, no database da Marvel, quais são as variáveis que tem maior correlação positiva.
mask = np.triu(np.ones_like(filmes.corr(), dtype=bool))

plt.figure(figsize=(20,20))
sns.heatmap(filmes.corr(), mask=mask, square = True, annot=True, vmin=-1, vmax=1)
plt.show()

#Conforme é possível ver abaixo, as variáveis com maior correlacão positiva são: Oscar Nomination e Oscar Won. Ou seja, grande parte da vezes quando um filme é indicado ao Oscar, ele vence.

#4. Entre no Portal Brasileiro de Dados Abertos e baixe o arquivo CSV da Relação de Empreendimentos de Geração (https://dados.gov.br/dataset/relacao-de-empreendimentos-de-geracao). Informe qual é a licença atribuída a esse dado.

# A licença atribuída é OpenData

#5. Importe somente as primeiras 500 linhas desse arquivo CSV que foi baixado. Observe que como esse arquivo é de origem brasileira, precisaremos utilizar o parâmetro encoding='iso-8859-1' na função read_csv do pandas.

dados_abertos=pd.read_csv("semana 4_EmpreendimentoOperacao.csv",sep=',', nrows=500, encoding='iso-8859-1')

dados_abertos.head(5)

#6. Com os dados de Empreendimentos de Geração, indique qual é o atributo que mais tem valores nulos e elimine-o.

dados_abertos.isnull().sum()

del dados_abertos['mdaPotenciaFiscalizadakW']
dados_abertos.info()

#7.  Com os dados de Empreendimentos de Geração, indique qual é o atributo que tem valores nulos na menor quantidade e elimine as linhas que tem esses atributos com valor nulo.

dados_abertos.shape[0]

dados_abertos.dropna(subset=['dscMunicipio'], inplace=True)

dados_abertos.shape[0]

#8. Com os dados de Empreendimentos de Geração, crie uma nova coluna chamada “mdaPotenciaOutorgadaMW”, baseada na coluna “mdaPotenciaOutorgadakW”. Observe que a nova coluna é em Megawatt e a anterior Kilowatt.

dados_abertos['mdaPotenciaOutorgadaMW'] = dados_abertos['mdaPotenciaOutorgadakW']/1000

dados_abertos.head(5)

#9. Com os dados de Empreendimentos de Geração, na coluna datOperação, deixe apenas a data nos valores, eliminando a informação sobre horas.

dados_abertos['datOperacao'] = dados_abertos['datOperacao'].str.replace(' 00:00:00','')

dados_abertos['datOperacao'].head(5)