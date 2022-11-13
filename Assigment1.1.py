import math 

print("*** Welcome to MoSa calculator ***")
print("Available operation is:")
print("+")
print("-")
print("*")
print("/")
print("sin")
print("cos")
print("tan")
print("log")
print("factorial")

op = input("Enter operation: ")

if op =="+" or op =="-" or op =="*" or op =="/":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

else:
    a = float(input("Enter number: "))

if op == "+":
    result = a + b

elif op == "-":
    result = a - b

elif op == "*":
    result = a * b
    
elif op == "/":
    if b == 0:
        result = "Cannot divide by zero"
    else:
        result = a / b

elif op == "sin":
    a = a / 180 * math.pi 
    result = math.sin(a)

elif op == "cos":
    a = a / 180 * math.pi 
    result = math.cos(a)
    
elif op == "tan":
    a = a / 180 * math.pi 
    result = math.tan(a)

elif op == "log":
    result = math.log(a)

elif op == "Sqrt":
    result = math.sqrt(a)
    
elif op == "factorial":
    result = math.factorial(int(a))

else:
    result = op + " is not true operation!!"

print(result)
