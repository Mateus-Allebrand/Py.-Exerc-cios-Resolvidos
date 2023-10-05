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

    letras_desc = ['_' for letra in palavra]
    
    #Número de chances
    chances = 6

    #letras erradas
    letras_erradas = []
    
    while chances > 0:

        #Imprime
        print(" ".join(letras_desc))
        print("")
        print("Chances Restantes: {}".format(chances))
        print("Letras Erradas:"," ".join(letras_erradas))
    
        
        #Tentativas
        tentativa = input("Digite uma letra: ").lower()
        print("")
        
        #condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_desc[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_desc:
            print("=-"*15)
            print("VOCÊ VENCEU!".center(30))
            print("=-"*15)
            break

    if "_" in letras_desc:
        print(f"VOCÊ PERDEU! \nA apalavra era: {palavra}")



#Bloco main
if __name__ == "__main__":
    game()

