#Crie um programa que crie uma matriz 3 x3 na tela
#e preencha com os valores lidos pelo teclado
#0 #  #  #
#1 #  #  #
#2 #  #  #
#  0  1  2
lista = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'digite uma número: {[l], [c]} '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()