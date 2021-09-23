import numpy as np

def numrus (number):
    integer = int((float(number) % 1) * 100 // 1)
    fractional_part = float(number) // 1
    thousands_separator = '{0:,}'.format(int(fractional_part)).replace(',', ' ')
    px = str(thousands_separator) + ',' + str(integer)
    return(px)

def computation_monthly_payment(amount, annual_rate, credit_term):
   i = float(annual_rate) / 100 / 12
   P = float(amount) * (i + (i / (((1 + i) ** credit_term) - 1)))
   return(P)

def monthly_payment_percent(amount, monthly_payment, credit_term, annual_rate):
    sumpcttotal = 0
    for number in range(int(credit_term) - 1):
        sumpct = amount * ((annual_rate / 100) / 365 * 30.4166)
        amount = amount - (monthly_payment - sumpct)
        sumpcttotal = sumpcttotal + sumpct
    return (sumpcttotal)

def selection_annual_rate(amount, credit_term, monthly_payment):
    for k in np.arange(1, 100, 0.01):
        var1 = monthly_payment
        var2 = computation_monthly_payment(amount, k, credit_term)
        if var2 >= var1:
            annualRate = str(k)
            return(annualRate)