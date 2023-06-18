#Crie u, programa que leia varios números inteiros pelo teclado
#programa só para quando o usauário digitar 999
#No final mostre quantos números foram digitados 
# e mostre qual a soma entre eles


#Programa principal
fl = 999
n = 0
c = 0
d = 0
while n != fl:
    n = int(input('Digite um número inteiro: '))
    c = c + 1
    if n != fl:
       d += n
print('Você digitou {} vezes sendo o último digito a flag'.format(c))
print('A soma de todos os números digitados é {}'.format(d))
