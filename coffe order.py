print("Hello dear vulueable Custmer, Welcome to the Bohji cafe!")
Type = input("Hot or Cold coffe?")
size = input("What size coffe Do you want? S,M,L :")
Cream = input("Do you want Cream? Y or N :")
extra_flavour_syrup = input("Do you want extra flavour? Y or N :")
extra_icecream = input("Want some icecrem on it?")
tip = input("Would you like to give a Tip! Y or N:")
tip_for_coffe = 1
bill = 0
if size == "S":
    bill +=  5
elif size == "M":
    bill += 8
elif size  == "L":
    bill += 12
else:
    print("Please choose the currect size!")
if Cream == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    else :
        bill += 4
if extra_flavour_syrup == "Y":
    bill += 1
if extra_icecream == "Y":
    bill += 2
if tip == "Y":
    bill += tip_for_coffe
    
print(f"Your final bill is: $ {bill}.")