from math_mat import soma,subt,mult,div,menu

while True: 
    op = menu()
    while op < 0 or op > 4:
        print("\033[31m\nDígito inválido!\n\nTente outra vez!\033[m\n")
        op = menu()
    print("")
    if op == 1:
        soma()
    if op == 2:
        subt()
    if op == 3:
        mult()
    if op == 4:
        div()
    if op == 0:
        print("=-="*20)
        print("CALCULADORA FINALIZADA".center(60))
        print("=-="*20)
        break