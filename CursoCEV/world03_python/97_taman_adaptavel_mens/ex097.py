#crie um programa que leia uma mensagem como argumento para uma parâmentro e mostre a mensgame com tamanho adaptável


def escreva(mens, tam):
   print('-' * (tam + 6))
   print(f'{mens:^{tam + 6}}')
   print('-' * (tam + 6))


# programa principal.
for i in range(0,3):
    msg = str(input('Escreva uma mensagem: ')).title()
    t = len(msg)
    escreva(msg,t)
