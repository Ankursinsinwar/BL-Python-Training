import time

input("Press ENTER to start stopwatch")
start = time.time()

input("Press ENTER to stop stopwatch")
end = time.time()

elapsed = end - start

print("Elapsed Time:", elapsed, "seconds")