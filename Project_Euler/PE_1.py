"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def check_divisible_3_5(num: int) -> bool:
    if num % 3 == 0 or num % 5 == 0:
        return True
    return False

def divisible_sum(num: int) -> int:
    sum1 = 0
    for i in range(num):
        if check_divisible_3_5(i) == True:
            sum1 += i
    return sum1

print(divisible_sum(1000))
