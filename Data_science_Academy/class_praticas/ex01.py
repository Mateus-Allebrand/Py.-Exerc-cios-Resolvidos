#classe test


class Livro():

    #função contrutor
    def __init__(self):

        self.titulo = "sapiens-uma breve historia da humanidade"
        self.isbn = 982595714
        print("Contrutor invocado para criar um objeto dessa classe")

    def imprime(self):
       print("Foi criado o livro: %s com isbn: %d " %(self.titulo,self.isbn))