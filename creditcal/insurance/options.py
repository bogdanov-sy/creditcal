import numpy as np
import pandas as pd
import scipy.optimize as optimize

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


def calculate_annuity_payment(principal, annual_rate, months):
    """
    Calculate the monthly annuity payment for a loan.
    
    :param principal: The loan amount (principal).
    :param annual_rate: The annual interest rate (as a decimal).
    :param months: The total number of monthly payments (loan term in months).
    :return: The monthly annuity payment.
    """
    monthly_rate = annual_rate / 12  # Convert annual rate to monthly rate
    annuity_factor = (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    monthly_payment = principal * annuity_factor
    return monthly_payment


def calculate_payment_breakdown(principal, annual_rate, months):
    """
    Calculate the monthly payment breakdown into principal and interest components.
    
    :param principal: The loan amount (principal).
    :param annual_rate: The annual interest rate (as a decimal).
    :param months: The total number of monthly payments (loan term in months).
    :return: A pandas DataFrame with breakdown of each payment.
    """
    monthly_payment = calculate_annuity_payment(principal, annual_rate, months)
    monthly_rate = annual_rate / 12
    balance = principal

    data = {
        "Month": [],
        "Principal Payment": [],
        "Interest Payment": [],
        "Total Payment": [],
        "Remaining Balance": []
    }

    for month in range(1, months + 1):
        interest_payment = balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment

        data["Month"].append(month)
        data["Principal Payment"].append(principal_payment)
        data["Interest Payment"].append(interest_payment)
        data["Total Payment"].append(monthly_payment)
        data["Remaining Balance"].append(balance)

    df = pd.DataFrame(data)
    return df

def calculate_interest_rate(principal, monthly_payment, months):
    """
    Calculate the annual interest rate given the principal, monthly payment, and number of months.
    
    :param principal: The loan amount (principal).
    :param monthly_payment: The monthly annuity payment.
    :param months: The total number of monthly payments (loan term in months).
    :return: The annual interest rate as a decimal.
    """
    def f(rate):
        return monthly_payment - principal * rate * (1 + rate)**months / ((1 + rate)**months - 1)

    # Initial guess for the monthly rate
    monthly_rate_initial_guess = 0.05 / 12
    # Use a root-finding algorithm to solve for the monthly interest rate
    monthly_rate = optimize.newton(f, monthly_rate_initial_guess)
    # Convert monthly rate to annual rate
    annual_rate = monthly_rate * 12
    return annual_rate
        


def calculatecredit(amount, insurance, monthly_payment, annual_rate, credit_term):
    if amount != 0 and  monthly_payment != 0 and annual_rate != 0 and credit_term != 0:

        real_rate = selection_annual_rate(amount, credit_term, monthly_payment)
        s_real = monthly_payment * credit_term
        overpaiment = str(s_real - amount)
        overpaymentPercent = str((float(overpaiment) / float(amount)) * 100)

        real_rateStr = str(numrus(float("{0:.1f}".format(float(real_rate)))))
        insStr = str(numrus(float("{0:.1f}".format(float(insurance)))))
        monthly_paymentStr = str(numrus(float("{0:.1f}".format(float(monthly_payment)))))
        overpaimentStr = str(numrus(float("{0:.1f}".format(float(overpaiment)))))
        overpaymentPercentStr = str(numrus(float("{0:.1f}".format(float(overpaymentPercent)))))

        context = {'annualRateIns': real_rateStr, 'monthlyPayment': monthly_paymentStr,
                        'overpaymentStr': overpaimentStr,
                        'overpaymentPercent': overpaymentPercentStr, 'insuranceStr': insStr}

    else:
        context = None

    return context


