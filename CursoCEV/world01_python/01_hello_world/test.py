#Programa calcula duas notas de uma aluno que foi passado pelo usuário e gera uma mensagem formatada mostrando a média.

import suporte

while True:
    notas =[]
    nome=input("Olá,\nDigite seu nome:").title()
    print(f"Seja bem vindo {nome}!")
    while True:
        acesso = input("Você é professor: [S-SIM/N-Não]\n \n").upper()
        if acesso not in "SN":
            acesso=input("Resposta Incorreta!")
            continue
        if acesso in "SN":
            print(f"Seja bem vindo Professor {nome}!\n")
            menuprof = int(input("======== Opções =========\n\n  [1] lançar Notas \n\n  [2] Vizualizar Notas "))
            if menuprof == 1:
                cont = int(input("Quantas notas serão lançadas? \n"))
                for c in range(0,cont):
                    co=0
                    nx = float(input(f"Digite nota número {co+1}\n"))
                
           
            