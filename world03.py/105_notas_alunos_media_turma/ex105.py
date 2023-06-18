#Faça um programa que tenha a função notas(), que pode receber varias notas e retormar um dicionário com as seguintes infomamções:
#A maior nota
#A menor nota
#a media da turma
#A situação opcional
#adcione também a docsting
####################################################################################################################
def notas(*num, sit=False):
    """Função Notas():
       Recebe varias notas de um aluno e gera um dicionário (Boletim) com respostas:
       -> Quantas notas foram adicionadas:
       -> O valor da maior nota:
       -> O valor da menor nota:
       -> Valor da média:
       #Param. *NUM: recebe notas
       #Param.  SIT: Recebe True or False.(opcional)
           -True: Mostra no dicionario:
              Media >= 8 = 'Boa'
              Media >= 6 and < 8 = 'Razoável'
              Media < 6 = 'Ruim'
           -False: Não mostra a situação.
        Return: Retorna o dicionario (Boletim).
    """
    n = len(num)
    media = 0
    cont = 0
    maior = menor = 0
    boletim = dict()
    for i, j in enumerate(num):
        cont += j
        if i == 0:
            maior = menor = j
        else:
            if j > maior:
                maior = j
            if j < menor:
                menor = j
    media = cont / len(num)
    boletim['Total'] = len(num) 
    boletim['Maior_nota'] = maior
    boletim['Menor_nota'] = menor
    boletim['Media'] = media
    if sit == True:
        if media >= 8:
            boletim['Situação'] = 'Boa'
        elif media >= 6 and media < 8:
            boletim['Situação'] = 'Razoavel'
        else:
            boletim['Situação'] = 'Ruim'
    resp = boletim        
    return resp


#Programa principal:
resp = notas(7.5,8.2,9.8,sit =True)
print(resp)
help(notas)