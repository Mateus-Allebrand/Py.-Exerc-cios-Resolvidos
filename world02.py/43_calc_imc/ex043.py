#underweight, ideal weight, overweight, obesity, morbid obesity

#Programa principal
weight = float(input('Enter the weight: '))
height = float(input('Enter the height: '))
mmc = weight/(height**2)
if mmc < 18.5:
    print('Underweight')
elif (mmc >= 18.5) and mmc < 25:
    print('Ideal weight')
elif (mmc >= 25) and mmc <= 30:
    print('Overweight')
elif (mmc > 30) and mmc <= 40:
    print('Obesity')
elif mmc > 40:
    print('Morbid obesity')
print('MMC = {}'.format(mmc))