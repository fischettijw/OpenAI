# write a python program to calculate the sum of numbers from 1 to 100,000,000 and print the sum and length of time it took to run the program. The program should use a loop to calculate the sum.
import time

start_time = time.time()

sum = 0
for i in range(1, 100_000_001):
    sum += i

end_time = time.time()

print("Sum of numbers from 1 to 100,000,000: ", sum)
print("Time taken to calculate the sum: ", end_time - start_time, "seconds")
