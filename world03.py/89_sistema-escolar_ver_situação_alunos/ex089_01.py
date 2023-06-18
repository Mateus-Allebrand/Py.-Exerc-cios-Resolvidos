#codigos teste 
lista = [['julian', '0', '5'], ['ana', '10', '4']]

# vamos criar uma função de 'busca'




#Programa principal
def encontrar(elemento):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    for i in range (len(lista)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in lista[i][j]: # se encontrarmos elemento ('ana')
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                break # saímos do loop interno
            break # e do externo
    return (pos_i, pos_j) # e retornamos os índices


r = encontrar('ana') # chamamos a função e salvamos em r
print(r) # imprime índices
print(lista[r[0]][r[1]]) # usa índices na lista como prova