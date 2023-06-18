#crie um programa que leia 4 números pelo teclado e armazeneos em uma tupla, no final mostre
#Quantas vezes apareceu o valor 9?
#em que posição apareceu o valor 3?
#quais foram o valores pares

#Programa principal
list = []
cont = 0
par = []
while cont < 4:
    n = int(input('Digite um número: '))
    list.append(n)
    cont += 1
for c in list:
    print(f'{c} ', end='')
    if c % 2 == 0:
        par.append(c)
nove = list.count(9)
print(f'\nO número 9 apareceu {nove} vezes')
if 3 in list:
    tres = list.index(3)
    print(f'\nO número 3 apareceu na {tres + 1}° posição')
else:
    print('\nO número tres não se encontra na lista')
print(f'\nNúmeros pares: {par}')