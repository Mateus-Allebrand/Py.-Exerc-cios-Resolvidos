#Crie um programa que leia o nome e o aproveitamento dos jogadores
#(quantas partidas disputadas e quantos gols feitos em cada partida)
#no final mostre os dados do time e pergunte ao usuário se quer ver algum jogador em especifico

time = list()
jogador = dict()
gols = dict()
z = list()
totgol =[]

while True:
    totg = 0
    jogador['nome'] = str(input('Nome: ')).title()
    n = int(input('N° de partidas: '))
    for p in range(0, n):
        gols[p + 1] = int(input(f'Quantos gols na {p+1}° partida:'))
        totg += gols[p + 1]
    jogador['partidas'] = gols.copy()
    jogador['total_gols'] = totg
    time.append(jogador.copy())
    gols.clear()
    jogador.clear()
    x = str(input(f'Cadastrar outro? [S/N]')).upper()[0]
    while x not in 'SN':
        print(f'ERRO! Responda apenas com [S] ou [N].')
        x = str(input(f'Cadastrar outro? [S/N]')).upper()[0]
    if x == 'N':
        print('             == -> FIM! <- ==')
        break
while True:
    print()
    print('==-=='*10)
    print('              TIME APROVEITAMENTO   ')
    print('--=--'*10)
    print('CÓD:       NOME:                           N° GOLS')
    for t,i in enumerate(time):
        print(f' {t:<2}        {i["nome"]:<10}                         {i["total_gols"]:<8}')
    print('==-=='*10)
    r = str(input('Deseja ver dados de algum jogador em particular? [S/N]')).upper()[0]
    while r not in 'SN':
        print('ERRO! Responda apenas com [S] ou [N]')
        r = str(input('Deseja ver dados de algum jogador em particular? [S/N]')).upper()[0]
    if r == 'N':
        print('              == -> FIM! <- ==')
        break
    cod = int(input('Digite o código: '))
    print()
    print(time[cod])
    