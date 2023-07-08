# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
from random import choice
from os import system, name



#Classe
class Hangman:

	# Método Construtor
     def __init__(self):
          print("inicializado com sucesso!")

	# Método para adivinhar a letra
     def advinhar(self,palavra,letra):
          self.letra = letra
          self.palavra = palavra
          if letra in palavra:
               return letra

	# Método para verificar se o jogo terminou
     def verifica_final(self,num):
          self.tent = num
          
         
	# Método para verificar se o jogador venceu
		
	# Método para não mostrar a letra no board
		
	# Método para checar o status do game e imprimir o board na tela







# Funçao para limpar tela após cada execução
def limpa_tela():

    #windowns
    if name == 'nt': #'nt' é o nome interno do windowns
        _ = system('cls') #comando para limpar tela no windowns 
        #Obs. _= é pq a função system retona algo. Estou jogando esse retorno para o (_)
    #Mac ou linux
    else:
        _= system('clear')  #comando para limpar tela no Mac ou linux








def grafico(chances):
    estagio = [" ||=======|                                                                                                                                    ||       |                                                                                                                                    ||       O                                                                                                                                    ||      /|\                                                                                                                                   ||      / \                                                                                                                                   ||                                                                                                                                         ___||____________", " ||=======|                                                                                                                                    ||       |                                                                                                                                    ||       O                                                                                                                                    ||      /|\                                                                                                                                   ||      /                                                                                                                                     ||                                                                                                                                         ___||____________",  " ||=======|                                                                                                                                    ||       |                                                                                                                                    ||       O                                                                                                                                    ||      /|\                                                                                                                                   ||                                                                                                                                            ||                                                                                                                                         ___||____________", " ||=======|                                                                                                                                    ||       |                                                                                                                                    ||       O                                                                                                                                    ||      /|                                                                                                                                    ||                                                                                                                                            ||                                                                                                                                         ___||____________", " ||=======|                                                                                                                                    ||       |                                                                                                                                    ||       O                                                                                                                                    ||       |                                                                                                                                    ||                                                                                                                                            ||                                                                                                                                         ___||____________",  " ||=======|                                                                                                                                    ||       |                                                                                                                                    ||       O                                                                                                                                    ||                                                                                                                                            ||                                                                                                                                            ||                                                                                                                                         ___||____________", " ||=======|                                                                                                                                    ||       |                                                                                                                                    ||                                                                                                                                            ||                                                                                                                                            ||                                                                                                                                            ||                                                                                                                                         ___||____________"]

    return estagio[chances]

