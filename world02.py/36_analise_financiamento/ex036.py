#Analise de financiamento

#Programa Principal
homevalue = float(input("What's the value of the house? "))
salary = float(input("Whats the salary value of the possible buyer: "))
timeinmonth = int(input("How many months will you pay: "))
installment = homevalue / timeinmonth
compromissed = salary * (30/100)
collors = {'azul':'\033[1;34m','clear':'\033[m'}
if installment > compromissed:
    print("You don't buy house")
elif installment <= compromissed:
    print("{}Congratulations!{} you can buy the house!".format(collors["azul"], collors["clear"]))
print(compromissed)
print(installment)

