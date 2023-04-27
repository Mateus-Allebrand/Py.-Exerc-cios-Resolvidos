#conversor
n = float(input('Digite um número em metros: '))
ncent = n * 100
nmili = n * 1000
print('O número em metros que voce digitou é {}, isso equivale a {:.0f} centimetros e {:.0f} milimetros.'.format(n, ncent, nmili))