#Crie um programa que leia varios números
#mostre quantos números foram digitados
#lista de valores ordenado em forma decrescente
#Se o valor 5 foi digitado, esta na lsita ou não


#Programa Pricipal
list = []
cont = 0
while True:
    n = int(input('Digite um número: '))
    cont += 1
    list.append(n)
    x = input('Deseja continuar? [S/N]').upper()[0]
    while x not in 'NS':
        x = input('Digito invalido!\nDeseja continuar? [S/N]').upper()[0]
    if x in 'N':
        break   
list.sort(reverse=True)
if 5 in list:
    c = list.count(5)
    print(f'\nO número 5 apareceu {c} vezes\n')
else:
    print('\nO número 5 não esta na lista\n')
print(list)
print(f'\nForam digitados {cont} números')
        
