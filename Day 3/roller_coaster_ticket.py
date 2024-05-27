height = int(input("Enter your height : "))
if height > 120:
    print("You can ride the roller-coaster!")
    age = int(input("Enter your age : "))
    if age <= 12:
        ticket = 5
        print("Your ticket will be 5$")
    elif age <= 18:
        ticket = 7
        print("Your ticket will be 7$")

    else:
        ticket = 12
        print("Your ticket will be 12$")
        
    photo_ticket = input("Do you want a photo-ticket? --> Y or N")
    if photo_ticket == "Y" or "y":
        ticket += 3
    print("Your ticket price will be ",ticket)
else:
    print("Sorry you can't ride!")