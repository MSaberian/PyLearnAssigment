Array = []

while True:
    newinput = input("please enter new number: ")
    if newinput == "end":
        print(Array)
        break
    else:
        if newinput not in Array:
            Array.append(newinput)
