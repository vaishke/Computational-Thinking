# Generating Weakleg numbers in a given range

def num_to_digits(num: int) -> list[int]:
    return [int(digit) for digit in str(num)]

def check_weakleg(num: int) -> bool:
    return num == sum([digit ** (num_to_digits(num).index(digit) + 1) for digit in num_to_digits(num)])

def generate_weaklegs(start: int, stop: int) -> list[int]:
    return list(filter(check_weakleg, range(start, stop)))
