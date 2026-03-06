import random

n = int(input("Enter number of coin flips: "))

if n <= 0:
    print("Enter a positive integer")
else:
    heads = 0
    tails = 0

    for i in range(n):
        if random.random() < 0.5:
            heads += 1
        else:
            tails += 1

    print("Heads %:", (heads/n)*100)
    print("Tails %:", (tails/n)*100)