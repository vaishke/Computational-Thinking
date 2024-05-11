# Finding the sum of strong numbers below a given limit

def digits(num: int) -> list[int]:
    return [int(digit) for digit in str(num)]

def check_strong(num: int) -> int:
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return num == sum([factorials[i] for i in digits(num)])

def strong_sum_upto(upto: int) -> int:
    return sum([num for num in range(1, upto) if check_strong(num)])
