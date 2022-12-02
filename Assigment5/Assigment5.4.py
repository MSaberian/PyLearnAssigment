# import MoSaFunction5

n = int(input("please enter number: "))
# MoSaFunction5.KhayyamPascalsTriangle(n)
KPT = []
for i in range(n):
    KPT.append([0]*(i+2))
    KPT[i][0] = 1
    print(KPT[i][0] ,end="\t")
    for j in range(1,i+1):
        KPT[i][j] = KPT[i-1][j-1] + KPT[i-1][j]
        print(KPT[i][j] ,end="\t")
    print("")