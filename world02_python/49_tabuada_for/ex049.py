#fazendo a tabuda usando o laço for

#Programa principal
n = int(input('Enter a number: '))
print('=========TABUADA=========')
for c in range(0,10+1):
    d = n * c
    print('=-=-=-={} X {} = {}=-=-=-='.format(n, c, d))