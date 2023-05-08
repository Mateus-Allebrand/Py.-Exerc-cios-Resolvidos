# Faça um programa que leia nome e peso de varias pessoas e guarade tudo em uma lista
#quantas pessoas foram cadastradas?
#lista com as pessoas mais pesadas
#uma lista com as pessoas mais leves

dados = list()
lista = []
pesa = list()
leves = list()
cont = 0
contp = 0
pes = 0
menpes = 0

while True:
    nome = str(input('Digite o nome: \n'))
    dados.append(nome)
    peso = float(input('Digite o peso: \n'))
    dados.append(peso)
    lista.append(dados[:])
    cont += 1
    dados.clear()
    x = str(input('Deseja continuar? ')).upper()[0]
    while x not in 'SN':
        print('Resposta inválida!\n')
        x = str(input('\nDeseja continuar? ')).upper()[0]
    if x == 'N':
        print(' ===> Fim <=== ')
        break

for c in lista:
    contp += 1
    if contp == 1:
       pes = (c[1])
       menpes = (c[1])
    else:
        if c[1] > pes:
            pes = c[1]
        if c[1] < menpes:
            menpes = c[1]

print(f'lista de cadastrados: {lista}')
print(f' Foram cadastrados {cont} pessoas')
print(f'O mais pesado pesa: {pes:.2f} quilos')
print(f'O menos pesado pesa: {menpes:.2f} quilos')




