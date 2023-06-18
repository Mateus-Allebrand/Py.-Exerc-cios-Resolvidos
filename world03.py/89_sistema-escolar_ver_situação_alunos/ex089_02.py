#codigo test 2
lista = [['julian', '0', '5'], ['ana', '10', '4'], ['10', 'ana', '4']]

def encontrar(elemento):
    lista_pos = [] # vamos salvar nesta nova lista
    for i in range (len(lista)):
        for j in range (i):
            if elemento in lista[i][j]:
                lista_pos.append((i, j)) # aqui adicionamos cada índice na lista
    return lista_pos # removemos os breaks, pois precisamos procurar na lista inteira

r = encontrar('ana')
print(r)
# o próximo print só funciona buscando por 'ana', pois ele espera que
# o retorno seja pelo menos dois elementos
print(lista[r[0][0]][r[0][1]], lista[r[1][0]][r[1][1]])