#Crie um programa que crie uma matriz 3 x3 na tela
#e preencha com os valores lidos pelo teclado
#0 #  #  #
#1 #  #  #
#2 #  #  #
#  0  1  2

lista = [[[], [], []], [[], [], []], [[], [], []]]
num = []
for c in range(0,9):
    
    num = int(input('Digite o número(0.0): '))
    lista[0] [0].append(num)

    num = int(input('Digite o número(0.1): '))
    lista[0][1].append(num)

    num = int(input('Digite o número(0.2): '))
    lista[0][2].append(num)

    num = int(input('Digite o número(1.0): '))
    lista[1][0].append(num)

    num = int(input('Digite o número(1.1): '))
    lista[1][1].append(num)

    num = int(input('Digite o número(1.2): '))
    lista[1][2].append(num)

    num = int(input('Digite o número(2.0): '))
    lista[2][0].append(num)

    num = int(input('Digite o número(2.1): '))
    lista[2][1].append(num)

    num = int(input('Digite o número(2.0): '))
    lista[2][2].append(num)
    break

print(f'  {lista[0][0]}    {lista[0][1]}    {lista[0][2]}    \n')
print(f'  {lista[1][0]}    {lista[1][1]}    {lista[1][2]}    \n')
print(f'  {lista[2][0]}    {lista[2][1]}    {lista[2][2]}    \n')









