inp = ""
arr = []
Ordered = True
while True:
    num = input("please enter new number: ")
    if num.isnumeric():
        arr.append(int(num))
        if len(arr) > 1:
            if arr[len(arr)-1] < arr[len(arr)-2]:
                Ordered = False
    elif num == "end":
        break
    else:
        print("⚠ enter only number")

print(arr)
if Ordered:
    print("✅ that is ordered array")
else:
    print("🈹 that is not ordered array")

    