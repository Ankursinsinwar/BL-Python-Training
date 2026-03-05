drain_per_minute = int(input())
battery = 100
minutes = 0

while battery > 0:
    battery -= drain_per_minute
    minutes += 1

print(minutes)
