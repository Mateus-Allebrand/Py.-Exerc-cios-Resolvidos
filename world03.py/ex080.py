#Crie um programa que leia 5 números e armazene em uma lista já na posição correta:
#não pode usar o sort(), e no final mostre a lista ordenada na tela

list = []
list2 = []
for l in range(0,5):
    x = int(input('Digite um número: '))
    list.append(x)
for c in range(0, len(list)):
    x = min(list)
    list.remove(x)
    list2.append(x)
print(f'\n\n{list2}')