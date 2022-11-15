import os

os.system('cls')

userInput = input('Are you from Canada? [Y/n] ').casefold()
fromCanada = True if userInput == 'y' or userInput == '' else False
theProvinceInCanada = '-'
tax = 0

if fromCanada:
    os.system('cls')
    print('Provinces')
    print('===============')
    print('1. Alberta')
    print('2. Ontario')
    print('3. New Brunswick')
    print('4. Nova Scotia')
    print('5. Other Provinces')
    theProvinceInCanada = input(f'\nSelect your province. [1-5] ')

    if theProvinceInCanada is '1':
        tax = 0.05
        theProvinceInCanada = 'Alberta'
    elif theProvinceInCanada is '2' or theProvinceInCanada is '3' or theProvinceInCanada is '4':
        tax = 0.13

        if theProvinceInCanada is '2':
            theProvinceInCanada = 'Ontario'
        elif theProvinceInCanada is '3':
            theProvinceInCanada = 'New Brunswick'
        elif theProvinceInCanada is '4':
            theProvinceInCanada = 'Nova Scotia'
    elif theProvinceInCanada is '5':
        tax = 0.11
        theProvinceInCanada = 'Other Provinces'

os.system('cls')
orderTotal = float(input('What is your total spending? '))

if fromCanada:
    orderTotalWTax = orderTotal + (orderTotal * tax / 100)
else:
    orderTotalWTax = orderTotal

os.system('cls')
print(f'Total spending: {orderTotal}')
print(f'Tax ({theProvinceInCanada}): {tax}%')
print('====================================')
print(f'Total + Tax : {orderTotalWTax}')
