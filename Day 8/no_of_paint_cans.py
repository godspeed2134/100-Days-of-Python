import math


def paint_calc(height, width, coverage=5):
    no_of_cans = (height * width) / coverage
    round_up = math.ceil(no_of_cans)
    print("You will need", round_up, "cans")


test_h = int(input("Enter height : "))
test_w = int(input("Enter width : "))

paint_calc(height=test_h, width=test_w)
