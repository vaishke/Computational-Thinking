# Separating Digits of a Number

def separate_digits(num: int) -> list[int]:
    num_str = str(num)
    digits = [int(digit) for digit in num_str]
    return digits
