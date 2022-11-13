import math

print("*** Welcome to MoSa Calculation Body Mass Index (BMI) ***")

weight = float(input("enter your weight(Kg): "))
height = float(input("enter your height(m): "))

BMI = weight/height**2

if BMI < 18.5:
    result = "Underweight"
    
elif BMI < 25:
    result = "Normal Weight"
    
elif BMI < 30:
    result = "Overweight"
    
elif BMI < 35:
    result = "Obesity"
    
else:
    result = "Extreme Obesity"

print("Your BMI is " + "%.2f" % BMI + ", therefore your BMI is " + result)