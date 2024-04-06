"""
n! means n * (n - 1) * ... * 3 * 2 * 1.
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!.
"""

def factorial(num: int) -> int:
    product = 1
    while num > 0:
        product *= num
        num -= 1
    return product

def sum_of_factorial(num: int) -> int:
    value = factorial(num)
    sum_of_digits = 0
    while value > 0:
        sum_of_digits += (value % 10)
        value //= 10
    return sum_of_digits

print(sum_of_factorial(100))
