height = float(input("Enter height"))
weight = float(input("Enter weight"))

bmi = weight/(height*height)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("overweight")