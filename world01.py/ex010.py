#conversor dollar
dolar = float(input('Qual o valor do dolar hoje? '))
din = float(input('Quanto dinheiro você possui? '))
demdolar = din / dolar
print('Com o seu valor de {:.2f}, você pode comprar {:.2f} dolar(es)'.format(din, demdolar))