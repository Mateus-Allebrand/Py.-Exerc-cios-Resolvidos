#Jogo da Forca

#Bibliotecas
from random import choice
from os import system, name
from modulo import limpa_tela, status





class Hangman():

    def __init__(self,palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_acertadas = []
               
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_acertadas:
            self.letras_acertadas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)

        else:
            return False
        return True
    
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)

    def hangman_won(self):
        if "_" not in self.hide_palavra():
            return True
        return False
    
    def hide_palavra(self):

        rtn = ""

        for letra in self.palavra:
            if letra not in self.letras_acertadas:
                rtn += "_"
            else:
                rtn += letra

        return rtn
    
    def print_game_status(self):

        print(status(len(self.letras_erradas)))

        print(f"\nPalavra: {self.hide_palavra()}")

        print(f"\nLetras erradas: ")
        for letra in self.letras_erradas:
            print(letra, )

        print()

        print("Letras corretas: \n")
        for letra in self.letras_acertadas:
            print(letra, )

def rand_palavra():
    #lista com palavras 
    palavras = ["policial", "bombeiro", "eletricista", "engenheiro", "caminhoneiro", "barbeiro", "pedreiro", "marceneiro", "corretor", "manobrista", "vendedor", "cozinheiro", "alfaiate", "cientista"," piloto", "açogueiro", "pintor", "programador", "professor", "advogado", "padeiro", "azulegista", "confeiteiro"]
    return choice(palavras)


def main():

    limpa_tela()

    game = Hangman(rand_palavra())

    while not game.hangman_over():

        game.print_game_status()

        user_input = input("Digite uma letra: ")

        game.guess(user_input)

    game.print_game_status()
    
    if game.hangman_won():
        print("Parabéns! Você ganhou! ")

    else:
        print("Game over! Você perdeu:")
        print(f"A palavra era: {game.palavra}")

if __name__ == "__main__":
    main()