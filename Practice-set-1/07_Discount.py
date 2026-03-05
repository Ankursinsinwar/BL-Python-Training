amount = float(input())

if amount >= 5000:
    amount *= 0.80
elif amount >= 3000:
    amount *= 0.90
elif amount >= 1000:
    amount *= 0.95

print(int(amount))
