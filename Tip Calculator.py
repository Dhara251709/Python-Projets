print("Welcome to the the Tip Calculator!")
bill =float( input("What wah your total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n"))
pepole = int(input("How many pepole to split the bill?\n"))
tip_as_percent = tip/100
total_tip_amount = bill*tip_as_percent
total_bill = bill+total_tip_amount
bill_per_person = total_bill/pepole
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: $ {final_amount}")