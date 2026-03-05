number = input()
valid = True

for i in range(len(number) - 1):
    if number[i] >= number[i + 1]:
        valid = False
        break

if valid:
    print("YES")
else:
    print("NO")