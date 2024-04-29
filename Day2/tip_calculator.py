print("Welcome to the tip calculator!")
bill = float(input("Enter your total bill : $"))
tip = int(input("How much tip do you want to give -> 10% , 12% , 15% ?"))
split = int(input("How many people to split the bill : "))

tip_percent = tip / 100
total_tip = tip_percent * bill
total_bill = bill + total_tip
pay = total_bill / split
print("You should pay : $", pay)
