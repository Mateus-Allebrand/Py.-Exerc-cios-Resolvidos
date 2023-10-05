## Pergunta de Negócio 9 (Desafio Nível Master Ninja):

### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?

#Demonstre o resultado através de gráfico de linha.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


df = pd.read_csv("dataset.csv")

venda_seg = df.groupby('Segmento')['Valor_Venda'].mean()

pd.options.display.float_format = '{:.2f}'.format

valor_consumer = venda_seg.loc['Consumer']
print(f"\033[32mMédia de vendas do Segmento Consumer: R${valor_consumer:.2f}")

valor_Corporate = venda_seg.loc['Corporate']
print(f"Média de vendas do Segmento Corporate: R${valor_Corporate:.2f}")

valor_Home_Office = venda_seg.loc['Home Office']
print(f"Média de vendas do Segmento Home Office: R${valor_Home_Office:.2f}\033[m")



df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format='%d/%m/%Y')

df['Ano'] = df['Data_Pedido'].dt.year
df['Mes'] = df['Data_Pedido'].dt.month

media_ano = df.groupby('Ano')['Valor_Venda'].mean()

pd.options.display.float_format = '{:.2f}'.format

for ano, media in media_ano.items():
    print(f"\033[34mMédia de vendas em {ano}: {media:.2f}\033[m")

media_mes = df.groupby('Mes')['Valor_Venda'].mean()


for mes, media in media_mes.items():
    print(f"\033[35mMédia de vendas em {mes}: {media:.2f}\033[m")

plt.figure(figsize=(10, 6))
plt.plot(media_ano.index, media_ano.values, marker='o', color='b')
plt.xlabel('Ano')
plt.ylabel('Média de Vendas')
plt.title('Média de Vendas por Ano')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(media_mes.index, media_mes.values, marker='o', color='b')
plt.xlabel('Mes')
plt.ylabel('Média de Vendas')
plt.title('Média de Vendas por Mes')
plt.grid(True)
plt.show()


#Poderia usar o relplot do seaborn que fazer relações  com mais de uma variaveis