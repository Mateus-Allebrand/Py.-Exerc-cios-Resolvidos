#faça um programa que leia o nome e média de um aluno, e situação desse aluno
# no final mostre o conteúdo da estrutura na tela

aluno = dict()

aluno['nome'] = str(input('Nome do aluno: ')).title()
aluno['nota'] = float(input(f'Digite a nota de {aluno["nome"]}: '))
if aluno['nota'] >= 7:
    aluno['situação'] = 'aprovado'.title()
elif aluno['nota'] < 7 and aluno['nota'] >= 4:
    aluno['situação'] = 'recuperação'.title()
else:
    aluno['situação'] = 'reprovado'.title()
print(f'O aluno {aluno["nome"]} tirou nota {aluno["nota"]}, sua situação é de {aluno["situação"]}')
