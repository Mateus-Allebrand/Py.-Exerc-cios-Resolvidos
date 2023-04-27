#calcular aluguel
dias = float(input('Por quantos dias o carro foi alugado? '))
km =float(input('Quantos km foi andando com o carro andou nesse periodo? '))
valuguel = dias * 60.0
valkm = km * 0.15 
totdevido = valuguel + valkm
print('Você deve R$ {} de aluguel pelos dias em que o carro foi utilizado, com um adcional de R$ {} pelos km(s) rodado com o veículo, totalizando assim um valor total de R$ {}'.format(valuguel, valkm, totdevido))