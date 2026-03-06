N = int(input("Enter number: "))

i = 2

while i*i <= N:
    while N % i == 0:
        print(i)
        N = N // i
    i += 1

print(N)