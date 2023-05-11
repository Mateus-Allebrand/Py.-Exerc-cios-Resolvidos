#Crie um programa que tenha uma função chamada voto()
#Que vai receber um parametro - o ano de nascimento de uma pessoa retornando um valor literal
#vai dizer se uma pessoa tem o voto obrigatório, negado ou opcional
#voto obrigatório de 18 a 70 anos
#############################################################################################
from datetime import datetime

def voto(ano):
    idade = datetime.now().year - ano
    if idade >= 18 and idade <= 70:
        return(f'Idade: {idade} anos \nVoto obrigatório!')
    elif idade >= 16 and idade < 18:
        return(f'Idade: {idade} anos \nVoto opcional!')
    elif idade > 70:
        return(f'Idade: {idade}anos \nVoto opcional!')
    else:
        return(f'Idade: {idade} anos\nVoto negado!')
    return idade
    


#programa princiopal
print('_'*40)
id = int(input('\nAno de nascimento: '))
print(voto(id))
