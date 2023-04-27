#crie um programa que leia nome e preço de produtos
#pergunte se o usuário vai continuar a registrar produtos
#A Qual total gasto na compra
#B Quantos produtos são mais caros do que mil reais 
# qual o nome do produto mais barato
contmil = 0
nomebarato = ''
valorbarato = 0
conttot = 0
cont = 0
while True:
    prod = input('Digite nome do produto: ')
    valor = float(input('\nDigite o valor: '))
    resp = input('\nDeseja continuar resgitrando produtos? [[S/N]] ?\n').upper()[0]
    conttot += valor
    cont += 1
    while resp not in 'NS':
        resp = input('\nDeseja continuar resgitrando produtos? [[S/N]] ?\n').upper()[0]
    if valor > 1000:
        contmil += 1
    if cont == 1:
        nomebarato = prod
        valorbarato = valor
    if valor < valorbarato:
        nomebarato = prod
        valorbarato = valor
    if resp == 'N':
        break
print(f'Valor total compras: {conttot}')
print(f'Total de produtos com valores maiores que R$ 1.000,00: {contmil}')
print(f'O produto mais barato é: {nomebarato}')