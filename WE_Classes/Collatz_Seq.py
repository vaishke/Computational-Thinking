# Program for generating Collatz Sequence Numbers

def next_collatz(num: int) -> int:
    return num // 2 if num % 2 == 0 else 3 * num + 1

def gen_collatz(num: int) -> list[int]:
    if num == 4:
        return [4, 2, 1]
    else:
        return [num] + gen_collatz(next_collatz(num))
