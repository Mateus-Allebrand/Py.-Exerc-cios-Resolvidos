import csv

with open("arqui.csv","w") as arquivo:
    #Cria objeto de gravação
    writer = csv.writer(arquivo)

    # grava arquivos linha a linha
    writer.writerow(('n1','n2','n3'))  #Estou escrevendo linha a linha 
    writer.writerow((10, 20, 30))
    writer.writerow((100, 200, 300))
    writer.writerow((1000, 2000, 3000))

    #Obs> Acima estava dando erro. Estava sem identação.Problema resolvido.


#with open ("arqui.csv", "r", encoding="utf8", newline="\r\n") as arquivo:

#     #Cria o objeto de leitura
#   leitor= csv.reader(arquivo)

#     #Cria o loop para percorrer e imprimir cada elemento do objeto 
#     for x in leitor:
#         print(x)


with open("arqui.csv","r") as arquivo:
    leitor = csv.reader(arquivo)
    #linha de código abaixo,retornava listas vazias(referente as linhas em branco)
    lista = [linha for linha in leitor if linha and any(linha)] #problema resolvido!

print(lista)

for i in lista[1:]: #iniciei no indice 01, pois não preciso do cabeçalho
    print(i)