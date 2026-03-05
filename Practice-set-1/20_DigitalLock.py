number = int(input())

while number >= 10:
    final_digit = 0
    while number > 0:
        final_digit += number % 10
        number //= 10
    number = final_digit

print(number)