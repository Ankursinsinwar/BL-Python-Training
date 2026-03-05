N = int(input())
inflows = list(map(int, input().split()))

capacity = 1000
current = 0

for i in range(N):
    current += inflows[i]
    if current > capacity:
        print(i + 1)
        break