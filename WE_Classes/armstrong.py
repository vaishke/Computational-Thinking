# Generating armstrong numbers in a given range

def sum_of_powers(num: int) -> int:
    return sum([int(digit) ** (len(str(num))) for digit in str(num)])

def check_armstrong(num: int) -> bool:
    return num == sum_of_powers(num)

def generate_armstrong(start: int, stop: int) -> list[int]:
    return list(filter(check_armstrong, range(start, stop)))
