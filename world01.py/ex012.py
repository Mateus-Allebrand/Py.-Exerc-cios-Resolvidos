#Programa pede valor do produto e porcentagem de desconto, quando fornecidos as informações ele calcula e mostra uma mensagem formatada com o valor do produto ja com o desconto.


#Programa principal
valorprod = float(input('Qual valor do produto? '))
porcdesc = float(input('Qual a porcentagem de desconto no produto? '))
valordesc = valorprod * (porcdesc/100)
valorofic = valorprod - valordesc
print(' o seu produto custa R$ {:.2f} , com o seu desconto de {:.0f}% sairá por R$ {:.2f} .'.format(valorprod, porcdesc, valorofic))