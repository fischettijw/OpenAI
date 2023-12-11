import tkinter as tk

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
        return None

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

def calculate_and_display_tax():
    income = float(income_entry.get())
    dependents = int(dependents_entry.get())
    filing_status = filing_status_var.get()
    tax = calculate_tax(income, dependents, filing_status)
    if tax is not None:
        result_label.config(text="Your federal income tax is: {:.2f}".format(tax))
    else:
        result_label.config(text="Error: Invalid filing status")

app = tk.Tk()
app.title("Federal Income Tax Calculator")

income_label = tk.Label(text="Enter your income:")
# income_label



income_label.pack()

income_entry = tk.Entry()
income_entry.pack()

dependents_label = tk.Label(text="Enter number of dependents:")
dependents_label.pack()

dependents_entry = tk.Entry()
dependents_entry.pack()

filing_status_label = tk.Label(text="Select filing status:")
filing_status_label.pack()

filing_status_var = tk.StringVar()
filing_status_var.set("single")

filing_status_options = ["single", "married_jointly", "married_separately", "head_of_household"]
for option in filing_status_options:
    tk.Radiobutton(app, text=option, variable=filing_status_var, value=option).pack()

calculate_button = tk.Button(text="Calculate", command=calculate_and_display_tax)
calculate_button.pack()

result_label = tk.Label(text="")
result_label.pack()

app.mainloop()
