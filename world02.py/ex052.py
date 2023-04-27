#verifique se é um número primo 
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
n = int(input('Digite um número: '))
col = {'Yellow': '\033[1;33m','clear':'\033[m'}
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(col['Yellow'])
        tot += 1
    else:
        print(col['clear'])
    print('{} '.format(c),end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))