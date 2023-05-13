#Dentro do pacote utilcev que criamos no ex111 , temos o módulo dados, crie uma função leiadinheiro()
#que seja capaz de funcionar como uma função imput(),mas com uma validação de dados, para aceitar valores apenas monetários
################################################################################################################
from utilcev import moeda
from utilcev import dados 

while True:
    valor = dados.leiadinheiro('digite um valor: R$')
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