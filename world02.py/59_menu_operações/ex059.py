#crie um programa que leia 2 números e mostre na tela um menu de opções
#somar
#multiplicar
#maior
#novos números
#sair


#Programa principal

n1 = float(input(' Digite um número: '))
n2 =float(input('Digite outro número: '))
op = int(input('=========== MENU OPÇÕES ===========\n== [ 1 ] => SOMAR                ==\n== [ 2 ] => MULTIPLICAR          ==\n== [ 3 ] => MAIOR                ==\n== [ 4 ] => NOVOS NÚMEROS        ==\n== [ 5 ] => SAIR                 ==\n===================================\n'))
res = 0
n = []
while op != 5:
    if op == 1:
        res = n1 + n2
        print('Resultado de {:.2f} + {:.2f} = {:.2f} '.format(n1, n2, res))
        n1 = float(input(' Digite um número: '))
        n2 =float(input('Digite outro número: '))
        op = int(input('=========== MENU OPÇÕES ===========\n== [ 1 ] => SOMAR                ==\n== [ 2 ] => MULTIPLICAR          ==\n== [ 3 ] => MAIOR                ==\n== [ 4 ] => NOVOS NÚMEROS        ==\n== [ 5 ] => SAIR                 ==\n===================================\n'))
    if op == 2:
        res = n1 * n2
        print('Resultado de {} X {} = {} '.format(n1, n2, res))
        n1 = float(input(' Digite um número: '))
        n2 =float(input('Digite outro número: '))
        op = int(input('=========== MENU OPÇÕES ===========\n== [ 1 ] => SOMAR                ==\n== [ 2 ] => MULTIPLICAR          ==\n== [ 3 ] => MAIOR                ==\n== [ 4 ] => NOVOS NÚMEROS        ==\n== [ 5 ] => SAIR                 ==\n===================================\n'))
    if op == 3:
        n = [n1,n2]
        n = max(n)
        print('Maior entre {} e {} é {} '.format(n1, n2, n) )
        n1 = float(input(' Digite um número: '))
        n2 =float(input('Digite outro número: '))
        op = int(input('=========== MENU OPÇÕES ===========\n== [ 1 ] => SOMAR                ==\n== [ 2 ] => MULTIPLICAR          ==\n== [ 3 ] => MAIOR                ==\n== [ 4 ] => NOVOS NÚMEROS        ==\n== [ 5 ] => SAIR                 ==\n===================================\n'))
    if op == 4:
        n1 = float(input(' Digite um número: '))
        n2 =float(input('Digite outro número: '))
        op = int(input('=========== MENU OPÇÕES ===========\n== [ 1 ] => SOMAR                ==\n== [ 2 ] => MULTIPLICAR          ==\n== [ 3 ] => MAIOR                ==\n== [ 4 ] => NOVOS NÚMEROS        ==\n== [ 5 ] => SAIR                 ==\n===================================\n'))
print('\n   ==-=-==-=-== FIM ==-=-==-=-==')