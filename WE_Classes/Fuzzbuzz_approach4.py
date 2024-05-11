# FizzBuzz approach 4 - using boolean concept

def fizzbuzz4(n: int) -> str:
    fbs = {(True, True): "FIZZBUZZ", (True, False): "BUZZ", (False, True): "FIZZ", (False, False): str(n)}
    return fbs[(n % 5 == 0, n % 3 == 0)]
