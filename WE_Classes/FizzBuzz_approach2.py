# FizzBuzz Approach 2

def fizzbuzz_(f, limit: int) -> list[str]:
    return [fizzbuzz2(i) for i in range(1, limit)]

def fizzbuzz2(n: int) -> str:
    fb = ""
    if n % 3 == 0:
        fb += "FIZZ"
    if n % 5 == 0:
        fb += "BUZZ"
    if fb == "":
        return str(n)
    else:
        return fb
