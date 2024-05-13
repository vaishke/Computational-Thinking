def exponent(num: int, exp: int) -> int:
    return num ** exp

def digit_sum(num: int) -> int:
    sum_digits = 0
    while num > 0:
        sum_digits += (num % 10)
        num //= 10
    return sum_digits

def maximum_sum(limit: int) -> int:
    sum_of_exponents = list()
    for iter1 in range(1, limit + 1):
        for iter2 in range(1, limit + 1):
            sum_of_exponents.append(digit_sum(exponent(iter1, iter2)))
    return max(sum_of_exponents)

print(maximum_sum(100))
