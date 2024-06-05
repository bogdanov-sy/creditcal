from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def refinance(request):
    return render(request, 'refinance/index.html', {})


def numrus(x):
    z = int((float(x) % 1) * 100 // 1)
    y = float(x) // 1
    p = '{0:,}'.format(int(y)).replace(',', ' ')
    px = str(p) + ',' + str(z)
    return (px)


def monthly_payment(s, g, n):
    i = g / 100 / 12
    P = s * (i + (i / (((1 + i) ** n) - 1)))
    return (P)


def monthly_payment_percent(s, z, n, grate):
    sumpcttotal = 0
    for number in range(int(n) - 1):
        sumpct = s * ((grate / 100) / 365 * 30.4166)
        s = s - (z - sumpct)
        sumpcttotal = sumpcttotal + sumpct
    return (sumpcttotal)


def refinancecalc(request):
    s1 = float(request.GET['creditAmount1'])  # s1 = float(input('Введите сумму кредита 1: '))
    ins1 = float(request.GET['insuranceAmount1'])  # ins1 = float(input('Введи сумму страховки 1: '))
    grate1 = float(request.GET['annualRate1'])  # grate1 = float(input('Введите годовую ставку 1: '))
    n1 = float(request.GET['creditTerm1'])  # n1 = input('Введите срок кредита (в месяцах) 1: ')
    n3 = float(request.GET['creditTerm3'])  # n3 = input('Введите месяц,с которого будет рефинансирование 1: ')
    s2 = float(request.GET['creditAmount2'])  # s2 = float(input('Введите сумму кредита 2: '))
    ins2 = float(request.GET['insuranceAmount2'])  # ins2 = float(input('Введи сумму страховки 2: '))
    grate2 = float(request.GET['annualRate2'])  # grate2 = float(input('Введите годовую ставку 2: '))
    n2 = float(request.GET['creditTerm2'])  # n2 = input('Введите срок кредита (в месяцах) 2: ')
    var11 = monthly_payment((float(s1) + float(ins1)), grate1, int(n1))
    var21 = monthly_payment((float(s2) + float(ins2)), grate2, int(n2))
    mpp1 = monthly_payment_percent(s1, var11, n3, grate1)
    overpay1 = monthly_payment(s1, grate1, int(n1)) * int(n1) - s1 + ins1
    overpay2 = monthly_payment(s2, grate2, int(n2)) * int(n2) - s2 + ins2
    X = float((overpay1 - mpp1) - overpay2)
    overpaymentStr = str(numrus(float("{0:.1f}".format(X))))
    return render(request, 'refinance/refinancecalc.html', {'overpaymentStr': overpaymentStr})
    # return HttpResponse('Процент кредита:' + annualRateIns + 'Ежемесячный процент:' + monthlyPayment + 'Переплата:' +overpayment)
