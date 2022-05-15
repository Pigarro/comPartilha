print("Welcome to the tip Calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100
split_bill_in = float(input("How many people to split the bill? "))

final_bill = (total_bill * tip_percentage + total_bill) / split_bill_in
print(f"Each person should pay: {final_bill:.2f} dolars")