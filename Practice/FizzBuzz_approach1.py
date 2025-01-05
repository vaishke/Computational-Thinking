# FizzBuzz Question - Approach 1 - Function sent as argument

def check_fizzbuzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 5 == 0:
        return "buzz"
    elif num % 3 == 0:
        return "fizz"
    else:
        return str(num)

def fizzbuzz001(check_fizzbuzz, limit: int) -> list[str]:
    return [check_fizzbuzz(i) for i in range(1, limit)]
