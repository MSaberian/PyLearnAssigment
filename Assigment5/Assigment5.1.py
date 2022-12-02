# import MoSaFunction5

n = int(input("please enter first number: "))
m = int(input("please enter second number: "))
# MoSaFunction5.chess(n,m)
for i in range(n):
    for j in range(m):
        if (i%2 + j%2)%2:
            print("*",end="")
        else:
            print("#",end="")
    print("")