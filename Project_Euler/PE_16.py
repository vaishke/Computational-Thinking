"""
2^{15} = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^{1000}?
"""

def powers_of_2(power: int) -> int:
    return 2 ** power

def digit_sum(num: int) -> int:
    num_str = str(powers_of_2(num))
    digits = [int(digit) for digit in num_str]
    return sum(digits)

print(digit_sum(1000))
