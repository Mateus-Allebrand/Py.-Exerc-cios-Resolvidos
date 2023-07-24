#Funções

#Função linha dupla
def rowdoble():
    return "=="*30


def tabelaservcabelo(n):
    servalores = [{"Corte": 30},
                  {"Definitiva": 200},
                  {"Progressiova": 150},
                  {"Mechas": 120},
                  {"Sair": 'Break'},
                  ]
    return servalores[n]

def tabelaservunhas(n):
    servalores = [{"Mão": 15},
                  {"Pé": 25},
                  {"Mão e Pé": 35},
                  {"Sair": 'Break'},
                  ]
    return servalores[n]


def tiposerv():
    listaserviços = []
    while True:
        print(rowdoble())
        print("TIPO SERVIÇO:".center(60))
        print(rowdoble())
        op = int(input("[[1]] Cabelo; \n\n[[2]] Sombrancelha; \n\n[[3]] Unha; \n\n[[0]] sair;" ))
        while op not in range(0,4):
            print("\nOpção inválida! \n\n")
            op = int(input("[[1]] Cabelo; \n\n[[2]] Sombrancelha; \n\n[[3]] Unha; \n\n[[0]] sair;" ))
        if op == 1:
            print(rowdoble())
            print("TIPO SERVIÇO PARA CABELO:".center(60))
            print(rowdoble())

            ops = int(input("[[1]] Corte; \n\n[[2]] Definitiva; \n\n[[3]] Mechas; \n\n[[4]] Progressiva; \n\n[[0]] sair;" ))
            while ops not in range(0,5):
                print("\nOpção inválida! \n\n")
                ops = int(input("[[1]] Corte; \n\n[[2]] Definitiva; \n\n[[3]] Mechas; \n\n[[4]] Progressiva; \n\n[[0]] sair;" ))

                if  ops == 1:
                    listaserviços.append(tabelaservcabelo(ops))
                if  ops == 2:
                    listaserviços.append(tabelaservcabelo(ops))
                if  ops == 3:
                    listaserviços.append(tabelaservcabelo(ops))
                if  ops == 4:
                    listaserviços.append(tabelaservcabelo(ops))
                if  ops == 0:
                    break
            
        if op == 2:
            print(rowdoble())
            print("TIPO SERVIÇO PARA UNHAS:".center(60))
            print(rowdoble())

            ops = int(input("[[1]] Mão; \n\n[[2]] Pé; \n\n[[3]] Mão e Pé; \n\n[[0]] sair;" ))
            while ops not in range(0,4):
                print("\nOpção inválida! \n\n")
                ops = int(input("[[1]] Mão; \n\n[[2]] Pé; \n\n[[3]] Mão e Pé; \n\n[[0]] sair;" ))

                if  ops == 1:
                    listaserviços.append(tabelaservcabelo(ops))
                if  ops == 2:
                    listaserviços.append(tabelaservcabelo(ops))
                if  ops == 3:
                    listaserviços.append(tabelaservcabelo(ops))
                if  ops == 4:
                    listaserviços.append(tabelaservcabelo(ops))
                if  ops == 0:
                    break
    return listaserviços