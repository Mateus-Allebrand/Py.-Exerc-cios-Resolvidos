from random import choice
from os import system, name


# Funçao para limpar tela após cada execução
def limpa_tela():

    #windowns
    if name == 'nt': #'nt' é o nome interno do windowns
        _ = system('cls') #comando para limpar tela no windowns 
        #Obs. _= é pq a função system retona algo. Estou jogando esse retorno para o (_)
    #Mac ou linux
    else:
        _= system('clear')  #comando para limpar tela no Mac ou linux



def game():
    limpa_tela()
    print("=-="*10)
    print("JOGO DA FORCA".center(30))
    print("=-="*10)
    
    print("Tente advinhar!".center(30))
    print("")

    #Definindo lista com todas as palavras possíveis
    palavras = ["laranja", "abacate", "calabresa", "pizza", 'churrasco', 'manteiga', 'queijo', 'alface', 'legumes', 'cenora', 'espinafre', 'tomate', 'cebola']

    #escolha palavras de modo randomico
    palavra = choice(palavras)

    n = len(palavra)

    print("_ " * n)
    print(palavra)
    print(n)
    

game()