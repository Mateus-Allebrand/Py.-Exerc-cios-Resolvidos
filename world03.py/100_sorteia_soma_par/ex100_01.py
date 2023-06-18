#faça um programa que tenha uma lista que receberá números
# E tem que ter duas funções, uma para sortear 5 números e colocar na lista, e outra para somar os números par,e mostrar eles
from time import sleep
from random import randint
lista = list()
ran = []





def sortear():
    print('=-> Gerando números <-= ')
    print(f'           \033[33m|\033[m ')
    print('           \033[33mv\033[m ')
    for i in range(0,5):
        n = randint(1,10)
        
        while n in lista:
            n = randint(1,10)
        print(f'           {n}...')
        sleep(0.3)
        lista.append(n)
    print(f'\nLista => {lista}')


def somapar():
    cpar = 0
    for c in lista:
        if c % 2 == 0:
            cpar += c
    print(f'\nA soma de todos os numeros pares nela é: {cpar}')

sortear()
somapar()
