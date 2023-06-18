# crie uma tupla com varias palavras , depois mostrar para cada palavras quais são seus acentos

#Programa principal
itens = ('casa','petroleo', 'casca', 'cuia', 'frigideira','bateria')
lista = []
for c in range(0, len(itens)):
    va = itens[c].count('a')
    ve = itens[c].count('e')
    vi = itens[c].count('i')
    vo = itens[c].count('o')
    vu = itens[c].count('u')
    if va > 0:
        lista.append('A')
    if ve > 0:
        lista.append('E')
    if vi > 0:
        lista.append('I')
    if vo > 0:
        lista.append('O')
    if vu > 0:
        lista.append('U')
    if lista != '':
        print(f'A palavra {itens[c]} tem as vogais {lista}')
        lista = []
    
