## Pergunta de Negócio 3:

## Qual o Total de Vendas por Estado?
#'Valor_Venda' , 'Estado'
## Demonstre o resultado através de um gráfico de barras.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt









df = pd.read_csv("/home/mateus/Documentos/Programacao/Python/Py.-Exercios-Resolvidos/CursoDSA/Projeto_02/dataset.csv")

# Agrupa os dados por estado, somando o valor da venda para cada estado
dados = df.groupby('Estado')['Valor_Venda'].sum().reset_index()

print(dados)

plt.figure(figsize=(20, 6))

sns.barplot(x='Estado', y='Valor_Venda', data=dados).set(title="Vendas por Estado")
plt.xticks(rotation=80)
plt.show()