correct_pin = input()

for _ in range(3):
    attempt = input()
    if attempt == correct_pin:
        print("ACCESS GRANTED")
        break
else:
    print("LOCKED")