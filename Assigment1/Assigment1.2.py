import math

print("*** Welcome to MoSa validation the size of the sides of a triangle ***")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

ind = 0

if a < (b + c):
    ind = ind + 1

if b < (a + c):
    ind = ind + 1

if c < (b + a):
    ind = ind + 1

if ind == 3:
    print("plot this triangle is possible")
else: 
    print("plot this triangle is impossible")