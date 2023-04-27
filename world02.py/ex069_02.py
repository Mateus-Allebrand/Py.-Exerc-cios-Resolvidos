toth = 0
totmm20 = 0
totm18 = 0
while True:
    idade = int(input('Digite idade: '))
    sexo = input('Digite sexo: [[M/F]] ').upper()
    while sexo not in 'MF':
        sexo = input('Digite sexo: [[M/F]] ').upper()
    resp = input('Quer continuar respondendo: [[S/N]]').upper()
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totmm20 += 1
    if idade >= 18:
        totm18 += 1
    if resp == 'N':
        break
    while resp not in 'SN':
        resp = input('Deseja continuar respondendo?\n [[S/N]] ').upper()[0]
    
print(f'A quantidade de pessoas com mais de 18 anos é: {totm18}')
print(f'A quantidade de homens é: {toth}')
print(f'Total de mulheres com menos de 20 anos {totmm20}')