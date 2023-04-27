#mostra  de uni dez cen mil
num = (input('Digite um número entre 0 e 9.999: '))
numalg = len(num)
if numalg == 1:
    print('unidade: {}'.format(num[0]))

elif numalg == 2:
    print('Unidade: {}\nDezena: {}'.format(num[1],num[0]))

elif numalg == 3:
    print('Unidade: {}\nDezena: {}\nCentena: {}'.format(num[2], num[1], num[0]))

elif numalg == 4:
    print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num[3], num[2], num[1], num[0]))

else:
    print('Você digitou um número invalido!\nTente outra vez.\nMas lembre-se que, é de 0 a 9.999')
    












































            

