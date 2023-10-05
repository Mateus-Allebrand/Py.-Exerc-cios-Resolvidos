#Funções

import datetime

#Função linha dupla
def rowdoble():
    return "=="*30


def cabelo(n):
    servalores = [0,{"Corte": 35},
                  {"Definitiva": 200},
                  {"Progressiova": 150},
                  {"Mechas": 120},
                  
                  ]
    return servalores[n]

def unhas(n):
    servalores = [0, {"Mão": 15},
                  {"Pé": 25},
                  {"Mão e Pé": 35},
                  ]
    return servalores[n]


def sombrancelha(n):
    servalores = [0,{"Rena": 25},
                  {"Fio a Fio": 350},
                  {"Tracional": 35},
                  
                  ]
    return servalores[n]


def tiposerv():
    listaserviços = []
    while True:
        print(rowdoble())
        print("TIPO SERVIÇO:".center(60))
        print(rowdoble())
        op = int(input(f"[[1]] Cabelo; \n\n[[2]] Sombrancelha; \n\n[[3]] Unha; \n\n[[0]] sair; \n\n{rowdoble()}\n" ))
        while op not in range(0,4):
            print("\nOpção inválida! \n\n")
            op = int(input(f"[[1]] Cabelo; \n\n[[2]] Sombrancelha; \n\n[[3]] Unha; \n\n[[0]] sair; \n\n{rowdoble()}\n" ))
        if op == 1:
            print(rowdoble())
            print("CABELO:".center(60))
            print(rowdoble())

            ops = int(input(f"[[1]] Corte; \n\n[[2]] Definitiva; \n\n[[3]] Mechas; \n\n[[4]] Progressiva; \n\n[[0]] sair; \n\n{rowdoble()}\n" ))
            while ops not in range(0,5):
                print("\nOpção inválida! \n\n")
                ops = int(input(f"[[1]] Corte; \n\n[[2]] Definitiva; \n\n[[3]] Mechas; \n\n[[4]] Progressiva; \n\n[[0]] sair; \n\n{rowdoble()}\n" ))

            if  ops == 1:
                listaserviços.append(cabelo(ops))
            if  ops == 2:
                listaserviços.append(cabelo(ops))
            if  ops == 3:
                listaserviços.append(cabelo(ops))
            if  ops == 4:
                listaserviços.append(cabelo(ops))
            if  ops == 0:
                break
            break
            
        

        if op == 2:
            print(rowdoble())
            print("SOMBRANCELHA: ".center(60))
            print(rowdoble())

            ops = int(input(f"[[1]] Rena; \n\n[[2]] Fio a Fio; \n\n[[3]] Tracional; \n\n[[0]] sair; \n\n{rowdoble()} \n" ))
            while ops not in range(0,4):
                print("\nOpção inválida! \n\n")
                ops = int(input(f"[[1]] Rena; \n\n[[2]] Fio a Fio; \n\n[[3]] Tracional; \n\n[[0]] sair; \n\n{rowdoble()} \n" ))

            if  ops == 1:
                listaserviços.append(sombrancelha(ops))
            if  ops == 2:
                listaserviços.append(sombrancelha(ops))
            if  ops == 3:
                listaserviços.append(sombrancelha(ops))
            if  ops == 4:
                listaserviços.append(sombrancelha(ops))
            if  ops == 0:
                break
            break

        if op == 3:
            print(rowdoble())
            print("UNHAS: ".center(60))
            print(rowdoble())

            ops = int(input(f"[[1]] Mão; \n\n[[2]] Pé; \n\n[[3]] Mão e Pé; \n\n[[0]] sair; \n\n{rowdoble()}\n" ))
            while ops not in range(0,4):
                print("\nOpção inválida! \n\n")
                ops = int(input(f"[[1]] Mão; \n\n[[2]] Pé; \n\n[[3]] Mão e Pé; \n\n[[0]] sair; \n\n{rowdoble()} \n" ))

            if  ops == 1:
                listaserviços.append(unhas(ops))
            if  ops == 2:
                listaserviços.append(unhas(ops))
            if  ops == 3:
                listaserviços.append(unhas(ops))
            if  ops == 4:
                listaserviços.append(unhas(ops))
            if  ops == 0:
                break
            break

        if op == 0:
            break
        break

    return listaserviços




