num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))

Divisors1 = []
Divisors2 = []
Greatest_Common_Divisor = 1

for i in range(1,num1+1):
    if (num1 / i).is_integer():
        Divisors1.append(i)
        
for i in range(1,num2+1):
    if (num2 / i).is_integer():
        Divisors2.append(i)
        if i in Divisors1:
            Greatest_Common_Divisor = i

print("Divisors number",str(num1) ,"is: ", str(Divisors1))
print("Divisors number",str(num2) ,"is: ", str(Divisors2))
print("The Greatest Common Divisor is: ", str(Greatest_Common_Divisor))