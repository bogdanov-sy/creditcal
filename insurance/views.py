from django.shortcuts import render
from django.http import HttpResponse

from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def insurance(request):
    return render(request, 'insurance/index.html', {})

def monthly_payment(s, g, n):
   i = float(g) / 100 / 12
   P = float(s) * (i + (i / (((1 + i) ** n) - 1)))
   return (P)

def numrus (x):
    z = int((float(x) % 1)*100 // 1)
    y = float(x) // 1
    p = '{0:,}'.format(int(y)).replace(',', ' ')
    px = str(p) + ',' + str(z)
    return(px)

def calculatecredit(request):
    s = float(request.GET['creditAmount'])
    ins = float(request.GET['insuranceAmount'])
    grate = float(request.GET['annualRate'])
    n = float(request.GET['creditTerm'])
    for k in range(1, 100, 1):
        var1 = monthly_payment((int(s) + int(ins)), grate, n)
        var2 = monthly_payment(s, k, n)
        if var2 >= var1:
            annualRateIns = str(k)
            monthlyPayment = str(numrus(float("{0:.1f}".format(var1))))
            overpayment = (monthly_payment((int(s) + int(ins)), grate, n) * n) - int(s)
            overpaymentStr = str(numrus(float("{0:.1f}".format(overpayment))))
            overpaymentPercent = str(int(overpayment / s * 100))
            return render(request, 'insurance/creditcal.html', {'annualRateIns': annualRateIns, 'monthlyPayment' : monthlyPayment, 'overpaymentStr' : overpaymentStr, 'overpaymentPercent' : overpaymentPercent})
            #return HttpResponse('Процент кредита:' + annualRateIns + 'Ежемесячный процент:' + monthlyPayment + 'Переплата:' +overpayment)