def aliquot(n: int) -> int:
    r, aliq = 2, 1
    while r * r < n:
        if n % r == 0:
            aliq += r + (n//r)
        r += 1
    if r == (n // r):
        aliq += r
    return aliq

def gen_amicable_pairs(start: int, limit: int) -> list[tuple]:
    pairs = []
    for n in range(start, limit):
        dn = aliquot(n)
        if n < dn:
            if aliquot(dn) == n:
                pairs.append((n, dn))
    return pairs

def euler21() -> int:
    return sum(sum(_) for _ in gen_amicable_pairs(1, 10000))
