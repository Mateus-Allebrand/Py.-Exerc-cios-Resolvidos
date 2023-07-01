
def soma():
    print("=="*30)
    print("ADIÇÃO".center(60))
    print("=="*30)
    n1 = float(input("\nDigite o primeiro número: \n"))
    n2 = float(input("Digite o segundo número: \n"))
    print(f"\n\033[32m{n1:.2f} + {n2:.2f} = {n1 + n2:.2f}\033[m")
    print("=="*30)


def subt():
    print("=="*30)
    print("SUBTRAÇÃO".center(60))
    print("=="*30)
    n1 = float(input("\nDigite o primeiro número: \n"))
    n2 = float(input("Digite o segundo número: \n"))
    print(f"\n\033[32m{n1:.2f} - {n2:.2f} = {n1 - n2:.2f}\033[m")
    print("=="*30)


def mult():
    print("=="*30)
    print("MULTIPLICAÇÃO".center(60))
    print("=="*30)
    n1 = float(input("\nDigite o primeiro número: \n"))
    n2 = float(input("Digite o segundo número: \n"))
    print(f"\n\033[32m{n1:.2f} x {n2:.2f} = {n1 * n2:.2f}\033[m")
    print("=="*30)


def div():
    try:
        print("=="*30)
        print("DIVISÃO".center(60))
        print("=="*30)
        n1 = float(input("\nDigite o primeiro número: \n"))
        n2 = float(input("Digite o segundo número: \n"))
        print(f"\n\033[32m{n1:.2f} / {n2:.2f} = {n1 / n2:.2f}\033[m")
        print("=="*30)
    except ZeroDivisionError:
        print("Não é possível fazer divisão por zero!\nMude o denominador!")

def menu():
    print("")
    print("=-="*20)
    print("=> CALCULADORA <=".center(60))
    print("=-="*20)
    print("")
    x = "=-="*20
    op = int(input(f"[[1]] Adição\n\n[[2]] Subção\n\n[[3]] Multiplicação\n\n[[4]] Divisão\n\n[[0]] Sair\n{x}\n"))
    return op
    