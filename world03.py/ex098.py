#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                  #a) de 1 até 10, de 1 em  1 
#b) de 10 até 0, de 2 em 2  
#c) uma contagem personalizada


from time import sleep
def contador(inicio,fim, passo):
    for c in range(inicio, fim , passo):
        print(f'{c} ',end='', flush= True)
        sleep(0.5)
        

print('Contagem de 1 até 10 de 1 em 1:')
contador(1,11,1)
print('\ncontagem de regressiva de 10 até 0 de 2 em 2: ')
contador(10,-1,-2)
print('\n =-> Peronalize sua Contagem <-= ')
i = int(input('Digite o valor de inicio: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo: '))
if p < 0:
    f -= 1
else:
    f += 1
contador(i,f,p)