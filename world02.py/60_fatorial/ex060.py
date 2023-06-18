#Faça um programa que leia um número qualquer e mostre o seu fatorial

#Programa principal
n = int(input('Digite um número: '))
a = n 
for c in range(n, 1 -1, -1):
    if c != n:
        n = c * n
print('O resultado de {}! é {} '.format(a, n))