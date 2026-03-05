N = int(input())
seats = 40

for _ in range(N):
    request = int(input())
    if seats >= request:
        seats -= request
        print("CONFIRMED")
    else:
        print("WAITLISTED")