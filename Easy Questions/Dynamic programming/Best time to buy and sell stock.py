class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        maxprofit = 0
        for price in prices:
            if price < min_price:
                min_price = price
                
            profit = price - min_price
            maxprofit = max(maxprofit, profit)
                
        return maxprofit
        
