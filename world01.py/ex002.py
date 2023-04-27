#second program
collors = {'preto':'\033[7;30m', 'limpa':'\033[m', 'branca': '\033[37m'}
nome=input('Qual o seu nome?')
print('É um prazer te conhecer {}{}{}!'.format(collors['branca'], nome, collors['limpa']))