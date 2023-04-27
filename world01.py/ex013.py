#calcular aumento
salariohj = float(input('Qual o salário do funcionário atualmente? '))
porcaumen = float(input('Qual a porcentagem de aumento? '))
totaumento = salariohj * (porcaumen / 100)
salariofi = salariohj + totaumento
print('O salário do funcionário hoje é de R$ {:.2f}, com o aumento de {:.0f}%, o salário ficará em R$ {:.2f}'.format(salariohj, porcaumen, salariofi))