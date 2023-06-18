#Programa lê nome do usuário e mostra o nome em letras maiúsculas, minusculas, diz o número de caracteres no nome sem os espaços e informa também o número de caracteres no primeiro nome.


#Programa principal.
nome = input('Digite o seu nome completo: ')
nome1 = nome.upper()
nome2 =nome.lower()
vaz = nome.count(' ')
tam = len(nome)
tamr = tam - vaz
prim = nome.split()
primt = len(prim[0])
print(nome)
print(nome2)
print(tamr)
print(primt)


