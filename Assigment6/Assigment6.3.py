import math

print("Solving the cubic equation")
print("enter a,b,c and d parameters")
print("ax^3 + bx^2 + cx + d = 0")

def cubic_equation(a,b,c,d):

    u = []
    u.append(1) 
    u.append(complex(-.5,math.sqrt(3)/2))
    u.append(complex(-.5,-1*math.sqrt(3)/2))

    delta = 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2

    delta0 = b**2 - 3*a*c
    delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    C = delta1 + math.sqrt(delta1**2 - 4*delta0**3)
    C = (C/2)**(1/3)

    X = []
    for i in range(3):
        x = b + u[i]*C + delta0/(u[i]*C)
        X.append(x/(-3*a))

    return X

while True:
    a = float(input("a: "))
    if a == 0.0:
        print("⚠ You have to choose non zero for a")
    else:
        break
    
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

print("{a}x^3 + {b}x^2 + {c}x + {d}".format(a=a, b=b, c=c, d=d))

X = cubic_equation(a,b,c,d)
for i in range(3):
    print("x{i} = {x}".format(i=i,x=X[i]))