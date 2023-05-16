#Programa lê um nome de cidade de diz se o nome da cidade tem a palavra "SANTO" no inicio do nome.


#Programa principal.
cidade = input('Digite o nome da sua cidade: ')
cidade = cidade.upper()
n = cidade.find('SANTO')
ininome = cidade.split()
if n == 0:
    print('O nome de sua cidade começa com a palavra {}'.format(ininome[0]))
else:
    print('O nome de sua cidade é {}'.format(cidade))