#crie um programa que gere 5 números aleátórios e coloque dentro de uma tupla
#mostre a listagem de núemros
#indique o maior e o menor

import math
import random
cont = 0
list = []
tup = ()
while cont < 5:
    ran = random.randint(0,999)
    cont +=1
    list.append(ran)
for c in list:
    print(f'{c} ', end='')
print(f'\nO maior número é {max(list)}')
print(f'O menor número é {min(list)}')