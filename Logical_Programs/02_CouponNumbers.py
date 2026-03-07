import random

N = int(input("Enter number of coupons: "))

coupons = set()
count = 0

while len(coupons) < N:
    num = random.randint(1, N)
    coupons.add(num)
    count += 1

print("Total random numbers generated:", count)