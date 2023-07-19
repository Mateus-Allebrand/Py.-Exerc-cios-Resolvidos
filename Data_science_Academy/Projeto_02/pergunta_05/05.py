## Pergunta de Negócio 5:

## Qual Segmento Teve o Maior Total de Vendas?
# 
## Demonstre o resultado através de um gráfico de pizza.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv("dataset.csv")
dados = df.groupby('Segmento')['Valor_Venda'].sum()

labels = dados.index.tolist()



print(dados)
plt.pie(dados, labels =labels, autopct='%1.1f%%')

plt.title("Proporções")

plt.show()


