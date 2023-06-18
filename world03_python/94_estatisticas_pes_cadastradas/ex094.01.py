#crie um programa que leia nome, sexo e idade de varias pessoas
#guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista
#No final mostre
#A- quantas pessoas cadastradas
#B-a média de idade
#C-uma lista com as mulheres
#D-uma lista com as pessoas com idade acima da média
#obs, quando questionar o usuário, só aceite resposta sim ou não
########################################################################################
lista = list()
temp = dict()
med = 0
medidade = 0
mulheres = list()
calc = []
acmedia = []
cont = 0
medof = []
while True:
    temp['nome'] = str(input('Nome: '))
    temp['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
    if temp['sexo'] == 'F':
        mulheres.append(temp['nome'])
    while temp['sexo'] not in 'MF':
        print('ERRO! => Responda apenas com [M] ou [F]')
        temp['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
    temp['idade'] = int(input('Idade: '))
    med += temp['idade']
    lista.append(temp.copy())
    temp.clear()
    x = str(input('Continuar cadastrando? [S/N]')).upper()[0]
    while x not in 'SN':
        print('ERRO! => Responda apenas com [S] ou [N]')
        x = str(input('Continuar cadastrando? [S/N]')).upper()[0]
    if x == 'N':
        break

medidade = med / len(lista)
for n,i in enumerate(lista):
    calc.append(i)
    if calc[n]['idade'] > medidade:
        acmedia.append(calc[n]['nome'])
        acmedia.append(calc[n]['idade'])
        medof.append(acmedia[:])
        acmedia.clear()

print(lista)
print(f'Foram cadastradas {len(lista)} pessoa(s)') #A Respondida
print(f'A media de idade das pessoas cadastradas é {medidade:.2f}') #B Respondida
print(f'As mulheres cadastradas são: {mulheres}') #c Respondida
#print(f'As pessoas que estão acima da média de idade: {medof}') #D Respondida
for z in medof:
    print(f'Acima da média de idade: Nome: {z[0]} Idade: {z[1]} ')
