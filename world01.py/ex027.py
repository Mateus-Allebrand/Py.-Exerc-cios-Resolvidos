#procura o primeiro e o ultimo nome
nome = input('Digite o seu nome: ')
nome = nome.upper()
nospl = nome.split()
firstn = nospl[0]
las = nome.rfind(' ')
lastn = nome[las: ]
lastn = lastn.lstrip()
print('O primeiro nome é {} e o ultimo é {}.'.format(firstn, lastn))