print("Thank you for choosing for service!")

size = input("Enter size of the pizza --> S or M or L")
if size == "s" or "S":
    bill = 15
    print("Your bill is 15$")
    add_pepperoni = input("Do you want pepperoni? --> Y or N")
    if add_pepperoni == "Y" or "y":
        bill += 2
        print("Your bill is : ",bill )
    extra_cheese = input("Do you want extra cheese? --> Y or N")
    if extra_cheese == "Y" or "y":
        bill += 1
        print("Your bill is : ",bill)
elif size == "m" or "M":
    bill = 20
    print("Your bill is 20$")
    add_pepperoni = input("Do you want pepperoni? --> Y or N")
    if add_pepperoni == "Y" or "y":
        bill += 3
        print("Your bill is : ",bill )
    extra_cheese = input("Do you want extra cheese? --> Y or N")
    if extra_cheese == "Y" or "y":
        bill += 1
        print("Your bill is : ",bill)
elif size == "L" or "l":
    bill = 25
    print("Your bill is 20$")
    add_pepperoni = input("Do you want pepperoni? --> Y or N")
    if add_pepperoni == "Y" or "y":
        bill += 3
        print("Your bill is : ",bill )
    extra_cheese = input("Do you want extra cheese? --> Y or N")
    if extra_cheese == "Y" or "y":
        bill += 1
        print("Your bill is : ",bill)