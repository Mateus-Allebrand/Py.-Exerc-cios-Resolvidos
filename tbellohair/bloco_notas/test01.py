#Teste para anotar valores e serviços
from functions import rowdoble, tiposerv, cabelo, unhas, sombrancelha
import pandas as pd
import datetime
import json
lista_geral = []

while True:
    lista_geral.clear()

    servicos = {}
    print("\nOlá,\n")
    print(rowdoble())
    print("MENU DE OPÇÕES: ".center(60))
    print(rowdoble())
    op = int(input(f"\n[[1]] Novo serviço: \n\n[[2]] Vizualizar serviços realizados hoje: \n\n[[0]] Sair: \n\n{rowdoble()}\n"))

    #Funcionando
    while op not in range(0,3):
        print("'OP' Inválida!")
        op = int(input(f"\n[[1]] Novo serviço: \n\n[[2]] Vizualizar serviços realizados hoje: \n\n[[0]] Sair: \n\n{rowdoble()}\n"))

    #Adcionar um novo serviço
    if op == 1:
        nome = input("Nome do cliente: \n").title()
        servicos[nome] =tiposerv()
        lista_geral.append(servicos)
        data = datetime.datetime.now()
        data_atual = data.strftime('%d/%m/%Y %H:%M:%S')
        lista_geral.append(data_atual)
        with open('bellohair.txt', 'a') as arquivo:
            arquivo.write(json.dumps(lista_geral, ensure_ascii=False) + "\n")
        
        print(lista_geral)
        continue
        
    if op == 2:
        with open('bellohair.txt', 'r') as arquivo:
            db = arquivo.read()
            print(db)
            continue
        
    if op == 0:
        print("good bye")
    
    break
