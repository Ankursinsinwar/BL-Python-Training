rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

arr = []

print("Enter elements:")

for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input())
        row.append(val)
    arr.append(row)

print("2D Array:")

for row in arr:
    print(row)