#crie um programa onde 4 jogadores joguem um dado e tenham resultados aleátórios
#guarde esses resultados em um dicionários e
# no final , coloque esse dicionário em ordem , sabendo que o vencedor tirou o maior número no dado

from random import randint
from operator import itemgetter, attrgetter
from time import sleep
cont = 0
jogt = {}
jogadores = dict()

print('-=' *30 )
print('jogo de dados')
for c in range(0,4):
    jogt['Jogador_01'] = randint(1,6)
    jogt['Jogador_02'] = randint(1,6)
    jogt['Jogador_03'] = randint(1,6)
    jogt['Jogador_04'] = randint(1,6)
    
for i,j in jogt.items():
    print(f'O {i} tirou o número {j}')
    sleep(1)
print('-=' *30)
for d in sorted(jogt,key=jogt.get,reverse=True):
    cont +=1
    print(f'O {d} ficou em {cont}° lugar - {jogt[d]}')
    sleep(1)