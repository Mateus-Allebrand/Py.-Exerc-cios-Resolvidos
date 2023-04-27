#crie um programa que leia o nome, idade e sexo de 4 pessoas
#qual a media da idade
#qual nome do homem mais velho
#quantas mulheres tem menos de 20 anos

# variaveis
s = 0
medidade = 0
nomehom = ''
maisvelho = 0
contmu = 0
#repestições
for c in range(1,5):
    print('=-=-=-=-=-=-=-=-=-=-=-=\n{}° pessoa\n'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]?'))
    s += idade
    if c == 1 and sexo in 'Mm':
        nomehom = nome
        maisvelho = idade
    if sexo in 'Mm' and idade > maisvelho:
        nomehom = nome
        maisvelho = idade
    if sexo in 'Ff' and idade < 20:
        contmu += 1
medidade = s / c
print('A idade média entre os participantes da pesquisa é {}'.format(medidade))
print('O homem mais velhor tem {} e se chama {}'.format(maisvelho,nomehom))
print('O número de mulheres que tem menos de 20 anos é {}'.format(contmu))