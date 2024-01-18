## Pergunta de Negócio 2:

## Qual o Total de Vendas Por Data do Pedido?
#Data_Pedido

## Demonstre o resultado através de um gráfico de barras.

from operator import itemgetter
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


df = pd.read_csv('/home/mateus/Documentos/Programacao/Python/Py.-Exercios-Resolvidos/CursoDSA/Projeto_02/dataset.csv')

dados = dict()

tot_v = df.groupby("Data_Pedido")['Valor_Venda'].sum()


print(tot_v)

plt.figure(figsize= (20, 6))
tot_v.plot(x = df["Data_Pedido"], y = df['Valor_Venda'], label = "vendas_datas")
plt.show()

#Obs: o grafico não esta mostrando "ao longo do tempo!"

