#Crie um programa que crie uma matriz 3 x3 na tela
#e preencha com os valores lidos pelo teclado
#0 #  #  #
#1 #  #  #
#2 #  #  #
#  0  1  2

#a soma de todos os números pares
# a soma dos valores da terceira coluna
#o maior valor da segunda coluna

lista = [[0,0,0], [0,0,0],[0,0,0]]
npar = []
contp = 0
contt = 0
mai = []
maior = 0
n = 0
cnt = 0
for l in range(0,3):
    for c in range(0,3):
        n = int(input(f'Digite o númeor na posição: {(l),(c)} '))
        lista[l][c] = n
        if n % 2 == 0:
            npar.append(n)
            contp += n
        if c == 2:
            contt += n
        if c == 1:
           mai.append(n)
for d in mai:
    cnt += 1
    if cnt == 1:
        maior = d
    else:
        if d > maior:
            maior = d

print('\n')        
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]',end='')
    print()


print('\n')
print(f'O maior número da segunda coluna é: {maior}\n')
print(f'A soma dos números da terceira coluna é: {contt}\n')
print(f'Os números pares são: {npar}\nA soma dos números pares é: {contp}\n')
