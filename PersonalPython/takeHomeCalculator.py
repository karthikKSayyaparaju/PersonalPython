def calculate_tax(income, brackets):
    """
    Calculate tax based on income and tax brackets.

    Parameters:
    - income: Annual income
    - brackets: List of tuples where each tuple contains (threshold, rate)

    Returns:
    - Total tax
    """
    tax = 0
    prev_threshold = 0

    for threshold, rate in brackets:
        if income > threshold:
            tax += (min(income, threshold) - prev_threshold) * rate
            prev_threshold = threshold
        else:
            tax += (income - prev_threshold) * rate
            break

    return tax


def calculate_take_home_pay(gross_salary, federal_brackets, state_brackets, social_security_rate, medicare_rate,
                            contribution_percentage, healthcare_amount, hsa_amount, social_security_limit,
                            contribution_limit, num_paychecks_per_year=24):
    """
    Calculate the take-home pay per paycheck after accounting for various taxes and deductions.

    Parameters:
    - gross_salary: Annual gross salary
    - federal_brackets: List of federal tax brackets (threshold, rate)
    - state_brackets: List of state tax brackets (threshold, rate)
    - social_security_rate: Social Security tax rate
    - medicare_rate: Medicare tax rate
    - contribution_percentage: 401(k) contribution percentage
    - healthcare_amount: Amount deducted for health insurance per paycheck
    - hsa_amount: Fixed HSA contribution amount per paycheck
    - social_security_limit: Maximum income subject to Social Security tax
    - contribution_limit: Maximum annual 401(k) contribution limit
    - num_paychecks_per_year: Number of paychecks per year (default is 26 for biweekly)

    Returns:
    - Take-home pay per paycheck
    """
    # Calculate annual 401(k) contribution
    annual_401k_contribution = min(gross_salary * contribution_percentage, contribution_limit)

    # Calculate total HSA contribution
    annual_hsa_contribution = hsa_amount * num_paychecks_per_year

    # Calculate taxable income after 401(k) and HSA contributions
    taxable_income = gross_salary - annual_401k_contribution - annual_hsa_contribution

    # Calculate federal and state income taxes based on brackets
    federal_tax = calculate_tax(taxable_income, federal_brackets)
    state_tax = calculate_tax(taxable_income, state_brackets)

    # Calculate Social Security and Medicare taxes
    social_security_taxable_income = min(gross_salary, social_security_limit)
    social_security_tax = social_security_taxable_income * social_security_rate
    medicare_tax = gross_salary * medicare_rate

    total_annual_taxes = federal_tax + social_security_tax + medicare_tax + state_tax

    # Calculate annual take-home pay
    annual_take_home_pay = gross_salary - total_annual_taxes - annual_401k_contribution - annual_hsa_contribution - (
                healthcare_amount * num_paychecks_per_year)

    # Calculate take-home pay per paycheck
    take_home_pay_per_paycheck = annual_take_home_pay / num_paychecks_per_year

    return take_home_pay_per_paycheck




# Federal tax brackets (2024)
federal_brackets = [
    (11000, 0.10),  # 10% on income up to $11,000
    (44725, 0.12),  # 12% on income between $11,001 and $44,725
    (95375, 0.22),  # 22% on income between $44,726 and $95,375
    (182100, 0.24),  # 24% on income between $95,376 and $182,100
    (231250, 0.32),  # 32% on income between $182,101 and $231,250
    (578125, 0.35),  # 35% on income between $231,251 and $578,125
    (float('inf'), 0.37)  # 37% on income over $578,125
]

# Georgia state tax brackets (2024)
georgia_brackets = [
    (750, 0.01),  # 1% on income up to $750
    (2250, 0.02),  # 2% on income between $751 and $2,250
    (3750, 0.03),  # 3% on income between $2,251 and $3,750
    (5250, 0.04),  # 4% on income between $3,751 and $5,250
    (7000, 0.05),  # 5% on income between $5,251 and $7,000
    (float('inf'), 0.0575)  # 5.75% on income over $7,000
]

florida_brackets = [
    # (750, 0.01),  # 1% on income up to $750
    # (2250, 0.02),  # 2% on income between $751 and $2,250
    # (3750, 0.03),  # 3% on income between $2,251 and $3,750
    # (5250, 0.04),  # 4% on income between $3,751 and $5,250
    # (7000, 0.05),  # 5% on income between $5,251 and $7,000
    (float('inf'), 0)  # 5.75% on income over $7,000
]


# Example usage:
gross_salary = 182000  # Example annual gross salary
social_security_rate = 0.062
medicare_rate = 0.0145
contribution_percentage = 0.03
healthcare_amount = -50  # Example health insurance deduction per paycheck
hsa_amount = 110  # Example fixed HSA contribution amount per paycheck
social_security_limit = 168600  # 2024 limit for Social Security tax
contribution_limit = 23000  # 2024 limit for 401(k) contributions

take_home_pay = calculate_take_home_pay(gross_salary, federal_brackets,
                                        florida_brackets,
                                        social_security_rate,
                                        medicare_rate, contribution_percentage, healthcare_amount, hsa_amount,
                                        social_security_limit,
                                        contribution_limit)

print(f"Gross Pay : ${gross_salary:.2f}")
print(f"Take-home pay per paycheck: ${take_home_pay:.2f}")
per_year_take_home = take_home_pay*24
per_month_take_home = take_home_pay*2
print(f"Take-home pay per month: ${per_month_take_home:.2f}")
print(f"Take-home pay per year: ${per_year_take_home:.2f}")
