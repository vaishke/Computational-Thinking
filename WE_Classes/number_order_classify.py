"""
Number Classification (input - int, output - A/D/P/V/X)
'A' - if number is strictly ascending
'D' - if number is strictly descending
'P' - if number has a peak - only one peak - highest number in the series of digit
'V' - if number has a valley - only one valley - lowest number in the series of digit
'X' - if the is none of the above
"""

def check_ascending(num: int) -> bool:
    return "".join(sorted(set(str(num)))) == str(num)

def check_descending(num: int) -> bool:
    return "".join(sorted(set(str(num)), reverse = True)) == str(num)

def check_peak(num: int) -> bool:
    num_str = str(num)
    max_ind = num_str.index(max(num_str))
    if (check_ascending(num_str[0:max_ind]) and check_descending(num_str[max_ind + 1:])) and num_str.count(max(num_str)) == 1:
        return True
    return False

def check_valley(num: int) -> bool:
    num_str = str(num)
    min_ind = num_str.index(min(num_str))
    if (check_descending(num_str[0:min_ind]) and check_ascending(num_str[min_ind + 1:])) and num_str.count(min(num_str)) == 1:
        return True
    return False

def classify_num(num: int) -> str:
    if check_peak(num):
        return 'P'
    elif check_valley(num):
        return 'V'
    elif check_ascending(num):
        return 'A'
    elif check_descending(num):
        return 'D'
    else:
        return 'X'
