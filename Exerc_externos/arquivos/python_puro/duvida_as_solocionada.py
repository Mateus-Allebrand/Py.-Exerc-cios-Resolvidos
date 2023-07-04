

arquivo = open("arquivo.txt","r")


print(arquivo.read())

arquivo.close()

with open("cientista.txt","r") as arqui:
    print(arqui.read())