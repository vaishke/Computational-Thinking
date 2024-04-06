"""
A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def checkPalindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

def palindromeProducts(digits: int) -> list[int]:
    products = list()
    for factor1 in range(10 ** (digits - 1), 10 ** digits):
        for factor2 in range(factor1 + 1, 10 ** digits):
            if checkPalindrome(factor1 * factor2):
                products.append(factor1 * factor2)
    return products

def maxPalindrome(digits: int) -> int:
    return max(palindromeProducts(digits))

print(maxPalindrome(3))
