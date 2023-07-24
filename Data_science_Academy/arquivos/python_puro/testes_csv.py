import pandas as pd


cont = 0
cont2 = 0

dados = open("salarios.csv","r") # abrindo arquivo csv para leitura 

db = dados.read() #lendo arquivo e salvando em uma variavel

lista = db.split("\n") # separando por \n 


full_data = []

for i in lista:
    rows_split = i.split(",")
    full_data.append(rows_split)


full_data[0].insert(1, "lastname") #Na lista externa na posição 0, estou incluindo um item na posição 1


for row in full_data:
    cont +=1
print(f"N° linhas {cont}") # imprimendo o número de linhas


for rown in full_data[0]:
    cont2 +=1
print(f"N° colunas {cont2}") # imprimendo o número de colunas


n3 = open("arquivo.txt","r") #abrindo um arquivo txt e salvando em uma variavel

print(n3.readlines()) #lendo um arquivo linha a linha e imprimendo na tela

for i in open("arquivo.txt"):  #imprimindo um arquivo linha a linha com laço FOR
    print(i)








# df =pd.read_csv("salarios.csv")

# print(df)