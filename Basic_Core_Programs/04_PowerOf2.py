N = int(input("Enter value of N: "))

if 0 <= N < 31:
    for i in range(N+1):
        print(f"2^{i} =", 2**i)
else:
    print("Enter N between 0 and 30")