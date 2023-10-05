### Pergunta de Negócio 1:
### Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv("dataset.csv")

resp1 = df[df["Categoria"] == "Office Supplies"]

cid = resp1.groupby('Cidade')['Valor_Venda'].sum()

print(f"A Cidade com menor Valor de Venda de Produtos da Categoria 'Office Supplies': {cid.idxmin()}")
print(f"A Cidade com maior Valor de Venda de Produtos da Categoria 'Office Supplies': {cid.idxmax()}")

conf = cid.sort_values(ascending=False)
print(conf)