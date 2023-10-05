from pandas import DataFrame

dados = {"Estados": ["RS", "SC", "PR", "SP","RJ","RN"],
         "Ano": [2003, 2001, 2005, 2008, 2009,2002],
         "Taxa_Desemprego": [1.4, 2.5, 3.8, 5.1, 3.1, 1.3]
         }

df = DataFrame(dados)

#Aqui imprimo todos os dados 
print(df)  

#Aqui só imprimo  os 5 primeiros dados
print(df.head())   

#Aqui estou redefinindo a ordem das colunas
print(DataFrame(dados, columns= ("Estados", "Taxa_Desemprego", "Ano"))) 
