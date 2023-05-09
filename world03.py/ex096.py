#Usando funções , faça um programa que leia lardura e altura de um terreno e mostre ao final quantos m² ele tem

def calculador(l,a):
     m2 = l * a
     print(f'   O terreno tem área de {m2:.2f} m²')
     print('-=' * 20)


print('  ====== CALCULADORA DE ÁREA =========')
print('-=' * 20)
l = float(input('   #   Digite -> Largura: '))
a = float(input('   #   Digite -> Altura: '))
calculador(l,a)