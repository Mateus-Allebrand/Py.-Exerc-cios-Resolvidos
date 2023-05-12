#Crie um mini sistema que utilize o interactive help 
#O usuário vai digitar o comando e o manual vai aparecer
#quando o usuário dogitar 'fim' o programa deve finalizar
from time import sleep

c = ['\033[m',             #0 limpar
     '\033[1;36;40m',      # l = ciano f = cinza
     '\033[1;36;42m',      # 2 = ciano f = verde
     '\033[1;36;45m'       #  = ciano f = roxo
    ]


def titulo(msg, cor=0):
    print(c[cor], end='')
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')


def ajuda(m):
    titulo(f'Acessando o manual de: \'{m}\'',2)
    
    help(m)
    print(c[0])

comando = ''
while True:
    comando = str(input('Biblioteca ou função: -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('FIM',1)
