#Teste para anotar valores e serviços
from functions import rowdoble


while True:
    print("Olá,\n")
    print(rowdoble())
    print("MENU DE OPÇÕES: ".center(60))
    print(rowdoble())
    op = int(input(f"\n[[1]] Novo serviço: \n\n[[2]] Vizualizar serviços realizados hoje: \n\n[[0]] Sair: \n\n{rowdoble()}\n"))

    #Funcionando
    while op not in range(0,3):
        print("'OP' Inválida!")
        op = int(input(f"\n[[1]] Novo serviço: \n\n[[2]] Vizualizar serviços realizados hoje: \n\n[[0]] Sair: \n\n{rowdoble()}\n"))

    #Funcionando
    if op == 1:
        print("op 1 selecionada")
    if op == 2:
        print("op 2 selecionada")
    if op == 0:
        print("good bye")
    
    
    break