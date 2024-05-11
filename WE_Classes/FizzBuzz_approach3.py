# FizzBuzz approach 3 - Identifying the sequence and implementing

def fizzbuzz3(n: int) -> str:
    fb_cycle = ["FIZZBUZZ", "", "", "FIZZ", "", "BUZZ", "FIZZ", "", "", "FIZZ", "BUZZ", "", "FIZZ", "", ""]
    return fb_cycle[n % 15] or str(n)
