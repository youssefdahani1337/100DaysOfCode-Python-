print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_split = int(input("How many people to split the bill? "))
total_bill_with_tip = total_bill * (1 + tip_percentage / 100)
bill_per_person = total_bill_with_tip / people_split
bill_per_person_str = "{:.2f}".format(round(bill_per_person, 2))
print(f"Each person should pay: ${bill_per_person_str}")
