#!/usr/bin/env python
# coding: utf-8

# ##Semana 2

# In[187]:


import numpy as np
import pandas as pd


# ##Exercícios

# 1. Criar um NDArray com os seguintes valores [1, 2.5, 7, -78, -0.9, 130, 25]

# In[188]:


lista1 = [1, 2.5, 7, -78, -0.9, 130, 25] 
dados1 = np.array(lista1)     
dados1  #toda a lista será criada com dados tipo float


# 2. Crie um NDArray com os valores de 0 a 10

# In[189]:


dados2 = np.arange(11)
dados2


# 3. Crie um NDArray de dimensão 2x5 com valores 1

# In[190]:


dadosones = np.ones((2,5))
dadosones


# 4. Crie um NDArray com valores de 1 a 100, com intervalos de 3 em 3.

# In[191]:


dados3 = np.arange(1,100,3)
dados3


# 5. Mostre as raízes quadradas dos valores do NDArray criado no exercícios 4.

# In[192]:


np.sqrt(dados3)


# 6. Altere a décima posição do NDArray criado no exercício 4 com o dobro do seu valor.

# In[193]:


dados3

dados3[9]=dados3[9] * 2
dados3 #o número alterado é o 28, que passa a ser 56 [lemos a 10ª posição como o número 28, mas o Python começa do 0, então a 10ª posição é a 9 do array]


# 7. Execute o comando para criar um Dataframe com os dados disponíveis no notebook.

# In[194]:


dados={'Empresa':['Microsoft', 'Google','Univesp','NVData Analytics','Power Bi Experience','USP'], 'Qtde Func':[1000, 1500,500, 100,100,499], 'Site':['https://www.microsoft.com/pt-br','https://www.google.com/','https://univesp.br/','https://www.nvdata.com.br/','https://powerbiexperience.com/pt/','https://www.usp.br/'],'Instagram':['@microsoft','@google','@univespoficial','@nv_data','@leokarpa','@usp.oficial'],'Criação':[1975,1998,2012,2019,2016,1934], 'País':['EUA','EUA','Brasil','Brasil','Brasil','Brasil']}


# In[195]:


empresas = pd.DataFrame(dados)
empresas


# 8. Execute um comando que seja possível identificar qual a média da quantidade de funcionários que as empresas listadas tem. Informe também a soma dos funcionários que as empresas tem.
# 

# In[196]:


empresas.describe(include='all')


# A média de funcionários é de 616,5

# In[197]:


empresas['Qtde Func'].sum() #soma de todos os funcionários


# 9. Mostre as primeiras 3 linhas do dataframe.

# In[198]:


empresas.head(3)


# 10. Mostre as últimas 3 linhas do dataframe.

# In[199]:


empresas.tail(3)


# 11. Liste apenas as linhas em que as empresas foram criadas nos últimos 10 anos. Informe a quantidade de registros.

# In[200]:


empresas[empresas['Criação']>=2011]


# 12. Vamos imaginar que em todas as empresas exista 1 chefe para cada 23 funcionários. Crie uma coluna que mostre a quantidade de chefes que cada empresa teria e depois informe quantos chefes teríamos ao todo. (os valores não precisam ser números inteiros, é apenas uma estimativa).
# 

# In[201]:


empresas['Chefes']=empresas['Qtde Func']/23
empresas


# In[202]:


empresas.Chefes.sum() #soma de chefes das empresas listadas acima


# In[203]:


s2.index


# In[204]:


s1.index


# In[205]:


#alterando os índices para letras
s2=pd.Series([1,2,-5,0], index=['a','b', 'c', 'd'])
s2


# ##Algumas anotações das aulas

# In[206]:


#como exemplo, foi criado um array com números aleatórios e numa dimensão  2x3
exemplo=np.random.rand(2,3)
exemplo


# In[207]:


#para saber o tipo dos dados neste array
exemplo.dtype


# In[208]:


#Tamanho
exemplo.shape


# In[209]:


# quantidade de dimensões
exemplo.ndim


# 
# 
# ---
# 
# 

# In[210]:


#Series (obs.: olhar para o índice do lado esquerdo)
s1=pd.Series([1,2,-5,0])
s1


# In[211]:


s1.values


# ##Anotações sobre características dos dataframes 

# In[212]:


#dataframe de exemplo:
empresas


# In[213]:


#excluir coluna
del empresas['Chefes']
empresas

#outra forma é:
# empresas.drop('Chefes', axis='columns', inplace=True) #o ´´´´inplace=True´´´ garante a exclusão definitiva e pode ser usado tanto para linha quanto para coluna

#para excluir linhas, pode-se usar:
#empresas.drop([0,1])   #neste caso, será excluída a linha 1 da coluna 0


# In[214]:


empresas.count()


# In[215]:


empresas.dtypes


# In[216]:


empresas.columns


# In[217]:


empresas.shape


# In[218]:


empresas.index


# In[219]:


empresas.sample(2) #pegando 2 amostras


# In[220]:


#alterando valores
empresas


# In[221]:


empresas['Qtde Func']=empresas['Qtde Func']+1 #vai adicionar 1 funcionário a cada empresa
empresas


# In[222]:


#ver dados de linhas
empresas.iloc[2]

