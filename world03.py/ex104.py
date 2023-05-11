#crie um programa que o programa principal só possa ter duas linhas
#######################################################
#               PROGRAMA PRINCIPAL:                   #
# n = leiaint('Digite um número: ')                   #
# print('Você acabou de digitar o número {n})        #
#######################################################

def leiaint(msg):
    fl = False
    num = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            return num
            fl = True
        else:
            print('Erro! Digite um número valido!')
        if fl == True:
            break
           



n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')