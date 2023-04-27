salary = float(input("Enter the employee's salary: "))
if salary <= 1250:
    salaryincrease = (salary * 15) / 100
    salary = salary + salaryincrease
else:
    salaryincrease = (salary * 10) / 100
    salary = salaryincrease + salary
print('The amount of your raise is $ {} dollars, your salary is now $ {} dollars'.format(salaryincrease, salary))