#Programa calcula o valor que usuário informa para ele em reais e mostra quanto equivale esse valor em dollar.


#Programa principal
dolar = float(input('Qual o valor do dolar hoje? '))
din = float(input('Quanto dinheiro você possui? '))
demdolar = din / dolar
print('Com o seu valor de {:.2f}, você pode comprar {:.2f} dolar(es)'.format(din, demdolar))