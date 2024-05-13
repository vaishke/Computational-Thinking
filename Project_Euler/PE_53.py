import math

def combination(total_obj: int, choose_obj: int) -> int:
    return (math.factorial(total_obj))/(math.factorial(choose_obj) * math.factorial(total_obj - choose_obj))

def count_limit_combinations(limit: int) -> int:
    above_million = list()
    for total_obj in range(1, 100 + 1):
        for choose_obj in range(0, total_obj):
            if combination(total_obj, choose_obj) >= limit:
                above_million.append((total_obj, choose_obj))
    return len(above_million)


print(count_limit_combinations(1000000))
