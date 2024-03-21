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