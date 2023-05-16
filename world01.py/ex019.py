#Programa lê os nomes de 4 alunos e escolhe entre eles para apagar o quadro negro.


#Programa principal
import random
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo alunos: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')
lista = [n1,n2,n3,n4]
a = random.choice(lista)
print(a)