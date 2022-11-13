print("*** Welcome to MoSa Calculation of educational status programme ***")

name = input("enter your name: ")
family = input("enter your family: ")

a = float(input("Enter first score: "))
b = float(input("Enter second score: "))
c = float(input("Enter third score: "))

d = (a + b + c)/3
result = "great"

if d <12:
    result = "fail"
elif d < 17:
    result = "normal"
    
print(name + " " + family + "'s GPA is " + result)