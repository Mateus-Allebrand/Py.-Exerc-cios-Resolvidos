currentyear = int(input('\033[1mEnter the current year: \033[m'))
birth = int(input('Enter the year of birth: '))
col = {'clear':'\033[m',
       'blue':'\033[1;34m',
       'red':'\033[1;31m',
       'green':'\033[1;32m',
       'grey':'\033[1;30m',
       'yellow':'\033[1;33m', }
difference = currentyear - birth
list = ['MIRIM','INFANTIL', 'JUNIOR', 'SÊNIOR','MASTER']
if difference <= 9:
    print('Belongs category to the: {}{}{}'.format(col['grey'], list[0], col['clear']))
elif ( difference > 9) and difference <= 14:
    print('Belongs category to the: {}{}{}'.format(col['yellow'], list[1],col['clear']))
elif (difference > 14) and difference <= 19:
    print('Belongs category to the: {}{}{}'.format(col['blue'], list[2],col['clear']))
elif (difference > 19) and difference <= 20:
    print('Belongs category to the: {}{}{}'.format(col['green'], list[3],col['clear']))
elif difference > 20:
    print('Belongs category to the: {}{}{}'.format(col['red'], list[4], col['clear']))

