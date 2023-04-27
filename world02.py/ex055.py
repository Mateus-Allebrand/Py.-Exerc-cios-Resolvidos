#leia o peso de 5 pessoas e diga qual é o mais pesado e qual é o mais leve entre eles
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite o peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {:.2f}\nO menor peso é {:.2f}'.format(maior, menor))