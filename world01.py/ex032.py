#Para saber se um ano será bissexto, basta que ele seja divisível por 4. O ano de 2020, por exemplo, é divisível por 4, logo, é bissexto. Mas, para anos centenários (1900, por exemplo) a regra é que ele seja divisível por 400
#De 4 em 4 anos é ano bissexto.
#De 100 em 100 anos não é ano bissexto.
#De 400 em 400 anos é ano bissexto.
#Prevalecem as últimas regras sobre as primeiras.
ano = int(input('Write the year: '))
if ano % 4 == 0:
    print("It's a leap year!")
elif ano % 400 == 0:
    print("It's a leap year!")
elif ano %  100 == 0:
    print("It's a leap year!")
else:
    print("It's not a leap year!")