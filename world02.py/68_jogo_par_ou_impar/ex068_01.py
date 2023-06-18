#criar um programa que jogue par o impar com o usuário


#Programa principal
import random
print( ' ======= PAR OU IMPAR -------')
resp = int(input('\n        Deseja jogar ? \n\n [[1]] SIM \n\n [[0]] NÃO \n\n=============================\n         '))
lista =[1,2,3,4,5,6,7,8,9,10]
nmaquina = random.choice(lista)
n = 0
comp = 0
fl = 0
while resp != 0 and resp!= 1:
        print('==== DÍGITO INVÁVIDO ==== \n\n==== TENTE NOVAMENTE =====')
        resp = int(input('\n   Deseja jogar novamente ? \n\n [[1]] SIM \n\n [[0]] NÃO \n\n=============================\n         '))
while resp != fl and resp == 1:
    n = int(input('Escolha um número inteiro de 1 a 10:\n '))
    parimp = int(input('VOCÊ QUER PAR OU IMPAR?\n [[0]] PAR \n [[1]] IMPAR \n' ))
    comp = nmaquina + n
    if comp % 2 == 0:
        print(f'Número da maquina: {nmaquina} \nSeu número:  {n}\n        {comp} ')
        if parimp == 0:
            print('======== PAR ========\n     VOCÊ GANHOU !')
        else:
            print('======== PAR ========\n     VOCÊ PERDEU !')
    if comp % 2 == 1:
        print(f'Número da maquina: {nmaquina} \nSeu número:  {n}\n        {comp}') 
        if parimp == 1:
            print('======== IMPAR ========\n        VOCÊ GANHOU !')   
        else:
            print('======== IMPAR ========\n   VOCÊ PERDEU !')
    nmaquina = random.choice(lista)
    print('\n======== FIM DE JOGO ========')
    resp = int(input('\n   Deseja jogar novamente ? \n\n [[1]] SIM \n\n [[0]] NÃO \n\n=============================\n         '))
    if resp != 0 and resp!= 1:
        print('==== DÍGITO INVÁVIDO ==== \n\n==== TENTE NOVAMENTE =====')
        resp = int(input('\n   Deseja jogar novamente ? \n\n [[1]] SIM \n\n [[0]] NÃO \n\n=============================\n         '))
print('\n======== FIM DE JOGO ========')