#Programa pede para o susuário digitar um número, e mostra na tela a tabuada do número digitado pelo usuário.
#OBS: Quando começar os exercícios de listas vou melhorar esse programa.


#Programa principal
n = int(input('Digite um número inteiro: '))
t = 'TABUADA'
zero = 0 * n
one = 1 * n
dos = 2 * n
tre = 3 * n
qua = 4 * n
cin = 5 * n
sex = 6 * n
set = 7 * n
oit = 8 * n
nov = 9 * n
dez = 10 * n
print('{:=^20}'.format(t))
print('     {} x 0 = {}'.format(n, zero))
print('     {} x 1 = {}'.format(n, one))
print('     {} x 2 = {}'.format(n, dos))
print('     {} x 3 = {}'.format(n, tre))
print('     {} x 4 = {}'.format(n, qua))
print('     {} x 5 = {}'.format(n, cin))
print('     {} x 6 = {}'.format(n, sex))
print('     {} x 7 = {}'.format(n, set))
print('     {} x 8 = {}'.format(n, oit))
print('     {} x 9 = {}'.format(n, nov))
print('     {} x 10 = {}'.format(n, dez))