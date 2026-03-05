marks = list(map(int, input().split()))

if any(m < 35 for m in marks):
    print("FAIL")
else:
    avg = sum(marks) / 5
    if avg >= 75:
        print("DISTINCTION")
    else:
        print("PASS")