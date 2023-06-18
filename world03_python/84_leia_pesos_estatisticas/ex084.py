# OUTRA FORMA DE RESOLVER

# Faça um programa que leia nome e peso de varias pessoas e guarade tudo em uma lista
#quantas pessoas foram cadastradas?
#lista com as pessoas mais pesadas
#uma lista com as pessoas mais leves
from operator import itemgetter, attrgetter
dados = list()
lista = []
pesa = list()
pesado = []
leves = list()
mleve = []
cont = 0
maior = 0 
menor = 0


while True:
    nome = str(input('Digite o nome: \n'))
    dados.append(nome)
    peso = float(input('Digite o peso: \n'))
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()
    x = str(input('Deseja continuar? ')).upper()[0]
    while x not in 'SN':
        print('Resposta inválida!\n')
        x = str(input('\nDeseja continuar? ')).upper()[0]
    if x == 'N':
        print(' ===> Fim <=== ')
        break
    
leves.append(sorted(lista,key=itemgetter(1)))
pesa.append(sorted(lista,key=itemgetter(1),reverse=True))

print(f'O total de pessoas registradas foi: {len(lista)}')
print(f'Os dois mais pesados são: {pesa[0][:2]}')
print(f'Os dois mais leves são: {leves[0][:2]}')


