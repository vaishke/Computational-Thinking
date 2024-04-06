"""
The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1.
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
Once the chain starts the terms are allowed to go above one million.
"""

def generate_collatz_sequence(num: int) -> list[int]:
    collatz_seq = [num]
    while num != 1:
        if num % 2 == 0:
            collatz_seq.append(num // 2)
            num //= 2
        else:
            num = (3 * num) + 1
            collatz_seq.append(num)
    return collatz_seq

def max_length_sequence(limit: int) -> int:
    result = list()
    for num in range(limit):
        result.append(generate_collatz_sequence(num))
    return max(result)

max_length_sequence(13)
