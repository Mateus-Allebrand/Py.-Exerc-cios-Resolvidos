# Faça um algoritimo que leia o nome de 5 professores e armazene na lista lst_professores
# cada professor recebera uma nota de 1 a 5 de 8 alunos
# Mostre o nome do professor e sua Nota 
# mostre a media de notas de cada professor
# mostre o professor com a nota mais alta e o professor com a media mais baixa

#Bibliotecas
from operator import itemgetter, attrgetter
from time import sleep

#variaveis
lst_professores = list()
nprof = list()
nome_nota = dict()
org = dict()
contnota = 0
media = 0
cont = 0
#Entrada de nomes -> professores
print("=="*40)
print("\033[1;32m=>\033[m \033[1;36mSEJA BEM VINDO!\033[m \033[1;32m<=\033[m".center(105))
print("--"*40)
for a in range(1,6):
    nome = input(f'\nDigite o nome do {a}° professor: ')
    lst_professores.append(nome.title())

#Recebendo notas
for b in lst_professores:
    print(f'\nDigite uma nota de [1] a [5] para o professor \033[1;32m{b}\033[m')
    contnota = 0
    media = 0
    
    for i in range(1,9):
        nota = int(input(f'{i}° aluno -> Nota:\n'))
        contnota += nota
        media = contnota / i
        print(f'Professor \033[1;32m{b}\033[m média até o momento \033[1;32m{media:.2f}\033[m')
        if i == 8:
            nprof.append(media)

#Apresentando média dos professores
print("=="*40)
print("\033[1;32m==\033[m \033[1;36mMÉDIA DOS PROFESSORES\033[m \033[1;32m==\033[m".center(105))
print("--"*40)
for c in range(0,5):
    sleep(1)
    print(f"Professor {lst_professores[c]:<50} Média {nprof[c]:^10.2f}")
    nome_nota[lst_professores[c]] = nprof[c]

#Organizando a lista em ordem descrescente para localizar a maior e a menor média
for d in sorted(nome_nota,key=nome_nota.get, reverse=True):
    org[d] = nome_nota[d]

#Apresentando as medias destaques 
print("=="*40)
print("\033[1;32m==\033[m \033[1;36m DESTAQUES \033[m \033[1;32m==\033[m".center(105))
print("--"*40)
for i,j in org.items():
    cont +=1
    if cont == 1:
        sleep(1)
        print(f"\n\033[1;32mMaior média = {j:<40.2f}  Professor -> {i:<10}\033[m")
    if cont == 5:
        sleep(1)
        print(f"\n\033[1;31mMenor média = {j:<40.2f}  Professor -> {i:<10}\033[m")

print("=="*40)



