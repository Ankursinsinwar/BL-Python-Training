year = int(input("Enter a year: "))

if year < 1000 or year > 9999:
    print("Enter a 4 digit year")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")