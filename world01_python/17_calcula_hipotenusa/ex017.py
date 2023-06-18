#Programa lê as medidas do cateto oposto e cateto adjacente, calcula o valor da hipotenusa e mostra o resultado para o usuário.


#Programa principal
from math import hypot
ca = float(input('Qual o valor do cateto oposto? '))
co = float(input('Qual o valor do cateto adjacente? '))
hipo = hypot(ca,co)
print(hipo)
