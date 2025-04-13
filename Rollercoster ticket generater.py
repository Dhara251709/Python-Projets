print("Welcome to the Fun World Rollercoster Ride!")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("You can ride the Rollercoster.")
    age = int(input("What is your age?\n"))
    if age <= 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("opps!you can not take a ride of rollercoster.")