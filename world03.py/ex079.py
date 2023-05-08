#Crie um programa que possa ler varios números pelo teclado, a vá adicionando em uma lista
#caso o número já exista dentro da lista ele não será adcionado
#no final mostre em ordem crescente os valores dentro da lista

list = []

while True:
    n = int(input('digite um número: '))
    if n not in list:
        list.append(n)
    x = input('Deseja acrencentar outro número?\n [[S / N]]?\n  ').upper()[0]
    if x == 'N':
        break
    while 'S' not in x:
        x = input('RESPOSTA INVÁLIDA!\nDeseja acrencentar outro número?\n [[S / N]]?\n  ').upper()[0]   
list.sort() 
print(list)
