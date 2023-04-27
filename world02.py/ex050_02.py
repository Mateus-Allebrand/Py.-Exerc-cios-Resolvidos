#somando os números pares
i = 0
for c in range(0, 6):
    n = int(input('Enter a number: '))
    if (n % 2) != 0:
        i = i + n
print(i)
