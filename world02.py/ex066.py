#Crie u, programa que leia varios números inteiros pelo teclado
#programa só para quando o usauário digitar 999
#No final mostre quantos números foram digitados 
# e mostre qual a soma entre eles
#AGORA UTILIZEI O BREAK 
fl = 999
s = n = 0
cont = 0

while n != fl:
    n= int(input('Digite um número: '))
    cont += 1
    if n == fl:
        break
    s += n
print(f'O valor dos {cont - 1} números digitados foi {s}')