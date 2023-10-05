#O programa pede ao usuário para digitar um número (entrada) e gera uma mensagem (saída) que formatada com o número digitado por ele e também o seu antecessor e sucessor é mostrado na mensagem para o usuário.


#Programa principal
n = int(input('Digite um número: '))
nant = n - 1
nsuc = n + 1
print('O número digitado por você foi {}, seu antecessor é {} e, seu sucessor é {}'.format(n, nant, nsuc))