from arquivo import lerarquivo
from arquivo import leiaint
from arquivo import cadastrar


def menu():
    arq ='db.txt'
    cadastro = list()
    while True:
        print('=' * 40)
        print('MENU PRINCIPAL'.center(40))
        print('=' * 40)
        print('[1] Ver pessoas cadastradas\n[2] Cadastrar nova pessoa\n[3] Sair do sistema')
        print('_' * 40)
        resp = input('Digite sua opção:')
        while resp not in '123':
            print('ERRO! responda apenas com [1], [2] ou [3] ')
            resp = input('Digite sua opção:')
        if resp == '1':
            print('Pessoas Cadastradas:'.center(40))
            print('_'*40)
            lerarquivo(arq)
        if resp == '2':
           print('NOVO CADASTRO:'.center(40))
           nome = str(input('Nome: ')).title()
           idade = leiaint(input('Idade: '))
           cadastrar(arq,nome,idade)
        if resp == '3':
            print()
            print('-='*20)
            print('FIM!'.center(40))
            print('-='*20)
            break







#########################################################################################################################
#op 1
#print('='*40)
#            print('CADASTRO'.center(40))
#            print('-'*40)
#           for i,j in enumerate(cadastro):
#               print(f'{i + 1:}°   Nome: {j["nome"]:<10}  \tIdade: {j["idade"]}')   
#           print('='*40)
#########################################################################################################################
 #op2
 #id = dict()
 #           n = input('Nome: ').title()
 #           id['nome'] = n
 #           anos = int(input('Idade: '))
#          id['idade'] = anos
#          cadastro.append(id.copy()) 
#          id.clear()
#########################################################################################################################