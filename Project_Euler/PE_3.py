"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def factorize(num: int) -> list[int]:
    factors = list()
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    r = 3
    while num > 1:
        while num % r == 0:
            factors.append(r)
            num //= r
        r += 2
    return factors

def max_prime_factor(num: int) -> int:
    return max(factorize(num))

%time
print(max_prime_factor(600851475143))
