#crie uma tupla com os 20 primeiros colocados da copa do mundo de 2018
#Quais são os 5 primeiros colocados?
#Os últimos 4 colocados?
#uma lista com os times em ordem alfabética
#em qual posição está portugal?


#Programa principal
posicao = ('França', 'Croácia', 'Bélgica','Inglaterra', 'Uruguai','Brasil',	'Suécia','Rússia','Colômbia','Espanha',		'Dinamarca', 'México', 'Portugal', 'Suíça', 'Japão', 'Argentina', 'Senegal', 'Irã', 'Coreia do Sul', 'Peru')

print(f'Os cinco primeiros colocados são: {posicao[0:5]}')
print(f'Os quatro últimos colocado são: {posicao[-4 : ]}')
print(sorted(posicao))
x = posicao.index('Portugal')
print(f'Portugal está na {x}° posição')