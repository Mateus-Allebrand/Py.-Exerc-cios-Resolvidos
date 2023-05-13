def menu():
    print('=' * 35)
    print('MENU PRINCIPAL'.center(35))
    print('=' * 35)
    resp =print('[1] Ver pessoas cadastradas\n[2] Cadastrar nova pessoa\n[3] Sair do sistema')
    print('_' * 35)
    opc = int(input('Digite sua opção:'))


    return opc


print(menu())
