class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 1
        
        for s in range(n - 1):
            temp = first
            first = first + second
            second = temp
            
        return first 
        
