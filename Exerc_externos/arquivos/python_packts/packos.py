import os 

texto ="Sou um cientista de  dados.\n"
texto += "faturo mais de 120 mil R$ mensal.\n"
texto += "Graças a Deus.\n"

print(texto)

arquivo = open(os.path.join("cientista.txt"), "w")

for word in texto.split("\n"):
    arquivo.write(word + " ")

arquivo.close()