a = int(input('Enter the first straight: '))
b = int(input('Enter the second straight: '))
c = int(input('Enter the tird straight: '))
if (a == b) and b == c:
    print('Equilateral tringle ')
elif ((a == b) and a != c) or ((a == c) and a != b ) or ((b == c) and b != a):
    print('Isosceles triangle')
elif (((a != b) and a != c) and c != b):
    print('Scalene triangle')