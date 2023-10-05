#crie um programa para ler varios números e colocar em uma lista
#crie outras 2 listas , uma com os números pares e outra com os números impares
#Ao final mostre as três listas

#Programa principal
import math
list = []
listp = []
listi = []
while True:
    n = int(input('Digite um número: '))
    list.append(n)
    x = input('Deseja inserir mais números? \n[S/N]?\n').upper()[0]
    while x not in 'NS':
        print('Reposta inválida! \n')
        x = input('Deseja inserir mais números? \n[S/N]?\n').upper()[0]
    if x == 'N':
        break
for c in list:
    if c % 2 == 0:
        listp.append(c)
    else:
        listi.append(c)
print(f'\nlista: {list} ', end='\n')        
if listp == []:
    print('\nNão tem nenhum número par na lista!\n') 
else:
    print(f'\nNúmeros Pares: {listp}\n', end= '\n')
if listi == []:
    print('\nNão tem nenhum número impar na lista!\n ')
else:
    print(f'\nNúmeros Impares: {listi} \n', end= '\n')

