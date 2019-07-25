from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1]-prices[0])
        
        maximum = [0, 
                   max(0, prices[1]-prices[0]), 
                   max([prices[2]-prices[0], prices[1]-prices[0], 0, prices[2]-prices[1]])] + [0 for num in prices[:-1]] 
        
        maxprof = [0 for i in range(len(prices)+2)]
        for i in range(-2, len(prices[:-2])):
            for j in range(-1, i+1):
                if prices[i+2] - prices[j+1] < 0:
                    continue
                maximum[i+2] = max(maximum[i+2], maxprof[j-1] + prices[i+2] - prices[j+1])
            maxprof[i+2] = max(maxprof[i+1], maximum[i+2])
    
        return maxprof[-3]