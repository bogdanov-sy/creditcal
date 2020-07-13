from django.shortcuts import render
from django.http import HttpResponse

from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def insurance(request):
    return render(request, 'insurance/index.html', {})

def monthly_payment(s, g, n):
   i = int(g) / 100 / 12
   P = int(s) * (i + (i / (((1 + i) ** n) - 1)))
   return (P)

def calculatecredit(request):
    s = request.GET['creditAmount']
    ins = request.GET['insuranceAmount']
    grate = request.GET['annualRate']
    n = int(request.GET['creditTerm'])
    for k in range(1, 100, 1):
        var1 = monthly_payment((int(s) + int(ins)), grate, n)
        var2 = monthly_payment(s, k, n)
        if var2 >= var1:
            annualRateIns = str(k)
            monthlyPayment = str(float("{0:.1f}".format(var1)))
            overpayment = (monthly_payment((int(s) + int(ins)), grate, n) * n) - int(s)
            overpaymentStr = str(float("{0:.1f}".format(overpayment)))
            return render(request, 'insurance/creditcal.html', {'annualRateIns': annualRateIns, 'monthlyPayment' : monthlyPayment, 'overpaymentStr' : overpaymentStr})
            #return HttpResponse('Процент кредита:' + annualRateIns + 'Ежемесячный процент:' + monthlyPayment + 'Переплата:' +overpayment)