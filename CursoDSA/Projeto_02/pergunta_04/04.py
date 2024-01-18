## Pergunta de Negócio 4:

## Quais São as 10 Cidades com Maior Total de Vendas?

## Demonstre o resultado através de um gráfico de barras.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt



df = pd.read_csv("/home/mateus/Documentos/Programacao/Python/Py.-Exercios-Resolvidos/CursoDSA/Projeto_02/dataset.csv")
dados_f = {}
dados = df.groupby('Cidade')['Valor_Venda'].sum()

cont = 0
da = dados.sort_values(ascending=False)

for chave, valor in da.items():
    dados_f[chave] = valor
    cont +=1
    if cont == 10:
        break
        
df_cidades_maiores_vendas = pd.DataFrame(list(dados_f.items()), columns=['Cidade', 'Valor_Venda'])
print(df_cidades_maiores_vendas)

plt.figure(figsize=(20,6))

sns.barplot(x='Cidade', y='Valor_Venda', data=df_cidades_maiores_vendas).set(title="10 Cidades com maior venda")
plt.xticks(rotation=80)
plt.show()

plt.show(block=True)


#Consegui sem muitos problemas