import math
A = int(input())
B = int(input())
prime_count = 0

for num in range(A, B + 1):
    if num > 1:
        prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            prime_count += 1

print(prime_count)
