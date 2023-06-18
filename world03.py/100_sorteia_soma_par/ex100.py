#faça um programa que tenha uma lista que receberá números
# E tem que ter duas funções, uma para sortear 5 números e colocar na lista, e outra para somar os números par,e mostrar eles

from random import randint
lista = list()
ran = []





def sortear():
    for i in range(0,5):
        n = randint(1,10)
        while n in lista:
            n = randint(1,10)
        lista.append(n)
    print(f'Lista => {lista}')


def somapar():
    cpar = 0
    for c in lista:
        if c % 2 == 0:
            cpar += c
    print(f'Lista => {lista}\nA soma de todos os numeros pares nela é: {cpar}')

sortear()
somapar()
