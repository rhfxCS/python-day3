name = input("what's your name? ").title().strip()
height = float(input("enter your height in cm :"))
weight = float(input("enter your wedth in kg :"))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Healthy")
else: 
    print("Overweight")