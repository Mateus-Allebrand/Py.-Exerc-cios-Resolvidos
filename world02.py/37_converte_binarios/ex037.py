# convertedor de bases binaria octal e hexadecimal

#Programa principal
num = int(input('Enter a number:'))
base =int(input('choose conversion base:\nType 1 for binary;\nType 2 for octadecimal;\nType 3 for hexadecimal: \nType chosen option:\n'))
if base == 1:
    print('You chose binary base!\nThe number {} in binary equals {} '.format(num, bin(num)))
elif base == 2:
    print('You chose octal base!\nThe number {} in octal equals {}'.format(num, oct(num)))
elif base == 3:
    print('You chose hexadecimal base!,\nThe number {} in hexadecimal equals {}'.format(num, hex(num))) 
else:
    print('You entered an invaled option!') 
