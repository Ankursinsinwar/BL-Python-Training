import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

delta = b*b - 4*a*c

if delta < 0:
    print("Complex roots")
else:
    root1 = (-b + math.sqrt(delta)) / (2*a)
    root2 = (-b - math.sqrt(delta)) / (2*a)

    print("Root1:", root1)
    print("Root2:", root2)