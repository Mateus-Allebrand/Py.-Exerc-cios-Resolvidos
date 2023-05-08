#crie um programa que leia um produto e seu respectivo preço em uma unica tupla
#No final mostre a listagem de produtos organizando os dados em forma tabular
list = [] 

while True:
    prod = input('Digite o nome do produto: ')
    list.append(prod)
    valor = float(input('Digite o valor: '))
    list.append(valor)
    flag =input('Deseja continuar ?\n [[S/N]] ').upper()[0]
    if flag == 'N':
        break
    elif flag == 'S':
        print('\nCerto, vamos continuar !')
    while flag != 'N' and flag != 'S':
        print('Digito inválido: ')
        flag =input('Deseja continuar ?\n [[S/N]] ').upper()[0]
print('=' * 40)
print('     LISTA DE PRODUTOS' )
print('=' * 40)
for cont in range(0, len(list)):
    if cont % 2 == 0:
        print(f'{list[cont]:.<30}',end='')
    else:
        if cont % 2 == 1:
            print(f'R$ {list[cont]:>7.2f}',end='\n')

