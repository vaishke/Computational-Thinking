class Solution:
    def romanToInt(self, s: str) -> int:
        
        dec = 0
        
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        for i in range(0, len(s)):
            
            if i + 1 != len(s):
            
                if roman[s[i]] >= roman[s[i + 1]]:
                
                    dec = dec + roman[s[i]]
                
                else:
                
                    dec = dec - roman[s[i]]
            
            else:
                
                dec = dec + roman[s[i]]
                
        return dec
