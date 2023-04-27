#jogo de advinhação
import random
zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5
lista = [zero, one, two, three, four, five]
thinking = random.choice(lista)
user = int(input('Enter the number between 0 and 5: '))
print('Number sorted: {}\nNumber choiced the user: {}'.format(thinking, user))
if thinking == user:
    print('====CONGRATULATION!====\nYou choiced the númber right!')
else:
    print('You got the number wrong!\nTry Again!')






