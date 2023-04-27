#leia 3 número e beja qual é o maior e qual é o menor e mostre na tela

a =int(input('Enter a number: '))
b =int(input('Enter a number: '))
c =int(input('Enter a number: '))
maior = a
menor = a

if (a > b) and a > c:
    maior = a
if (b > a) and b > c:
    maior = b
if (c > b) and c > a:
    maior = c
#
if (a < b) and a < c:
    menor = a
if (b < a) and b < c:
    menor = b
if (c < b) and c < a:
    menor = c
if (a == b) or a == c:
    print('you entered more than once the number {}'.format(a))
if b == c:
    print('you entered more than once the number {}'.format(b))
print('maior',maior)
print('menor',menor)
