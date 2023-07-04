#JSON (java script object notation)

import json


dict_mat = {"nome": "Mateus",
        "nascimento": "1996",
        "profissão": "Programador",
        "linguagem": "Python"
        }

# for i,j in dict_mat.items():
#     print(f"{i} {j}")

json.dumps(dict_mat)




with open("arquimat.json","w") as arquivo: #abrindo um arquivo.json  para gravação
    arquivo.write(json.dumps(dict_mat)) # Converte o dicionario para o formatp Json


with open("arquimat.json","r") as arquivo:    
    texto = arquivo.read()
    dados = json.loads(texto)

arquivo_fonte = "arquimat.json"
arquivo_destino = "dados.txt"

with open(arquivo_fonte,"r") as infile:
    text = infile.read()
    with open(arquivo_destino,"w") as outfile:
        outfile.write(text)


#trecho de codigo abaixo == o de cima porém otimizado em apenas uma linha
open(arquivo_destino,"w").write(open(arquivo_fonte, "r").read())

with open("dados.txt","r") as arquivo1:
    texto = arquivo1.read()
    dados = json.loads(texto)

print(dados)