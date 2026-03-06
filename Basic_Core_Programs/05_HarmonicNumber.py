N = int(input("Enter value of N: "))

if N == 0:
    print("N must not be zero")
else:
    harmonic = 0
    for i in range(1, N+1):
        harmonic += 1/i

    print("Harmonic Value:", harmonic)