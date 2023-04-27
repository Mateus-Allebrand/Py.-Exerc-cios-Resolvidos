#faça um programa que leia o sexo de uma pessoa e ssó aceite o valor 'm' ou 'f', se for digitado um valor diferente solicite que digite novamente.
tipsex = ''
nome = input('Digite seu nome: ')
sexo = input('Digite seu sexo: [M/F] ').upper()
while sexo != 'M' and sexo != 'F':
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: [M/F] ').upper()
if sexo == 'M':
        tipsex = 'Olá senhor {}'.format(nome)
if sexo == 'F':
        tipsex = 'Olá senhora {}'.format(nome)
print(tipsex)