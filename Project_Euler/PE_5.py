"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def check_divisible(dividend: int, divisor: int) -> bool:
    return dividend % divisor == 0

def smallest_multiple(limit: int) -> int:
    multiple = 1
    for divisor in range(2, limit + 1):
        if check_divisible(multiple, divisor):
            continue
        else:
            multiple *= divisor
    return multiple

print(smallest_multiple(10))
