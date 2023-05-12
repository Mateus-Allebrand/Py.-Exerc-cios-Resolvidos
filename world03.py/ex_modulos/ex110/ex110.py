#adcione no  módulo moeda.py  criado nos desafios anteriores uma função chamada resumo
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo até aqui.
#####################################################################################################
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
    moeda.resumo(r1,r2,r3,r4)
    x = str(input('deseja continar? [S/N]')).upper()[0]
    while x not in 'NS':
        print('Erro! Responda penas com [S] ou [N]')
        x = str(input('Deseja continar? [S/N]')).upper()[0]
    if x == 'N':
        fim = '=====> FIM! <====='
        print(f'{fim}'.center(65))
        break
    print(moeda.resumo(r1,r2,r3,r4))