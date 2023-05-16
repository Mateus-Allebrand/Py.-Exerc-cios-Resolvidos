#Programa lê um número real mas mostra como saída apenas o valor inteiro.

#Programa principal
import math
n = float(input('Digite um número real: '))
nint = math.trunc(n)
print(nint)