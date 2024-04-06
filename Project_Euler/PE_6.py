"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_squares(limit: int) -> int:
    squares_sum = 0
    for num in range(1, limit + 1):
        squares_sum += (num ** 2)
    return squares_sum

def square_sums(limit: int) -> int:
    num_sum = 0
    for num in range(1, limit + 1):
        num_sum += num
    return (num_sum ** 2)

def difference(num: int) -> int:
    return abs(sum_squares(num) - square_sums(num))

print(difference(100))
