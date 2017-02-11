total = 155.60
tax_percent = .075
tip_percent = .15

tax = total * tax_percent
tip = total * tip_percent
total_after_tax_and_tip = total + tax + tip

# Use the str() function to convert a number into a string.
print("The meal cost $" + str(total))
print("Tax is $" + str(tax))
print("Tip is $" + str(tip))
print("Total bill = $" + str(total_after_tax_and_tip))
