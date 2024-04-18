#importações
import suporte
from random import randint


#programa principal

while True:
    escolha = suporte.menu()

    if escolha == 0:
        suporte.fim()

    if escolha == 1:
        print("Registre-se: ")
        no = input("Qual seu nome? \n").title()
        ida= randint(1,1000)

        professor = suporte.Prof(ida,no)
        
        print(professor.professores())


#teste aleatório


