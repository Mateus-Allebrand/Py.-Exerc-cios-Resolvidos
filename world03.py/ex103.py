#faça um programa que receba dois parametros opcionais nome e quantidade de gols e retorne uma mensagem de que jogador com nome ......... fez N° ...... gols, caso não seja passado alrgumentos para os paramentros o programa deve conseguir executar sem problema algum

def ficha(nome, num ):
    if num == '':
        num = 0
    if nome == '':
        nome = '< Desconhecido >'
    return f'O jogador {nome} fez {num} gols na partida'


n = str(input('Nome do jogador: ')).title()
g = str(input('Número de gols: '))
print(ficha(n,g))