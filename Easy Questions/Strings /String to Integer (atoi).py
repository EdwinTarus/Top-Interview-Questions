class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        
        if not s:
            return 0
        
        i = 0
        sign = 1
        
        if s[i] == "+":
            i +=1
        elif s[i] == "-":
            i +=1
            sign = -1
        
        parsed = 0
        
        while i < len(s):
            cur = s[i]
            #"4193 with words"
            if not cur.isdigit():
                break 
            else:
                parsed = parsed * 10 + int(cur)
            i +=1
        
        parsed *= sign
        # within bounds
        MIN = -2147483648 # -2^31
        MAX = 2147483647 # 2^31 -1
        
        if parsed > MAX:
            return MAX
        if parsed < MIN:
            return MIN
        return parsed
        
