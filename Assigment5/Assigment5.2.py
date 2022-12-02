# import MoSaFunction5

n = int(input("please enter first number: "))
m = int(input("please enter second number: "))
# MoSaFunction5.MultiplicationTable(n,m)
for i in range(n+1):
    for j in range(m+1):
        if i == 0 and j == 0:
            print("X",end="\t")
        elif i == 0 or j == 0:
            print(i + j,end="\t")
        else:
            print(i * j,end="\t")
    print("")