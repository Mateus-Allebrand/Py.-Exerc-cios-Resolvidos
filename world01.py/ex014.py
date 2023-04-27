#conversor temperatura
celsius = float(input('Digite a temperatura em Graus Celsios: '))
osc = 1.8
fah = 32
celf = celsius * osc
fahrenheit = fah + celf
print('A temperatura em °F é {:.1f}'.format(fahrenheit))