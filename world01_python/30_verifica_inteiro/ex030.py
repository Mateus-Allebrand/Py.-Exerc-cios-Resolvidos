#veridfica se número é inteiro

#Programa principal
num =int(input('Enter the number integer: '))
if (num % 2) == 0:
    print('The number entered is an integer')
else: 
    print('The number entered is a decimal')