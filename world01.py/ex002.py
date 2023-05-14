#programa consiste em uma mensagem (qual seu nome?) que aguarda uma entrada de dados do usuário, e retorna a ele com uma mensagem de boas vindas. Adcionei cores padrão Ansi.


#Programa principal
collors = {'preto':'\033[7;30m', 'limpa':'\033[m', 'branca': '\033[37m'}
nome=input('Qual o seu nome?')
print('É um prazer te conhecer {}{}{}!'.format(collors['branca'], nome, collors['limpa']))