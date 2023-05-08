#medalha = emoji.emojize(":1st_place_medal:")
#detetive = emoji.emojize(":detective:")
#modtrsnfolingus = emoji.emojize(":face_with_tongue:")
##mostlingdoido= emoji.emojize(":zany_face:")


import random
import emoji
emoz = 2
contv = 1

print('==============================================================================\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=> VAMOS COMEÇAR! <=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n==============================================================================')
print('============================= TENTE ADIVINHAR! ===============================')
print('==============================================================================')
lista = [1,2,3,4,5]
nmaq = random.choice(lista)
npes = int(input('                        \n                        Qual número estou pensando? \n'))
if npes == nmaq:
    print('PARABÉNS!\nVocê Acertou em {} tentativa'.format(contv))
else:
    while nmaq != npes:
        print('Você Errou!\n\n')
        print('estava pensando no número {}\nTente outras vez!'.format(nmaq))
        nmaq = random.choice(lista)
        npes = int(input('                        \n                        Qual número estou pensando? \n'))
        contv += 1
    print('PARABÉNS!\nVocê Acertou em {} tentativas'.format(contv))
