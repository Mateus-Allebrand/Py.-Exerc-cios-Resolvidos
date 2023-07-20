## Pergunta de Negócio 8 (Desafio Nível Master):

### Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt


df = pd.read_csv("dataset.csv")


resp1 = df[df['Valor_Venda'] > 1000]
media_ant = resp1['Valor_Venda'].mean()
media_dep =  media_ant - (media_ant * 0.15) 
print(f'Media antes do desconto: R$ {media_ant:.2f}')
print(f'Media depois do desconto: R$ {media_dep:.2f}')




#media_ant = df['Desconto'] = np.where(df['Valor_Venda'] > 1000,0.15,0.10)
# df['Desconto'].value_counts()

# print(df['Desconto'].value_counts())

# Cria uma nova coluna de acordo com a regra definida acima


#RESOLVIDO COM SUCESSO, FICOU MAIS SIMPLES POSSÍVEL