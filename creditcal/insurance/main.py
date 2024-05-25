from options import calculatecredit

def main():
    amount_of_credit = float(input("Amount of credit: "))
    insurance = float(input("Insurance: "))
    monthly_payment = float(input("Monthly payment: "))
    annual_rate = float(input("Annual rate: "))
    credit_term = float(input("credit_term: "))
    result = calculatecredit(amount_of_credit, insurance, monthly_payment, annual_rate, credit_term)
    print(result)


main()


def main():
    principal = float(input("Введите сумму кредита: "))
    annual_rate = float(input("Введите годовую процентную ставку (в виде десятичной дроби, например, 0.05 для 5%): "))
    months = int(input("Введите срок кредита в месяцах: "))

    breakdown_df = calculate_payment_breakdown(principal, annual_rate, months)
    print(breakdown_df)
    breakdown_df.to_csv("loan_payment_breakdown.csv", index=False)
    print("\nДанные сохранены в 'loan_payment_breakdown.csv'")

if __name__ == "__main__":
    main()