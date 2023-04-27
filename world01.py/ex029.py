#aplica multa
speed = float(input('Enter the speed of the car: '))
speedlimit = 80
cal= (speed - speedlimit)
multa = 0
if cal <=0:
    multa = multa + 0
else:
    multa = (multa + cal) * 7
    print('YOU WERE FINED FOR SPEEDNING!\n you owe $ {:.2f} Dollars'. format(multa))

    

