#Programa solicita o salário do funcionário e porcentagem de aumento, quando fornecidos os dados ele gera uma mensagem formatada com o valor do salário atualizado com o aumento.


#Programa principal
salariohj = float(input('Qual o salário do funcionário atualmente? '))
porcaumen = float(input('Qual a porcentagem de aumento? '))
totaumento = salariohj * (porcaumen / 100)
salariofi = salariohj + totaumento
print('O salário do funcionário hoje é de R$ {:.2f}, com o aumento de {:.0f}%, o salário ficará em R$ {:.2f}'.format(salariohj, porcaumen, salariofi))