import time

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

start = time.time()

primes = [2, 3]
count = 2
number = 5

while count < 1000:
    if is_prime(number):
        primes.append(number)
        count += 1
    number += 2

end = time.time()

print("The first 1000 prime numbers are: ", primes)
print("Time taken: ", end - start, "seconds.")
