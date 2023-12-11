def calculate_tax(income, dependents, filing_status):
    if filing_status == "single":
        standard_deduction = 12200 + 2440 * dependents
    elif filing_status == "married_jointly":
        standard_deduction = 24400 + 2440 * dependents
    elif filing_status == "married_separately":
        standard_deduction = 12200 + 2440 * dependents
    elif filing_status == "head_of_household":
        standard_deduction = 18350 + 2440 * dependents
    else:
        print("Error: Invalid filing status")
        return

    taxable_income = max(0, income - standard_deduction)

    if taxable_income <= 9525:
        tax = taxable_income * 0.1
    elif taxable_income <= 38700:
        tax = 9525 * 0.1 + (taxable_income - 9525) * 0.12
    elif taxable_income <= 82500:
        tax = 9525 * 0.1 + (38700 - 9525) * 0.12 + (taxable_income - 38700) * 0.22
    elif taxable_income <= 157500:
        tax = 9525 * 0.1 + (38700 - 9525) * 0.12 + (82500 - 38700) * 0.22 + (taxable_income - 82500) * 0.24
    elif taxable_income <= 200000:
        tax = 9525 * 0.1 + (38700 - 9525) * 0.12 + (82500 - 38700) * 0.22 + (157500 - 82500) * 0.24 + (taxable_income - 157500) * 0.32
    elif taxable_income <= 500000:
        tax = 9525 * 0.1 + (38700 - 9525) * 0.12 + (82500 - 38700) * 0.22 + (157500 - 82500) * 0.24 + (200000 - 157500) * 0.32 + (taxable_income - 200000) * 0.35
    else:
        tax = 9525 * 0.1 + (38700 - 9525) * 0.12 + (82500 - 38700) * 0.22 + (157500 - 82500) * 0.24 + (200000 - 157500) * 0.32 + (500000 - 200000) * 0.35 + (taxable_income - 500000) * 0.37
    return tax

income = float(input("Enter your income: "))
dependents = int(input("Enter the number of dependents: "))
filing_status = input("Enter your filing status (single, married_jointly, married_separately, head_of_household): ")
tax = calculate_tax(income, dependents, filing_status)
if tax is not None:
    print("Your federal income tax is:", tax)
