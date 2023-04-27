# Recriando o exercício 51 com while, esse exercício consiste em ler um número e
# sua P. Aritmética e mostrar na tela os 10 primeiros resultados

#primeiro = int(input('Dogite o número: '))
#razao = int(input('Digite a razão: '))
#termo = primeiro
#cont = 1
#while cont <= 10:
 #   print('{} -> '.format(termo), end='')
  #  cont += 1
   # termo += razao

primeiro = int(input('Dogite o número: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    cont += 1
    termo += razao
    

