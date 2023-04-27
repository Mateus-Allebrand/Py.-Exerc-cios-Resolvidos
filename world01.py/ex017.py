#calcular hipotenusa
from math import hypot
ca = float(input('Qual o valor do cateto oposto? '))
co = float(input('Qual o valor do cateto adjacente? '))
hipo = hypot(ca,co)
print(hipo)
