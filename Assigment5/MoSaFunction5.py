import math

def chess(n,m):
    for i in range(n):
        for j in range(m):
            if (i%2 + j%2)%2:
                print("*",end="")
            else:
                print("#",end="")
        print("")

def MultiplicationTable(n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and j == 0:
                print("X",end="\t")
            elif i == 0 or j == 0:
                print(i + j,end="\t")
            else:
                print(i * j,end="\t")
        print("")

def Rhombus(n):
    for i in range(n*2-1):
        for j in range(n*2-1):
            if abs(j - (n-1)) <= (n-1 - abs(i - (n-1))):
                print("*",end="")
            else:
                print(" ",end="")
        print("")

def KhayyamPascalsTriangle(n):
    KPT = []
    for i in range(n):
        KPT.append([0]*(i+2))
        KPT[i][0] = 1
        print(KPT[i][0] ,end="\t")
        for j in range(1,i+1):
            KPT[i][j] = KPT[i-1][j-1] + KPT[i-1][j]
            print(KPT[i][j] ,end="\t")
        print("")