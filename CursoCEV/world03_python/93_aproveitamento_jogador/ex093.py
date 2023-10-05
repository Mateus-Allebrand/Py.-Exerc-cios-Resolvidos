#crie um programa que gerencie o aproveitamento de um jogador de futebol
#o programa vai ler o nome e quantas partidas ele jogou
#vai ler quantos gols ele fez em cada partida
# No final de tudo vai ser guardado tudo em um dicionário incluindo o total de gols feito durante o campeonato


dados = dict()
temp = dict()
contg = 0

dados['Nome'] = str(input('Nome do jogador: ')).title()
n = int(input('Total de partidas: '))
for i in range(0, n):
    temp[i + 1] = int(input('N° gols:'))
    contg += temp[i + 1]



print('-=' * 30)
for j, k in temp.items():
    print(f'Na {j}° partida - Marcou {k} gol(s)')
print(f'Total de {contg} gols')

dados['partidas'] = temp.copy()
dados['total_gols'] = contg

print('-=' * 30)
for a, b in dados.items():
    print(f'No campo {a} tem {b}')

print('-='*30)
print(dados)