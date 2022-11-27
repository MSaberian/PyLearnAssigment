Array = []
Yarra = []

while True:
    num = input("please enter new number: ")
    if num.lstrip("-").isdigit():
        Array.append(int(num))
        Yarra.append(int(0))
    elif num == "end":
        for i in range(len(Array)):
            Yarra[i] = Array[len(Array) - i - 1]

        print("Array: " + str(Array))
        print("Reversed Array: " + str(Yarra))
        break
    else:
        print("⚠ enter only number")