import math


def calculate_months_to_target(principal, monthly_contribution, annual_rate, target_amount):
    # Convert annual rate to monthly and decimal
    monthly_rate = annual_rate / 12 / 100

    # Define the target amount and initial principal
    target = target_amount
    principal = principal

    # Initialize the number of months
    months = 0

    # Loop until the principal grows to the target amount
    while principal < target:
        # Update principal with interest and monthly contribution
        principal = principal * (1 + monthly_rate) + monthly_contribution
        months += 1

    return months


# Example parameters
initial_principal = 360000
monthly_contribution = 0
annual_interest_rate = 24
target_amount = 6000000

# Calculate the number of months
months_needed = calculate_months_to_target(initial_principal, monthly_contribution, annual_interest_rate, target_amount)
def convert_months_to_years_and_months(months):
    years = months // 12
    remaining_months = months % 12
    return years, remaining_months

years, remaining_months = convert_months_to_years_and_months(months_needed)

print(f"Number of months needed: {months_needed} for initial principle {initial_principal} with interest rate of {annual_interest_rate} to make {target_amount}")
print(f"Equivalent to {years} years and {remaining_months} months")
