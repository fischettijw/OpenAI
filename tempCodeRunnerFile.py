import time

start = time.time()

sum = 0
for i in range(1, 10000001):
    sum += i

print("The sum of numbers from 1 to 10,000,000 is: ", sum)

end = time.time()

print("Time taken to calculate the sum: ", end - start, "seconds")
