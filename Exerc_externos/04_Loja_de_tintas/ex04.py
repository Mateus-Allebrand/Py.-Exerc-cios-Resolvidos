# Programa para loja de tintas:
# O programa deve pedir o tamanho da area a ser pintada 
# Deve calcular levando em consideração que um litro de tinta pinta 3 m² 
# A tinta é vendida em latas de 1 litro , 3,6 litros e 18 litros.
# ajude o cliente a tomar a melhor decisão 
# o valor da lata de 18 litros é de 178,90 

from math import ceil


# Calcula quanto rende por embalagem 
embp = 1 * 3      #rende  3.0 m²     R$   9.94
embm = 3.6 * 3    #rende 10.8 m²     R$  37.98
embg = 18 * 3     #rende 54.0 m²     R$ 178.90 


while True:
    print("\033[34m=="*30)
    print("MENU".center(60))
    print("=="*30)
    print("\033[m")
    
    op = int(input(" [1] Orçamento completo \n [2] calcular Área \n [3] calcular Quantidade de Tinta \n [4] Ver valores \n [0] Sair \n\n\033[34m============================================================\033[m\n"))
    while op < 0 or op >4:
        print("\033[31mDigito inválido!\n\nTente outra vez!\033[m\n\n")
        op = int(input("\n [1] Orçamento completo \n [2] calcular Área \n [3] calcular Quantidade de Tinta \n [4] Ver valores \n [0] Sair \n\n============================================================\n"))
    if op == 1:
        # Calcula a area
        altura = float(input("\nDigite a altura: "))
        largura = float(input("\nDigite a largura: "))
        area = largura * altura
        print(f"\nVocê possui uma área de {area:.2f} m²\n")
        print(f"Para um melhor desempenho, recomendamos 3 demãos de tinta\n")
        print(f"Tinta rende 3 m² por litro\n")

        if area <= 2:
            print("Recomendamos a lata de 1 litro => R$ 9.94 cada \n")
            qlatas = (area * 3) / 3
            gasto = 9.94 * (ceil(qlatas))
            print(f"\033[32mVocê precisa de {ceil(qlatas)} lata(s) \n\nValor total: R$ {gasto:.2f} \033[m\n")

        elif area <= 12:
            print("Recomendamos a lata de 3.6 litros => R$ 37.98 cada \n")
            qlatas = (area * 3) / 10.8
            gasto = 37.98 * (ceil(qlatas))
            print(f"\033[32mVocê precisa de {ceil(qlatas)} lata(s) \n\nValor total: R$ {gasto:.2f} \033[m\n")

        elif area > 12:
            print("Recomendamos a lata de 18 litros => R$ 178.90 cada \n")
            qlatas = (area * 3) / 54
            gasto = 178.90 * (ceil(qlatas))
            print(f"\033[32mVocê precisa de {ceil(qlatas)} lata(s) \n\nValor total: R$ {gasto:.2f} \033[m\n")

    if op == 2:
        # Calcula a area
        altura = float(input("\nDigite a altura: "))
        largura = float(input("\nDigite a largura: "))
        area = largura * altura
        print(f"\nVocê possui uma área de {area:.2f} m²\n")

    if op == 3:
        area = float(input("Digite a área: "))
        qtinta = area / 3
        vcorreto = qtinta * 3
        qtinta = ceil(qtinta)
        vcorreto = qtinta * 3
        print(f"Você precisa de {qtinta} litro(s) de tinta para cobrir a area")
        print(f"Para um melhor desempenho, recomendamos 3 demãos de tinta\n")
        print(f"\033[32mNecessário {ceil(vcorreto)} litro(s) para cobrir a área corretamente\033[m")

    if op == 4:
        print("=="*30)
        print("\033[33m EMBALAGEM              RENDIMENTO                VALORES\033[m\n")
        print(" 1.0 litro                3.00 m²               R$   9.94")
        print(" 3.6 litros              10.80 m²               R$  37.98")
        print("18.0 litros              54.00 m²               R$ 178.90")
        print("")
        print("=="*30)

    if op == 0:
        print("=="*30)
        print("FIM".center(60))
        print("=="*30)
        break
 