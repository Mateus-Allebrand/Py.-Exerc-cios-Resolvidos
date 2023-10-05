#Crie um programa em que o usuários possa digitar uma expressão qualquer que tenha parenteses
#O aplicativo tem que verificar se os parenteses estão abertos e fechados na ordem corretax 

#Programa Principal
x = input('Digite sua expressão: ')
npa = 0
npf = 0
if '(' in x and ')' in x:
    pa = x.index('(')
    pf = x.index(')')
    npa = x.count('(')
    npf = x.count(')')

    if pa < pf and npa == npf:
        print('Os parenteses estão colocados de forma correta!')
    else:
        print('Os parenteses estão na posição errada')
elif '(' in x and ')' not in 'x':
    print('Parenteses incompletos')
elif ')' in x and '(' not in 'x':
    print('Parenteses incompletos')
elif npf != npa:
    print('número de parenteses incorreto')