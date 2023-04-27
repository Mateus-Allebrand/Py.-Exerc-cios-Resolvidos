#contagem regressiva com timer
import emoji
import time
n = emoji.emojize(":bomb:")
x =emoji.emojize(":collision:")
print('\n')
print(n)
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print(x)
print('Happy new Year!')
