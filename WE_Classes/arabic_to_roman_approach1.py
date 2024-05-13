# Converting from Arabic to Roman - Approach 1

def arabic_to_roman(num: int) -> str:
    a2r = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

    roman = ''
    for n, r in a2r:
        howmany, num = divmod(num, n)
        roman += howmany * r
    return roman
