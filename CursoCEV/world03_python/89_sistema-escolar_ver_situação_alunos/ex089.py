#crie um programa que leia o nome e duas notas de varios alunos
#Guarde tudo em uma lista composta
#no final mostre o nome e a média de cada aluno e permita que o usuário possa mostrar individualmente as notas de cada aluno

import math
dadosind =list()
geral = []
cont = 0
print('='*30)
print('     CADASTRANDO ALUNOS'   )
print('='*30)
while True:
    cont += 1
    nome = input('Nome: ').upper()
    dadosind.append(nome)
    nota1 = float(input('Nota[1]: '))
    dadosind.append(nota1)
    nota2 = float(input('Nota[2]: '))
    dadosind.append(nota2)
    m = (nota1 + nota2) / 2
    dadosind.append(m)
    geral.append(dadosind[:])
    dadosind.clear()
    x = str(input(f'Deseja inserir outro aluno?\n [S/N]')).upper()[0]
    while x not in 'SN':
        x = str(input(f'Deseja inserir outro aluno?\n [S/N]')).upper()[0]
    if x == 'N':
        break
geral.sort()
while True:
    print(f'\nNÚMERO DE ALUNOS CADASTRADOS: {cont}\n\n')
    t = str(input('Deseja ver todos os alunos cadastrados? [S/N]')).upper()[0]
    if t == 'S':
        for m in geral:
            print(f'=============================\nNome: {m[0]}\n\nMédia: {m[3]}\n\n=============================')
    s = str(input('\nDeseja pesquisar um em particular? [S/N] ')).upper()[0]
    if s =='N':
        break
    if s == 'S':
        aluno = str(input('Digite o nome: ')).upper()
        for i in geral:
            loc = geral.index(i)
            for c in i:
                if c == aluno:
                    loc2 = geral[loc].index(c)
                    print(f'\nNome: {geral[loc][loc2]}\n\nMédia: {geral[loc][loc2+3]}')#a
                    break
                               
    s = str(input('\nContinuar? [S/N] ')).upper()[0]
    if s =='N':
        print('========= FIM =========')
        break

         
        