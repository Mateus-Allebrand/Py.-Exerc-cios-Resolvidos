today = int(input('Enter the current year: '))
yearbirth = int(input('Enter the year of birth: '))
difference = today - yearbirth
enlist =  18
collors = {'red':'\033[1;31m','clear':'\033[m', 'green':'\033[1;32m'}
if difference < enlist:
    print('Must enlist in \033[1;44m {} \033[m years!\nYou must enlist in the year \033[1;44m {} \033[m'.format(enlist - difference,(enlist - difference)+today))
elif difference == enlist:
    print("=================================================================================================================\n{}=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=CONGRATULATIONS{}-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n=================================================================================================================\nYou're old enough to enlist!\nGo to the nearest military gartel and enlist!\n{}=-=-=-ATTENTION!!!-=-=-=\nDon't miss the deadline!{}".format(collors['green'], collors['clear'],collors['red'],collors['clear']))
elif difference > enlist:
    print("==================================================================================================\n{}=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=ATTENCION!!!-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-={}\n==================================================================================================\nYou didn't register on the correct date.\ngo to the nearest military unit and provide clarification!\n{}You should have enlisted in the year {}{} ".format(collors['red'],collors['clear'],collors['red'],((difference - enlist)-today)*-1,collors['clear']))