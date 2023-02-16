ar1 = [1, 4, 3, 4, 1]
ar2 = [3, 2, 1]
ar3 = [5, 6, 6, 5]
ar4 = [6, 10, 10, 4]

def check(ar):
    for i in range(len(ar)//2):
        if ar[i] != ar[-1*(i+1)]:
            return False
    return True

print(check(ar4))