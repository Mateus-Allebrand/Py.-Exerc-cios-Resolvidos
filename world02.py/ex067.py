
# faça um programa que leia um número e mostre sua tabuada de cada número digitado
# o programa deve para quando digitarem um número negativo

cont = 0
res = 0
n = int(input('Digite um número: '))
while n >= 0:
   for cont in range(0, 10 + 1): 
       res = cont * n
       print (f' {cont} X {n} = {res}')
       cont += 1
   n = int(input('Digite um número: '))
   
        
