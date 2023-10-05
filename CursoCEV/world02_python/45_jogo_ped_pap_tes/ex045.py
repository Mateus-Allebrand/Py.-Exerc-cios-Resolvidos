#Jogo pedra, papel e tesoura

#Programa principal
import random
print('==============LET THE GAMES BEGIN!===============\n')
hand = int(input('              [1] PAPER\n\n              [2] ROCK\n\n              [3] SCISSORS\n=================================================\n'))
a = 1
b = 2
c = 3
list = [a,b,c]
computer = random.choice(list)
col = {'clear':'\033[m',
       'red': '\033[1;31m'}
#igualdades
if (hand == 1) and computer == 1:
    print('Machine => PAPER\n\nYou => PAPER\n\nNobody Won!')
elif (hand == 2) and computer == 2:
    print('Machine => ROCK\n\nYou => ROCK\n\nNobody Won')    
elif (hand == 3) and computer == 3:
    print('Machine => SCISSORS\n\nYou => SCISSORS\n\nNobody Won')
    #hand = 3
elif (hand == 3) and computer == 1:
    print('Machine => PAPER\n\nYou => SCISSORS\n\nYou WIN!')
elif (hand == 3) and computer == 2:
    print('Machine => ROCK\n\nYou => SCISSORS\n\nYou Lose!')
    #hand rock and paper e v
elif (hand == 2) and computer == 1:
    print('Machine => PAPER\n\nYou => ROCK\n\nYou Lose!')
elif (hand == 1) and computer == 2:
    print('Machine => ROCK\n\nYou => PAPER\n\nYou Win!')
elif (hand == 2) and computer == 1:
    print('Machine => PAPER\n\nYou => ROCK\n\nYou Lose!')
    #machinescissers
elif (hand == 1) and computer == 3:
    print('Machine => SCISSORS\n\nYou => PAPER\n\nYou Lose!')
elif (hand == 2) and computer == 3:
    print('Machine => SCISSORS\n\nYou => ROCK\n\nYou Win!')
else:
    print('{} You have entered an invalid value {}\nTry again'.format(col['red'], col['clear']))