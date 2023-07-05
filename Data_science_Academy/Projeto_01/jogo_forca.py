from random import choice

#Definindo lista com todas as palavras possíveis
possible_words = ["laranja", "abacate", "calabresa", "pizza", 'churrasco', 'manteiga', 'queijo', 'alface', 'legumes', 'cenora', 'espinafre', 'tomate', 'cebola']

#lista vazia para receber letras adivinhadas
empty_list = []

#número maximo de tentativas = 
nu_tentativas = 6
cont_tentativas = 0

#Escolher uma palavra aleatória da lista
chosen_word = choice(possible_words)

while cont_tentativas < nu_tentativas:
    cont_tentativas += 1
    print(cont_tentativas)