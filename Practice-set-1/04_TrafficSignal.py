T = int(input())
T = T % 90
if T == 0:
    T = 90

if 1 <= T <= 30:
    print("RED")
elif 31 <= T <= 45:
    print("YELLOW")
else:
    print("GREEN")
