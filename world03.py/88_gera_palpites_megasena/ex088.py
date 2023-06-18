#Faça um programa que ajude um jogador da mega sena a criar palpites de seis números entre 1 e 60.
# O programa deve perguntar para o usuáro quantos jogos ele quer gerar

import random
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
temp = []
m = []
mega = []

while True:
    n = int(input('Quantos palpites você deseja? '))
    for c in range(0, n):
        mega.append(0)
        for l in range(0,6):
            num = random.choice(lista)
            temp.append(num)
            m.append(temp[:])
            temp.clear()
        mega[c] = m[:]
        m.clear()
    break
for d in range(0,n):
    print(f'Palpite n° {d +1}: {mega[d]}')



print(len(mega))
print(l)
print(c)