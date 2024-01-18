#Programa calcula duas notas de uma aluno que foi passado pelo usuário e gera uma mensagem formatada mostrando a média.


while True:
    notas =[]
    nome=input("Olá,\nDigite seu nome:").title()
    print(f"Seja bem vindo {nome}!")
    while True:
        acesso = input("Você é professor: [S-SIM/N-Não]\n \n").upper()
        if acesso not in "SN":
            acesso=input("Resposta Incorreta!")
            continue

        if acesso in "S":
            print(f"Seja bem vindo Professor {nome}!\n")
            menuprof = int(input("======== Opções =========\n\n  [1] lançar Notas \n\n  [2] Vizualizar Notas \n\n  [0] Sair"))
            if menuprof == 1:
                aluno = []
                nomealuno= input("qual nome do aluno?\n").title()
                aluno.append(nomealuno)
                cont = int(input("Quantas notas serão lançadas? \n"))
                co=0
                for c in range(0,cont):
                    co+=1
                    nx = float(input(f"Digite nota número {co}\n"))
                    aluno.append(nx)
                somanota = 0
                for d in aluno[1:]:
                    somanota += d
                
                media = somanota/cont
                aluno.append(media)
                notas.append(aluno)

            if menuprof == 2:
                print(notas)
                
            if menuprof == 0:
                print("\n\n     ==== Finalizando ====        \n\n")
                break
        if acesso in "N":
            idaluno= input(f"seja bem vindo {nome}!\nDigite seu id de aluno: ")
            print(idaluno)
            break
                 
        
         