units = int(input())
total_bill = 0

if units <= 100:
    total_bill = units * 3
elif units <= 200:
    total_bill = 100 * 3 + (units - 100) * 5
else:
    total_bill = 100 * 3 + 100 * 5 + (units - 200) * 8

if units > 300:
    total_bill += total_bill * 0.10

print(int(total_bill))
