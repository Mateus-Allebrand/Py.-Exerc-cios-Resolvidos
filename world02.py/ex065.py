#crie um programa que leia números inteiros e pergunte se o usoário deseja continuar digitando mais números
#ao final mostre a media , qual maior valor e qual menor
import math
n = 0 
fin = 2
media = 0
maior = 0
cont = 0
print('========= Vamos Começar ========')
while fin != 0:
    n = int(input('digite um número inteiro: \n'))
    cont = cont + 1
    media = media + n
    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    fin = int(input('Deseja eniserir mais números? \n [1]SIM \n [0] NÃO \n'))
    if fin != 1 and fin != 0:
        print('Digito inválido. \nTente outra vez!')
        fin = int(input('Deseja eniserir mais números? \n [1]SIM \n [0] NÃO \n'))

media = media / cont
print('A média é {} '.format(media))
print('O maior valor é {}'.format(maior))
print('O menor valor é {}'.format(menor))
