# task_1
'''
NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]
We have the following input list of numbers, some of them are prime.
You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.

Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS.

Compare the results and performance of each of them.
'''

import time

NUMBERS = [
2,  # prime
1099726899285419,
1570341764013157,  # prime
1637027521802551,  # prime
1880450821379411,  # prime
1893530391196711,  # prime
2447109360961063,  # prime
3,  # prime
2772290760589219,  # prime
3033700317376073,  # prime
4350190374376723,
4350190491008389,  # prime
4350190491008390,
4350222956688319,
2447120421950803,
   5,  # prime
]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def filter_primes_with_threads(numbers):
    with ThreadPoolExecutor() as executor:
        primes = executor.map(is_prime, numbers)
    return [num for num, prime in zip(numbers, primes) if prime]

def filter_primes_with_processes(numbers):
    with ProcessPoolExecutor() as executor:
        primes = executor.map(is_prime, numbers)
    return [num for num, prime in zip(numbers, primes) if prime]

# час, який займає filter_primes_with_threads
start_time = time.time()
filter_primes_with_threads(NUMBERS)
end_time = time.time()
print(f"filter_primes_with_threads takes {end_time - start_time} sec")

# час, який займає filter_primes_with_processes
start_time = time.time()
filter_primes_with_processes(NUMBERS)
end_time = time.time()
print(f"filter_primes_with_processes takes {end_time - start_time} sec")