class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1
        valid = True
        while (l< r):
            #check if matching letter
            if (s[l] == s[r]):
                valid = True 
                l +=1
                r -=1
            else:
                if (self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])):
                    valid = True
                    return valid
                else:
                    return False
                
        return valid

    def isPalindrome(self, s:str):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

        