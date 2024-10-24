class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        # totalL[n] = max(totalL [n-2] + Ln, totalL [n-1])
        # # [2,7,9,3,1]
        # tot[2]
        # tot[7]
        # tot[11]
        # tot[11]
        # tot[12]
        
        # [rob1[], rob2[], n[], n+1[]]
        for n in nums:
            totalLoot = max(rob1 + n, rob2)
            rob1  = rob2
            rob2 = totalLoot
        return rob2
        
        
