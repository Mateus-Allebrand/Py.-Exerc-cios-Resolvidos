#classe test


class Livro():

    #função contrutor
    def __init__(self, titulo, isbn):

        self.titulo = titulo
        self.isbn = isbn
        print("Contrutor invocado para criar um objeto dessa classe")

    def imprime(self):
       print(f"Foi criado o livro: {self.titulo} com isbn: {self.isbn}")

    def get_titulo(Self):
        return Self.titulo
    
    def get_isbn(Self):
        return Self.isbn



livro1 = Livro("macados",985645858)


class Aluno():
    
    def __init__(self, nome, matricula, media):
        self.nome = nome
        self.matricula = matricula
        self.media = media

    def imprime(self):
        print(f"Nome: {self.nome.title()} \nMatricula: {self.matricula} \nMedia: {self.media} \n")

    def get_nome(self):
        return self.nome.title()
    
    def get_media(self):
        return self.media
    
    def get_matricula(self):
        return self.matricula
    

aluno01 = Aluno("mateus", 103, 9.5)

aluno02 = Aluno("leonidas", 300, 7.6)



print(getattr(aluno01, "matricula"))

setattr(aluno01, "matricula",213)

print(getattr(aluno01, "matricula"))