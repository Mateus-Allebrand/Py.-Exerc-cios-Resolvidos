km =float(input('Enter the distance of your trip in kilometers: '))
higher = 0.45
bottom = 0.50
if km <= 200:
    km = km * bottom
    print('Your trip will cost $ {} Dollars'.format(km))
else:
    km = km * higher 
    print('Your trip will cost $ {} Dollars'.format(km))