#crie um programa que simule o funcionamento de um caixa eletronico
#pergunte ao usuário qual valor será sacado 
# o programa vai informar quantas celulas de cada valor será entregue ao cliente
# considere que o caixa tem cedulas de 50,20,10,1


#Programa principal
print('============================================')
print('                  Banco')
print('============================================')
valor = int(input('Digite o valor do saque: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'{totced} Cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced =10
        elif ced == 10:
            ced =1
        totced = 0
        if total == 0:
           break