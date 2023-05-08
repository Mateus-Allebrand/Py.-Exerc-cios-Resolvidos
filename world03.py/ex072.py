#digite uma tupla com númeos de 0 a 20 escrito extenso, ao usuario digitar digitar o número
#ele aparece na tela por extenso

num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

n = int(input('Digite um número:\n '))
while True:
    if n > 20 or n < 0:
        n = int(input('Digito inválido!\n\nDigite um número:\n '))
    else:
        if n < 0 or n > 20:
            n = int(input('Digito inválido! Digite um número '))
            
        if n == 0:
            print(num[0])
            break
        elif n == 1:
            print(num[1])
            break
        elif n == 2:
            print(num[2])
            break
        elif n == 3:
            print(num[3])
            break
        elif n == 4:
            print(num[4])
            break
        elif n == 5:
            print(num[5])
            break
        elif n == 6:
            print(num[6])
            break
        elif n == 7:
            print(num[7])
            break
        elif n == 8:
            print(num[8])
            break
        elif n == 9:
            print(num[9])
            break
        elif n == 10:
            print(num[10])
            break
        elif n == 11:
            print(num[11])
            break
        elif n == 12:
            print(num[12])
            break
        elif n == 13:
            print(num[13])
            break
        elif n == 14:
            print(num[14])
            break
        elif n == 15:
            print(num[15])
            break
        elif num == 16:
            print(num[16])
            break
        elif n == 17:
            print(num[17])
            break
        elif n == 18:
            print(num[18])
            break
        elif n == 19:
            print(num[19])
            break
        elif n == 20:
            print(num[20])
            break
    
    