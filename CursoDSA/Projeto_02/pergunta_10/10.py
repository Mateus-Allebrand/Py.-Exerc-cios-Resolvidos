## Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias):

### Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? 

#Demonstre tudo através de um único gráfico.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

#'Categoria', 'SubCategoria'

df = pd.read_csv("dataset.csv")

dados = df.groupby('Categoria')['Valor_Venda'].sum()
dados2 = df.groupby('SubCategoria')['Valor_Venda'].sum()
dados2=dados2.sort_values(ascending=False)
for i,j in dados.items():
    print(f"{i:<20}       R${j:>10.2f}")

dados_arm ={}
cont = 0
for i,j in dados2.items():
    cont +=1
    if cont == 13:
        break
    dados_arm[i] = j

print("")
for i,j in dados_arm.items():
    print(f"{i:<20}       R${j:>10.2f}")
  



