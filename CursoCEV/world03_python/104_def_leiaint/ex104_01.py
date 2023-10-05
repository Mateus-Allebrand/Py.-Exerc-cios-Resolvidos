#crie um programa que o programa principal só possa ter duas linhas
#######################################################
#               PROGRAMA PRINCIPAL:                   #
# n = leiaint('Digite um número: ')                   #
# print('Você acabou de digitar o número {n})        #
#######################################################


def leiaint():
    n = input('Digite um número:')
    while n.isalpha():
        print('ERRO! Tente outra Vez!\n')
        n = input('Digite um número:')
    if n.isnumeric():
        print(f'Você acabou de digitar um número {n}')
    
    
leiaint()
