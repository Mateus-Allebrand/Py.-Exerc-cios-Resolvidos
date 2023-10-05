#Crie um programa que leia nome, ano de nascimento e carteira de trabalho,
# caso a pessoa tenha carteira de trabalho , também armazene a data de contratação e o salario
#acrescente com quantos anos a pessoa vai se aposentar

ano_atual = 0
aposenta = 36
dados = {'nome':'','idade': 0,'ctps': 999, 'contratação': 0, 'salario': 0,'aposentadoria': 0 }
print('*** Caso não tenha algum itém ***\n          [Digite [0]]')
ano_atual = int(input('Ano atual: '))
dados['nome'] = str(input('\nNome: ')).title()
nascimento = int(input('\nAno de nascimento: '))
idade = ano_atual - nascimento
dados['idade'] = idade 
dados['ctps'] = int(input('\nN° CTPS: '))
if dados['ctps'] == 0:
    print(f'\n{dados["nome"]} tem {dados["idade"]} anos e não tem CTPS')
else:
    dados["contratação"] = int(input('\nAno de contratação: '))
    dados['salario'] = float(input('\nvalor salário: '))
    x= ano_atual - dados['contratação']
    falta = 36 - x
    dados['aposentadoria'] = dados['idade'] + falta
    print(f'\nNome: {dados["nome"]}')
    print(f'\nIdade: {dados["idade"]}')
    print(f'\nN° CTPS: {dados["ctps"]}')      
    print(f'\nAno contratação: {dados["contratação"]}')      
    print(f'\nSalário: {dados["salario"]}')      
    print(f'\nSe aposentará com {dados["aposentadoria"]} anos')      