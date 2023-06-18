#Programa simples que solicita dois números ao usuário e soma-os,como saída temos uma mensagem formatada com o resultado.


#Programa principal
n1 = int(input('digite um número:'))
n2 = int(input('Digite outro:'))
s = n1 + n2
print('A soma entre os números {} e {} vale {}'.format(n1, n2, s))