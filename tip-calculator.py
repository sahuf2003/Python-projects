print("welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip_percent = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))
tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"each person should pay: ${final_amount}")
