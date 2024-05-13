def self_power(num: int) -> int:
    return num ** num

def sum_self_powers(limit: int) -> int:
    sum1 = 0
    for num in range(1, limit + 1):
        sum1 += self_power(num)
    return sum1

def last_ten_digits(num: int) -> str:
    digits = str()
    iter  = 1
    while iter <= 10:
        digits += str(num % 10)
        num //= 10
        iter += 1
    return digits[::-1]

print(last_ten_digits(sum_self_powers(1000)))
