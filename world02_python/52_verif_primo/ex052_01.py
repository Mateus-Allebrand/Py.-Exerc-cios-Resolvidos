#verifique se é um número primo

#Programa principal
n = int(input('Digite um número: '))
totd = 0
for c in range(1, n+1):
    if n % c == 0:
        totd += 1
if totd == 2:
    print('{} É um número primo!\nFoi dividido apenas {} vezes'.format(n, totd))
else:
    print('{} não é um número primo!\nFoi dividisível {} vezes'.format(n, totd))