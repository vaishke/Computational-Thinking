class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        y = x
        while x > 0:
            r = x % 10
            rev = rev*10 + r
            x //= 10
        if y >=0 and y == rev:
            return True
        else:
            return False
