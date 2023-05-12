def aumentar(n,p,cifrao=False):
    aum = n *(p/100)
    tot = n + aum
    if cifrao == False:
        forma = f'O valor: {n:.2f} com um aumento de {p}% é igual a {tot:.2f}'
    if cifrao == True:
        forma = f'O valor: R$ {n:.2f} com um almento de {p}% é igual a R$ {tot:.2f}'
    return forma

def diminuir(n,p,cifrao=False):
    dim = n *(p/100)
    tot = n - dim
    if cifrao == False:
        forma = f'O valor: {n:.2f} com uma redução de {p}% é igual a {tot:.2f}'
    if cifrao == True:
        forma = f'O valor: R$ {n:.2f} com uma redução de {p}% é igual a R$ {tot:.2f}'
    return forma


def metade(n,cifrao=False):
    tot = n / 2
    if cifrao == False:
        forma = f'A metade de {n:.2f} é {tot:.2f}'
    if cifrao == True:
        forma = f'A metade de R$ {n:.2f} é R${tot:.2f}'
    return forma



def dobro(n,cifrao=False):
    tot = n * 2
    if cifrao == False:
        forma = f'O dobro de {n:.2f} é {tot:.2f}'
    if cifrao == True:
        forma = f'O dobro de R$ {n:.2f} é R${tot:.2f}'
    return forma


