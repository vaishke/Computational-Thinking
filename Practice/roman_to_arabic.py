# Converting Roman Numeral to Arabic

def roman_to_arabic(roman: str) -> int:
    romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    normalized = roman.replace("CM", "DCCCC").replace('CD', 'CCCC').\
                       replace('XC', 'LXXXX').replace('XL', 'XXXX').\
                       replace('IX', 'VIIII').replace('IV', 'IIII')
    return sum(romans[ch] for ch in normalized)
