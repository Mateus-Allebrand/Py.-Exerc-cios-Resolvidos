#melhorando exercício 61
primeiro = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} => '.format(termo),end='')
    cont += 1
    termo += razao
resp = int(input('\n\nQuer adcionar mais alguns números a Progressão? \n\n         [ 1 ] SIM \n\n         [ 2 ] NÃO \n\n         '))
while resp == 1:
    numnovo = int(input('\n\nQuantos números mais você quer na progressão? \n'))
    contmnovo = cont + numnovo
    while cont <= (contmnovo - 1):
        print('{} => '.format(termo),end='')
        cont += 1
        termo += razao
while resp != 1 and resp != 2:
    print('\n\nDigito invalido!\n\nTente outra vez!')
    resp = int(input('\n\nQuer adcionar mais alguns números a Progressão? \n\n         [ 1 ] SIM \n\n         [ 2 ] NÃO \n\n         '))
print('\n=========== FIM ===========')