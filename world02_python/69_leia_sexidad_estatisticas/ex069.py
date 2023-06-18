#Crie um programa que leia o sexo e idade de varias pessoas 
# A cada pergunta respondida pergunte se o usuário quer continuar o questionário
# no final mostre
#A quantas pessoas tem mais de 18 anos
#B quantos homens foram cadastrados
#C quantas mulheres tem menos de 20 anos

#Programa princinpal
while True:
    contsmasc = 1
    contsfemi = 0
    contidade = 0
    maioridade = 0
    fmnova = 0
    qtdade = 0
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo:\n [[M/F]] ').upper()[0]
    resp = input('Deseja continuar respondendo?\n [[S/N]] ').upper()[0]
    while resp not in 'SN':
        resp = input('Deseja continuar respondendo?\n [[S/N]] ').upper()[0]
    if resp == 'N':
        break
    if sexo == 'M':
        contsmasc = contsmasc + 1
    if sexo == 'F':
        contsfemi = contsfemi + 1
    if idade > 18:
        maioridade = maioridade + 1
    if sexo == 'F' and idade < 20:
        fmnova = fmnova + 1
    qtdade = contsfemi + contsmasc
    
print(f' [[A]] Número de pessoas cadastradas com mais de 18 anos: {maioridade} \n\n [[B]] Quantidade de homens cadastrados: {contsmasc} \n\n[[C]] Quantidade de mulheres com menos de 20 anos: {fmnova}')