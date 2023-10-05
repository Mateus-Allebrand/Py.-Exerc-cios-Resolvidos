#Programa pede uma medida em metros (converte para milimetros e centímetros) e gera uma mensagem formatada com a medida em metro convertida em centimetros e milimetros.


#Programa principal
n = float(input('Digite um número em metros: '))
ncent = n * 100
nmili = n * 1000
print('O número em metros que voce digitou é {}, isso equivale a {:.0f} centimetros e {:.0f} milimetros.'.format(n, ncent, nmili))