InitialBalance = int(input())
N = int(input())

for _ in range(N):
    amount = int(input())
    if amount % 100 == 0 and InitialBalance >= amount:
        InitialBalance -= amount
        print("SUCCESS")
    else:
        print("FAILED")

print(InitialBalance)
