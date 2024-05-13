def exponent(num: int, exp: int) -> int:
    return num ** exp

def generatePowers(limit: int) -> list[int]:
    powers = list()
    for num in range(2, limit + 1):
        for exp in range(2, limit + 1):
            powers.append(exponent(num, exp))
    return powers

def noOfDistinctPowers(limit: int) -> int:
    return len(set(generatePowers(limit)))

print(noOfDistinctPowers(100))
