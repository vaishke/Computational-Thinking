"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

from math import *

def check_prime(num: int) -> bool:
    flag = True
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            flag = False
            break
    return flag

def prime_factors(num: int) -> list[int]:
    prime_factors = list()
    for iter in range(2, int(sqrt(num)) + 1):
        if check_prime(iter) and num % iter == 0:
            prime_factors.append(iter)
    return prime_factors

%time
print(max(prime_factors(600851475143)))
