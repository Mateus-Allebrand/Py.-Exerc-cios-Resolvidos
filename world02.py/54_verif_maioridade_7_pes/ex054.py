#Leia o ano de nascimento de 7 pessoas e verifique quem já atingiu a maior idade:

#Programa principal
ano = int(input('digite o ano atual: '))
tot = 0
for c in range(0,7):
     nasc = int(input('Digite o ano de seu nascimento: '))
     if (ano - nasc) < 21:
        tot += 1
     elif (ano - nasc) >= 21:
        tot += 0
print('{} é o número de pessoas que ainda não atingiram a maior idade'.format(tot))