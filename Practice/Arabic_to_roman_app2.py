# Converting Arabic to Roman  - Approach 2

def arabic2roman(num: int) -> str:
    a2r = {1000:'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
           50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    roman = ''
    for n, r in sorted(a2r.items(), reverse=True):
        roman += (num // n) * r
        num %= n
    return roman
