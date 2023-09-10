import numpy as np

amount = 0
insurance = 0
monthly_payment = 0
annual_rate = 0
credit_term = 0


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
        


def calculatecredit(amount, insurance, monthly_payment, annual_rate, credit_term):
    if amount != 0 and  monthly_payment != 0 and annual_rate != 0 and credit_term != 0:
    
    
    if amount == 0:
        if monthly_payment == 0:
            break
        else:
            amount = (monthly_payment * credit_term) - insurance
        print(amount)

    if monthly_payment == 0:
        monthly_payment = opt.computation_monthly_payment(float(amount + insurance), float(annual_rate), int(credit_term))

    if insurance == 0:
        monthly_payment_real = opt.computation_monthly_payment(amount, annual_rate, credit_term)
        i = float(annual_rate) / 100 / 12
        insurance = (monthly_payment - monthly_payment_real) / (i + (i / (((1 + i) ** credit_term) - 1)))

    real_rate = opt.selection_annual_rate(amount, credit_term, monthly_payment)
    s_real = monthly_payment * credit_term
    overpaiment = str(s_real - amount)
    overpaymentPercent = str((float(overpaiment) / float(amount)) * 100)

    real_rateStr = str(opt.numrus(float("{0:.1f}".format(float(real_rate)))))
    insStr = str(opt.numrus(float("{0:.1f}".format(float(insurance)))))
    monthly_paymentStr = str(opt.numrus(float("{0:.1f}".format(float(monthly_payment)))))
    overpaimentStr = str(opt.numrus(float("{0:.1f}".format(float(overpaiment)))))
    overpaymentPercentStr = str(opt.numrus(float("{0:.1f}".format(float(overpaymentPercent)))))

    print("Реальный процент: " + str(real_rateStr))
    print("Страховка: " + str(insStr))
    print("Общая сумма переплаты: " + str(overpaimentStr))

    return 