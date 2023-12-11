import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = time.time()

primes = []
count = 0
number = 2

while count < 1000:
    if is_prime(number):
        primes.append(number)
        count += 1
    number += 1

end = time.time()

print("The first 1000 prime numbers are: ", primes)
print("Time taken: ", end - start, "seconds.")
