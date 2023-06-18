#somando os pares

#Programa principal
d = 0
for c in range(1, 6+1):
    n = int(input('Enter a number: '))
    if (n % 2) == 0:
        d = d + n
print('somatorio dos números pares = {}'.format(d))