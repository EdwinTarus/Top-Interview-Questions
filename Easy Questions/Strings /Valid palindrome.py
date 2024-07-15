class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join(c for c in s if c.isalnum())
        
        fs = ""
        for c in s:
            if c.isalnum():
                fs += c
        
        fs=fs.lower()
        t = fs[::-1]
        
        if t!=fs:
            return False 
        return True 
