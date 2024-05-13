# Converting numbers to words in Indian and Western Systems

WESTERN = {10 ** 12: 'Trillion ', 10 ** 9: 'Billion ', 10 ** 6: 'Million ', 1000: 'Thousand ', 1: ''}
INDIAN  = {10 ** 7: "Crore ", 10 ** 5: 'Lakh ', 1000: 'Thousand ', 1: ''}

def convert2digits(n: int) -> str:
    onewords = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ",
                "Nine ", "Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ",
                "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen"]
    tens = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty", "Ninety"]

    if n < len(onewords):
        return onewords[n]
    else:
        return tens[n // 10] + onewords[n % 10]

def convert3digits(n: int) -> str:
    if n < 100:
        return convert2digits(n)
    else:
        hundreds, tensunits = divmod(n, 100)
        if tensunits == 0:
            return convert2digits(hundreds) + "Hundred "
        else:
            return convert2digits(hundreds) + "Hundred and " + convert2digits(tensunits)

def figures_to_words(system: dict, value: int) -> str:
    in_words = ''
    for denom in sorted(system.keys(), reverse=True):
        howmany, value = divmod(value, denom)
        if howmany > 0:
            in_words += convert3digits(howmany) + system[denom]
    return in_words
