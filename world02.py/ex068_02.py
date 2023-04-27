#criar um programa que jogue par ou impar com o usuário, termina quando o usuário perder
#mostre quantas vezes ele ganhou
#import random
#lista = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
#restd = 0
#cont = 0

#print('======== PAR OU IMPAR --------')
#resp = int(input('\n======== Quer Jogar ? ========\n\n  [[1]]  SIM\n\n  [[0]]  NÃO\n\n============================== \n   '))

#while resp != 0 and resp != 1:
#    print('\n==== RESPOSTA INVÁLIDA =====\n\n==== TENTE NOVAMENTE ! ====')
#   resp = int(input('\n======== Quer Jogar ? ========\n\n  [[1]]  SIM\n\n  [[0]]  NÃO\n\n============================== \n   '))
#if resp == 0:
    print('======== FIM DE JOGO =========')
#if resp == 1:    
#    while restd % 2 == 1 and parimpar == 1:
#        maquina = random.choice(lista)
#       n = int(input('Digite um número: '))
#        parimpar =int(input('\nQuer PAR ou IMPAR ?\n\n [[0]] PAR \n\n [[1]] IMPAR \n\n'))
#       restd = n + maquina
#        cont += 1
#       if restd % 2 == 0 and parimpar == 0:
#            print('Você ganhou!')
#            print(f'Número Maquina: {maquina}\nSeu Número: {n} \nTotal: {restd}')
#        if restd % 2 == 1 and parimpar == 1:
#            print('Você perdeu! ')
#            cont -= 1
#            print(f'Número Maquina: {maquina}\nSeu Número: {n} \nTotal: {restd}')
#            print(f'você teve {cont} vitórias')
#            print('======= Fim do Jogo ======= ')
