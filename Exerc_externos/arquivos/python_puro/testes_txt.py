#primeiros testes com arquivo text:

arquivo = open("arquivo.txt", "r") # abrir arquivo txt ("r" de read)-Modo Leitura

print(arquivo.read(12)) # ler arquivo .txt (parametro numerico limitando o n°caracteres apresentados)
print(arquivo.tell()) # conta caracteres (retonra número)
print(arquivo.seek(0,0)) # apos leitura cursor fica no final (seek e coor. volta o cursor para o inicio)

arquivo.close() # Fechando arquivo para não haver erros, pode ocorrer se permanecer aberto



arquivo = open("arquivo.txt", "w") # abrir arquivo txt ("w" de write)-Modo Escrita
arquivo.close() # Fechando arquivo para não haver erros, pode ocorrer se permanecer aberto

arquivo = open("arquivo.txt", "a") # abrir arquivo txt ("a" de append)-Modo Acrescentar
arquivo.close() # Fechando arquivo para não haver erros, pode ocorrer se permanecer aberto