class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       # l, r = 0, 1
        maxprof = 0 
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxprof += (prices[i] - prices[i-1])
        return maxprof
