import os
from options import calculate_payment_breakdown, numrus, calculate_annuity_payment
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webcreditcal.settings")
STATIC = settings.STATIC_ROOT


def main():
    principal = float(input("Введите сумму кредита: "))
    annual_rate = float(input("Введите годовую процентную ставку (в виде десятичной дроби, например, 0.05 для 5%): "))
    months = int(input("Введите срок кредита в месяцах: "))

    breakdown_df = calculate_payment_breakdown(principal, annual_rate, months)
    print(breakdown_df)
    breakdown_df.to_csv(STATIC + 'loan_payment_breakdown.csv', index=False)
    print("\nДанные сохранены в 'loan_payment_breakdown.csv'")
    monthly_payment = calculate_annuity_payment(principal, annual_rate, months)
    print(numrus(monthly_payment))
    total = monthly_payment * months
    print(numrus(total))
if __name__ == "__main__":
    main()