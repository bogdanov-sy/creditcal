from django.shortcuts import render
from . import options as opt
import sys

from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def insurance(request):
    return render(request, 'insurance/index.html', {})

def calculatecredit(request):
    amount = float(request.GET['creditAmount'])
    insurance = float(request.GET['insuranceAmount'])
    monthly_payment = float(request.GET['monthlyPayment'])
    annual_rate = float(request.GET['annualRate'])
    credit_term = float(request.GET['creditTerm'])

    if amount == 0:
        if monthly_payment == 0:
            sys.exit("Невозможно определить параметры кредита")
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

    return render(request, 'insurance/creditcal.html', {'annualRateIns': real_rateStr, 'monthlyPayment' : monthly_paymentStr, 'overpaymentStr' : overpaimentStr, 'overpaymentPercent' : overpaymentPercentStr, 'insuranceStr' : insStr})
