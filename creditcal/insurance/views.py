from django.shortcuts import render
from insurance.options import calculatecredit

from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def index(request):
    return render(request, 'insurance/index.html', {})

def calculate(request):
    amount = float(request.GET['creditAmount'])
    insurance = float(request.GET['insuranceAmount'])
    monthly_payment = float(request.GET['monthlyPayment'])
    annual_rate = float(request.GET['annualRate'])
    credit_term = float(request.GET['creditTerm'])

    context = calculatecredit(amount, insurance, monthly_payment, annual_rate, credit_term)

    if context is None:
        return render(request, 'insurance/index.html', {'error': 'Не указаны сумму и ежемесячный платеж'})
    else:
        return render(request, 'insurance/creditcal.html', context)


