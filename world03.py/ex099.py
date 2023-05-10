#faça um programa que tennha uma função maior( que analize qual o maior valor passado) e mostre na tela qual maior valor


def maior(*num):
    maior = 0
    cont = 0
    for i,n in enumerate(num):
        cont +=1
        if i == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    print('\nAnalizando valores: ')
    print(f'Fotam informados {cont} valores')
    print(f'o maior número é: {maior} \n')
    


maior(1,5,6,7,8,9,11,2)
maior(5, 6, 1, 2, 12, 13, 15, 51, 45, 17, 19)
maior()
maior(7)