# Kaprekar's Sequence Generation

def num_to_digits(num: int) -> list[int]:
    return [int(digit) for digit in str(num)]

def digits_to_num(digits: list[int]) -> int:
    return int("".join(str(digit) for digit in digits))

def largest(num: int) -> int:
    return digits_to_num(sorted(num_to_digits(num), reverse = True))

def smallest(num: int) -> int:
    return digits_to_num(sorted(num_to_digits(num)))

def next_kaprekar(num: int) -> int:
    return largest(num) - smallest(num)

def kaprekar_seq(num: int) -> list[int]:
    sequence = []
    while num not in sequence:
        sequence.append(num)
        num = next_kaprekar(num)
    return sequence
