#verifica o valor conforme a forma de pagammento


#Programa principal
productvalue = float(input('Enter rhe product value: '))
condiction = int(input('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-CHOSE PAYMENT METHOD:=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n                      =>[1]<= Cash Payment!\n\n                      =>[2]<= Debit Card!\n\n                      =>[3]<= Credit Card! up to two times\n\n                      =>[4]<= Credit Card! In three installments or more.\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n'))
desc = 0
if condiction == 1:
    desc = productvalue*(10/100)
    print('O seu produto custará: {:.2f}'.format(productvalue - desc))
elif condiction == 2:
    desc = productvalue * (5/100)
    print('O seu produto custará: {:.2f}'.format(productvalue - desc))
elif condiction == 3:
    print('O seu produto custará: {}'.format(productvalue))
elif condiction == 4:
    desc = productvalue * (20/100)
    print('O seu produto custará: {}'.format(productvalue + desc))
else:
    print('Digito inválido')