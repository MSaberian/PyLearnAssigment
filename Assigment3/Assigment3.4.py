num = int(input("please enter a number: "))

for i in range(num):
    if i%2 == 0:
        print("*",end="")
    else:
        print("#", end="")
        