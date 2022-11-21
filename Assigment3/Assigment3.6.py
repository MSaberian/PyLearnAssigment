num1 = int(input("please enter first number: "))
num2 = int(input("please enter second number: "))

coefficient1 = 1
coefficient2 = 1

while True:
    multiple1 = coefficient1 * num1
    multiple2 = coefficient2 * num2
    if multiple1 == multiple2:
        print("Greatest common multiple of " , str(num1), "and" , str(num2) , "is: ", str(multiple1))
        print("coefficient1: " , str(coefficient1), "coefficient2:" , str(coefficient2) )
        break
    elif multiple1 > multiple2:
        coefficient2 += 1
    else:
        coefficient1 += 1
