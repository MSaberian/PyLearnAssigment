number = int(input("please enter number: "))

Factorial = 1
couter = 0
while True:
    couter += 1
    Factorial *= couter
    if Factorial == number:
        print("yes")
        break

    elif Factorial > number:
        print("no")
        break
