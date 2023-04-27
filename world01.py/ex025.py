#procura nome
nome =input('Escreva o nome: ')
nome =nome.upper()
pal = 'Silva'
n = nome.find('SILVA')
if n != -1:
    print('O nome possui a palavra {}.'.format(pal))
else:
    print('Nome não possui a palavra {}.'.format(pal))