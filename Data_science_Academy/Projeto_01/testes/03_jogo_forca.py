# import emoji
# emoji.emojize(":face_with_crossed-out_eyes:")
# x =emoji.emojize(":worried_face:")
# emoji.emojize(":downcast_face_with_sweat:")

from modulos import grafico,limpa_tela, Hangman
from random import choice
from os import system, name





def game():
    limpa_tela()
    print("=-="*10)
    print("JOGO DA FORCA".center(30))
    print("=-="*10)
    
    print("Tente advinhar!".center(30))
    print("")

    #Definindo lista com todas as palavras possíveis
    palavras = ["policial", "bombeiro", "eletricista", "engenheiro", "caminhoneiro", "barbeiro", "pedreiro", "marceneiro", "corretor", "manobrista", "vendedor", "cozinheiro", "alfaiate", "cientista"," piloto", "açogueiro", "pintor", "programador", "professor", "advogado", "padeiro", "azulegista", "confeiteiro"]

    #escolha palavras de modo randomico
    palavra = choice(palavras)

    letras_desc = ['_' for letra in palavra]
    
    #chances
    chances = 6

    #letras erradas
    letras_erradas = []
    
    while chances > 0:
          
        print(grafico(chances))
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
        print(grafico(0))



#Bloco main
if __name__ == "__main__":
    game()



