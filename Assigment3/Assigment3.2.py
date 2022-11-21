import random

narry = []
i = 0
n = int(input("please enter number: "))
while i < n:
    m = random.randint(0, 2*n)
    if not m in narry:
        narry.append(m)
        i += 1

print(narry)