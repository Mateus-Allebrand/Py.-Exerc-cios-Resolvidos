#verifica situação do aluno, conforme a media dele

#Programa principal
n1 = float(input('Enter the first note: '))
n2 = float(input('Enter the second note: '))
average = (n1 + n2) / 2
collor = {'clear':'\033[m',
          'red':'\033[1;31m',
          'green':'\033[1;32m',
          'blue':'\033[1;34m'}
if average < 5:
    print('Your grade is: {}{}{}\n{}-_-_-_-_-_=>YOU FAILED!<=-_-_-_-_-_-{}'.format(collor['red'],average,collor['clear'],collor['red'],collor['clear']))
elif (average >= 5) and average <= 6.9:
    print('Your grade is: {}{}{}\n{}=>{}{}You have to do the recovery!{}'.format(collor['blue'], average, collor['clear'],collor['green'],collor['clear'],collor['blue'],collor['clear']))
elif average >= 7:
    print('{}=-=-=-=-={}{}=>CONGRATULATIONS!<={}{}=-=-=-=-={}\n=-=-=-=-=-Your grade is: {}{}{}=-=-=-=-=-\n-=-=-=-=-=-{}You are approved!{}=-=-=-=-=-'.format(collor['blue'],collor['clear'],collor['green'],collor['clear'],collor['blue'],collor['clear'],collor['green'], average,collor['clear'],collor['green'],collor['clear']))
