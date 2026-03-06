n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

count = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                print(arr[i], arr[j], arr[k])
                count += 1

print("Total Triplets:", count)