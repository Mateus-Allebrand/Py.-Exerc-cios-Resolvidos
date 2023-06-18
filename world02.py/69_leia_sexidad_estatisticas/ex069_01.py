#Crie um programa que leia o sexo e idade de varias pessoas 
# A cada pergunta respondida pergunte se o usuário quer continuar o questionário
# no final mostre
#A quantas pessoas tem mais de 18 anos
#B quantos homens foram cadastrados
#C quantas mulheres tem menos de 20 anos


#Programa principal
toth = 0
totm18 = 0
totmm20 = 0
idade = 0
while True:
    idade = int(input('Digite idade: '))
    sexo = input('Digite o sexo: [[M/F]] ').upper()[0]
    resp = input('Deseja continuar respondendo? [[S/N]]').upper()[0]
    if sexo == 'M':
         toth += 1
    if sexo == 'F' and idade < 20:
        totmm20 += 1
    if idade > 18 :
        totm18 += 1
    if resp == 'N':
            break



