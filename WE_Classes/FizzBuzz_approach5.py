# Fizzbuzz approach 5 - Using pick() function

def fizzbuzz6(k: int) -> str:
    def pick(n: int) -> int:
        return 2 * int(n % 5 == 0) + int(n % 3 == 0)
    return [str(k), "FIZZ", "BUZZ", "FIZZBUZZ"][pick(k)]
