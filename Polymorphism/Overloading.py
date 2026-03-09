class Addition:

    def add(self, *numbers):
        sum = 0
        for num in numbers:
            sum += num
        return sum


a = Addition()

print(a.add(2, 3))
print(a.add(2, 3, 4))
print(a.add(2, 3, 4, 5))