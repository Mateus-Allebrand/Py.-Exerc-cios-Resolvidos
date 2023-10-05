#Faça um programa que tenha a função notas(), que pode receber varias notas e retormar um dicionário com as seguintes infomamções:
#A maior nota
#A menor nota
#a media da turma
#A situação opcional
#adcione também a docsting
####################################################################################################################


def notas(*num, sit=False):
    dic = dict()
    n = len(num)
    for i,d in enumerate(num):
        dic[i] = d
            
    print(dic)    
    
        
        

notas(2,4,5)