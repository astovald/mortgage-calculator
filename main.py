print("Mortgage calculator")

def mortgage_calculator(amount, duration_years):
    monthly_payment = (amount / duration_years) / 12
    return monthly_payment

loan_amount = int(input("Enter loan amount: "))
loan_years = int(input("Enter loan duration in years: "))

result = mortgage_calculator(loan_amount, loan_years)

print(f"Monthly payment for this loan is {result:.2f}€")


