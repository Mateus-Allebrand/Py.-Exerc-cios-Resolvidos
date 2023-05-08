# OUTRA FORMA DE RESOLVER

# Faça um programa que leia nome e peso de varias pessoas e guarade tudo em uma lista
#quantas pessoas foram cadastradas?
#lista com as pessoas mais pesadas
#uma lista com as pessoas mais leves
dados = list()
lista = []
pesa = list()
leves = list()
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
for c in lista:
    cont += 1
    if cont == 1:
        maior = c[1]
        pesa.insert(0,c)
        menor = c[1]
        leves.insert(0,c)
    else:
        if c[1] > maior:
            pesa.insert(0,c)
        if c[1] < menor:
            leves.insert(0,c)

print(f'O mais pesado da lista é : {pesa}')
print(f'O mais leve da lista é: {leves}')
