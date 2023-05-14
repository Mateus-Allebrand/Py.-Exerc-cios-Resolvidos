#O programa pede ao usuário para digitar um número, e como saída gera uma frase formatada mostrando o número digitado pelo usuário, o dobro, o triplo e a raiz quadrada.


#Programa principal
n = float(input('Digite um número: '))
n2 = 2 * n
n3 = 3 * n
nraiz = n**(1/2)
print('o número digitado foi {},\no dobro dele é {},\no triplo é {},\ne sua raiz é {}'.format(n, n2, n3, nraiz))
