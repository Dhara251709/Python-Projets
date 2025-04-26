print("Hello dear vulueable Custmer, Welcome to the La'Pilanos Pizza!")
size = input("What size pizza Do you want? S,M,L :")
Topping = input("Do you want Toppings on Your Pizza? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :")
bill = 0
if size == "S":
    bill +=  15
elif size == "M":
    bill += 20
elif size  == "L":
    bill += 25
else:
    print("Please choose the currect size!")
if Topping == "Y":
    if size == "S":
        bill += 2
    else :
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: $ {bill}.")
