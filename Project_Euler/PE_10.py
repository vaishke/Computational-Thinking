"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import math

def check_prime(num: int) -> bool:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and num != 2:
            return False
    return True

def generate_prime(num: int) -> list[int]:
    prime = list()
    for i in range(2, num + 1):
        if check_prime(i) == True:
            prime.append(i)
    return prime

def sum_of_primes(num: int) -> int:
    return sum(generate_prime(num))

# print(check_prime(4))
print(sum_of_primes(2000000))
