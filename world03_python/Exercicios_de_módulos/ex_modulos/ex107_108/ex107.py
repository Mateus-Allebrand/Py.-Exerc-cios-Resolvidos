#Crie um Módulo chamado moeda.py que tenha funções incorporadas 
#aumentar(), diminuir(), dobro(), metade()
#faça um programa que importe esse módulo e use algumas dessas funções
#################################################################################################
import moeda

while True:
    valor = float(input('Qual valor: '))
    porcentagem =int(input('Porcentagem: '))
    r1 = moeda.aumentar(valor,porcentagem)
    r2 = moeda.diminuir(valor,porcentagem)
    r3 = moeda.dobro(valor)
    r4 = moeda.metade(valor)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    x = str(input('deseja continar? [S/N]')).upper()[0]
    while x not in 'NS':
        print('Erro! Responda penas com [S] ou [N]')
        x = str(input('Deseja continar? [S/N]')).upper()[0]
    if x == 'N':
        print('   =====> FIM! <=====')
        break