#Programa pede uma entrada de uma dado para o usuário e retorna para ele os informações de tipo de dado, em relação ao que ele digitou.

#Programa principal
n = input('Digite algo:')
print(type(n))
print('É alfanuméreco?')
print(n.isalnum())
print('É numéreco?')
print(n.isnumeric())
print('É decimal?')
print(n.isdecimal())
print('É alfabético?')
print(n.isalpha())
