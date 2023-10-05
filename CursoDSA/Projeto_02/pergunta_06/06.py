## Pergunta de Negócio 6 (Desafio Nível Baby):
### Qual o Total de Vendas Por Segmento e Por Ano?

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


df = pd.read_csv("dataset.csv")

df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format='%d/%m/%Y')

df['Ano'] = df['Data_Pedido'].dt.year

venda_seg = df.groupby(['Ano','Segmento'])['Valor_Venda'].sum()

pd.options.display.float_format = '{:.2f}'.format

print(venda_seg)


