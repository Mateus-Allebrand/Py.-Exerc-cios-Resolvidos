#testes funçao filter

par = lambda x: True if (x % 2 == 0) else False



lista = [1,5,12,3,5,46,15,12,32,56,48,78,56,123,45,78,54,62]


print(list(filter(par,lista)))

lista2 = list(filter(par,lista))
print(lista2)


lista3 = [1,5,12,48,78,56,123,45,78,54,62]

print(list(filter(lambda x: x % 2 == 0,lista3)))