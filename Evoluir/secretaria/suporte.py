#importações



def menu():
    x = ("=-="*20)
    print(x)
    print("Bem Vindo!".center(60))
    print(x) 
    while True:
        opcao = int(input(f"\n Escolha uma opção: \n\n [[1]] Sou professor; \n\n [[2]] Sou aluno; \n\n [[0]] Sair \n\n{x}\n\n"))
        if opcao<0 or opcao>2:
            print("Opção Inváida!\nTente outra Vez!\n")
            continue
        return opcao
    
def fim():
    x = ("=-="*20)
    print(x)
    print("== FIM! ==".center(60))
    print(x)

class Prof():

    def __init__(self,ide, nome):
        self.ide = ide
        self.nome = nome

    def professores(self):
        professorex = []
        professorex.append(self.ide)
        professorex.append(self.nome)
    
        return professorex

        