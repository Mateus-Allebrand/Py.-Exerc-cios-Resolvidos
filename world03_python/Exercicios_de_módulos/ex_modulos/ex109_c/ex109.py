#Modifique as funções criadas no exercicio 107 para que elas aceitem um parametro amais,
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda()
#desenvolvido no desafio 108
###############################################################################################
import moeda

while True:
    valor = float(input('Digite o valor: R$ '))
    porcentagem =int(input('Porcentagem: '))
    f = str(input('Mostrar formatado? [S/N]')).upper()[0]
    if f == 'N':
        nota = cifrao=False
    if f == 'S':
        nota = cifrao=True
    r1 = moeda.aumentar(valor,porcentagem,nota)
    r2 = moeda.diminuir(valor,porcentagem,nota)
    r3 = moeda.dobro(valor,nota)
    r4 = moeda.metade(valor,nota)
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
