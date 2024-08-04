cost = float(input("What is the cost? "))
tax_rate = float(input("What is the tax rate? "))

tax_amount = cost * (tax_rate / 100)
total_cost = tax_amount + cost

print(f"Tax: ${tax_amount:.2f}")
print(f"Total Cost: ${total_cost:.2f}")