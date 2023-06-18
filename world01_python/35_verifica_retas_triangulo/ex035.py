#verifica a possibilidade de fazer um triângulo

#Programa principal
a =int(input('Enter the size of the first straight: '))
b =int(input('Enter the size of the second straight: '))
c =int(input('Enter the size of the third straight: '))
ab = a + b 
ac = a + c
bc = b + c
if ab > c:
    print('Can form a triangle')
if ac > b:
    print('Can form a triangle')
if bc > a:
     print('Can form a triangle')   
else:
    print("Can't form a triangle")