#Verifica qual número é maior dos dois digitados pelo usuário


#Programa principal
n1 =float(input('Enter a number: '))
n2 =float(input('Enter a number: '))
if n1 > n2:
    print('The number {:.2f} is greater than {:.2f}'.format(n1, n2))
elif n1 < n2:
    print('The number {:.2f} is greater than {:.2f}'.format(n2, n1))
elif n1 == n2:
    print('The number {:.2f} and {:.2f} are the same'.format(n1, n2))