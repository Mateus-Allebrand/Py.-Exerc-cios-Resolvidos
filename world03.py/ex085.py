#Crie um programa que leia 7 valores númericos e guarde eles separados, pares e impares
#Ao final mostre os valores pares e mostre também os valores impares, em ordem crescente

lista  = []
par = []
impar = []

for c in range(0,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        if n % 2 == 1:
            impar.append(n)
par.sort()
impar.sort()
lista.append(par)
lista.append(impar)
print(lista)
print(f'valores pares:{par}')
print(f'Valores impares: {impar}')
