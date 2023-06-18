#Faça um programa que leia 5 números e os guarde em uma lista
#Depois faça o programa dizer qual foi o maior e o menor e suas respectivas posições


#Programa principal
list = []

for l in range(0,5):
    list.append(int(input('Digite um número: ')))
print(f'O maior número na lista é {max(list)} e está localizado na {list.index(max(list)) + 1 }° posição')
print(f'O menor número na lista é {min(list)} e está localizado na {list.index(min(list)) + 1 }° posição')
