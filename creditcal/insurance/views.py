from django.shortcuts import render
from insurance.options import calculate_payment_breakdown, calculatecredit
import os
from django.http import FileResponse, Http404
from django.conf import settings

def download_file(request, filename):
    file_path = os.path.join(settings.STATIC_ROOT, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
    else:
        raise Http404("File not found")

def generate_and_save_text(amount, annual_rate, months):
    # Генерация текста
    breakdown_df = calculate_payment_breakdown(amount, annual_rate, months)
    print(breakdown_df)
    file_path = os.path.join(settings.STATIC_ROOT, 'loan_payment_breakdown.csv')
    breakdown_df.to_csv(file_path, sep=";", index=False)
    print("\nДанные сохранены в 'loan_payment_breakdown.csv'")




# Create your views here.
def index(request):
    return render(request, 'insurance/index.html', {})

def calculate(request):
    amount = int(request.GET['creditAmount'])
    insurance = int(request.GET['insuranceAmount'])
    monthly_payment = float(request.GET['monthlyPayment'])
    annual_rate = int(request.GET['annualRate'])
    months = int(request.GET['creditTerm'])

    generate_and_save_text(amount + insurance, annual_rate / 100, months)

    context = calculatecredit(amount, insurance, monthly_payment, annual_rate, months)

    print(context)

    if context is None:
        return render(request, 'insurance/index.html', {'error': 'Не указаны сумму и ежемесячный платеж'})
    else:
        return render(request, 'insurance/creditcal.html', context)


