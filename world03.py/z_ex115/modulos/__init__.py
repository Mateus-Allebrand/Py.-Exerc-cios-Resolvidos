from arquivo import lerarquivo



def menu():
    arq ='ex15.txt'
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
        if resp == '3':
            print()
            print('-='*20)
            print('FIM!'.center(40))
            print('-='*20)
            break
        if resp == '2':
            id = dict()
            n = input('Nome: ').title()
            id['nome'] = n
            anos = int(input('Idade: '))
            id['idade'] = anos
            cadastro.append(id.copy())
            id.clear()
        if resp == '1':
            print('pessoas cadastradas')
            lerarquivo(arq)
        









#print('='*40)
#            print('CADASTRO'.center(40))
#            print('-'*40)
#           for i,j in enumerate(cadastro):
#               print(f'{i + 1:}°   Nome: {j["nome"]:<10}  \tIdade: {j["idade"]}')   
#           print('='*40)