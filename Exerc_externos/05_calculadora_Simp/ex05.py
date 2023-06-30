nome = input("Olá, qual seu nome? \n")

print(f"Seja bem vindo! {nome.title()}")

print("=="*30)
print("CALCULADORA".center(60))
print("=="*30)

n1 = float(input("Digite o primeiro número: \n"))
n2 = float(input("Digite o segundo número: \n"))
op = input("Escolha uma operação: \n (+) (-) (*) (/) \n")

if op == "+":
    resultado = n1 + n2
    print(f"{n1:.2f} + {n2:.2f} = {resultado:.2f}")

elif op == "-":
    resultado = n1 - n2
    print(f"{n1:.2f} - {n2:.2f} = {resultado:.2f}")

elif op == "/":
    resultado = n1 / n2
    print(f"{n1:.2f} / {n2:.2f} = {resultado:.2f}")

elif op == "*":
    resultado = n1 * n2
    print(f"{n1:.2f} x {n2:.2f} = {resultado:.2f}")

else:
    print("Digito Inválido: \n")