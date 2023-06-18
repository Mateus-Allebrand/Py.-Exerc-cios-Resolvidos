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
    temp['nome'] = str(input('Nome: ')).title()
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

print('=='*30)
print('=='*30)
print(f'\nForam cadastradas {len(lista)} pessoa(s)') #A Respondida
print('-='*30)
print(f'\nA media de idade das pessoas cadastradas é de {medidade:.1f} anos') #B Respondida
print('-='*30)
print(f'\nAs mulheres cadastradas são: {mulheres}') #c Respondida
print('-='*30)
#print(f'As pessoas que estão acima da média de idade: {medof}') #D Respondida
for z in medof:
    print(f'\nAcima da média de idade: Nome: {z[0]} Idade: {z[1]} \n')
print('=='*30)
print('=='*30)