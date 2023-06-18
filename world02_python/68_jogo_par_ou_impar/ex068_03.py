import random
maquina = random.randint(1, 10)
restd = 0
n = 0
cont = 0
print('======== PAR OU IMPAR ========')
while True:
    resp = int(input('\n         QUER JOGAR?   \n\n   [[1]] SIM \n\n   [[0]] NÃO \n\n    '))
    if resp == 0:
        print('==== FIM DE JOGO ====')
        break
    if resp != 1:
        print('==== DÍGITO INVÁLIDO ====')
        break
    n = int(input('Digite um número: '))
    parimpar = int(input('\nQuer par ou impar ? \n\n [[0]] PAR \n\n [[1]] IMPAR \n'))
    restd = maquina + n
    print(f'Maquina número: {maquina} \nSeu número: {n} \nTOTAL: {restd}')
    if restd % 2 == 0 and parimpar == 0:
        cont += 1
        print(f'==== VOCÊ GANHOU ! ==== \n ' )
        print(f'Maquina número: {maquina} \nSeu número: {n} \nTOTAL: {restd} PAR')
    if restd % 2 == 1 and parimpar == 1:
        cont += 1
        print(f'==== VOCÊ GANHOU ! ==== \n ' )
        print(f'Maquina número: {maquina} \nSeu número: {n} \nTOTAL: {restd} IMPAR')
    if restd % 2 == 0 and parimpar == 1:
        print(f'\n==== VOCÊ PERDEU ! ==== \n venceu {cont} vez(es) consecutiva(s)' )
        print(f'\nMaquina número: {maquina} \nSeu número: {n} \nTOTAL: {restd} PAR')
        break
    if restd % 2 == 1 and parimpar == 0:
        print(f'\n==== VOCÊ PERDEU ! ==== \n\n venceu {cont} vez(es) consecutiva(s)' )
        print(f'\nMaquina número: {maquina} \nSeu número: {n} \nTOTAL: {restd} IMPAR')
        break