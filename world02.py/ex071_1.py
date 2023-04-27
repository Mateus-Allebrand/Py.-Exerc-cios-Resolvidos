#
print('=-'*30)
print('{:>35}'.format('BANCO CENTRAL'))
print('=-'*30)
valor = int(input('\n\n             Digite o valor que deseja sacar: '))
cedatual = 50
cont = 0
while True:
    if valor >= cedatual:
        while valor >= cedatual:
            valor -= cedatual
            cont += 1
            break    
    else:
        if valor < cedatual:
            cedatual = 20
            while valor >= cedatual:
                valor -= cedatual
                cont += 1
                break   
