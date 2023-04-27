# verifique se a frase é um palindromo
frase = input('Digite uma frase: ')
e = frase.replace(' ' , '')
e = e.upper()
inv = e[::-1]
if e == inv:
    print(e)
    print(inv)
    print('É um palindromo')
else:
    print(e)
    print(inv)
    print('Não é um palindromo')


