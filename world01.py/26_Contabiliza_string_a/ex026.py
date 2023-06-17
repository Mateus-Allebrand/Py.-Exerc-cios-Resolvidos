#Objetivo do programa é contar a quantidade de 'a' presente na frase, assim como a posição em que ele se encontra.

#Programa Principal
n = input('Digite uma frase: ')
n = n.lower()
serc = 'a'
n1 = n.count(serc)
n2 = n.find(serc)
n3 = n.rfind(serc)

print(f"O n° de 'a' na frase é igual a {n1}")
print(f"O 'a' na primeira posição esta no indice de n° {n2}")
print(f"O 'a' na última posição esta no indice de n° {n3}")