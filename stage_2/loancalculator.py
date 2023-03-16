from math import ceil
loan = int(input('Enter the loan principal:'))
x = input('''What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:''')

def payment(principal, months):
    return ceil(principal/months)

def lastpayment(principal, months):
    return principal - (months - 1) * payment(principal, months)

if x == "m":
    y = int(input('Enter the monthly payment:'))
    pay = payment(loan, y)
    if pay <= 1:
        print(f"It will take {pay} month to repay the loan")
    elif pay > 1:
        print(f"It will take {pay} months to repay the loan")
elif x == "p":
    mon = int(input('Enter the number of months:'))
    pay = payment(loan, mon)
    lpay = lastpayment(loan, mon)
    print(f'Your monthly payment = {pay} and the last payment = {lpay}.')