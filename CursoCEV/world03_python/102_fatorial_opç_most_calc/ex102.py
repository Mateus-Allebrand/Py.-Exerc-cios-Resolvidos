#Crie um programa que tenha uma função fatorial() que receba dois parametros, o número do fatorial, e o segundo parametro é um valor boleano se deseja ou não mostrar o processo de calculo na tela

def fatorial(n = 1, bol = 0):
    """-> Calcula o fatorial de um número.
        # Param. N: Número que será calculado o fatorial
        # Param. Bol: Indica um valor boleano a ser passado
                 Se True: Mostra o cálculo realizado.
                 Se False: Mostra apenas o resultado.
        # Return: Sem
    """
    while n == 0:
        print('Erro!')
        print('Adcione um número diferente de 0 entre os parenteses')
        x = str(input('certo? [S/N]')).upper()[0]
        if x == 'S':
            n = 3
            print('coloquei o número 3 de exemplo para você ver o funcionamento!')
            print('Agora é sua vez!')
        if x == 'N':
            print('Certo,\nVamos finalizar!')
            res = '=-=-=-=- fim -=-=-=-=    '
            break
    while n == 1:
        print('O resultado de 1! = 1')
        print(f'Vou colocar o n° 3 para você ver o funcionamento:')
        n = 3
        break
    cont = 0
    for i in range(n,1,-1):
        cont +=1
        if cont == 1:
            res = i
        else:
            res = res * i
    if bol == True:
        for j in range(n,1,-1):
            print(f'{j} x ', end='' )
        print(f'1 = {res}')       
    else:
        if bol == False:
           print(f'O resultado de {n}! = {res}')
        
#Programa Principal:
fatorial(6,True)
help(fatorial)