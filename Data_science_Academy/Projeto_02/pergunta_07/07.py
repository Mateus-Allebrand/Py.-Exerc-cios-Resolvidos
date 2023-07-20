## Pergunta de Negócio 7 (Desafio Nível Júnior):

# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:

# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.

### Quantas Vendas Receberiam 15% de Desconto?

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


df = pd.read_csv("dataset.csv")

resp1 = df[df["Valor_Venda"] > 1000].count()

resp2 = df[df["Valor_Venda"] < 1000].count()

print(f"Total de {resp1[0]} vendas receberiam 15% de desconto")

# Cria uma nova coluna de acordo com a regra definida acima
#df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10) => Outra forma de resolver
                                                            #True,"False"