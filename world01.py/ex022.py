#mostra o nome em letras maiúsculas ,minusculas n de caracteres no nome sem espaços e n de caracteres no primeiro nome 
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


