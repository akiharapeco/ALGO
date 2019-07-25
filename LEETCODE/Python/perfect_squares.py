class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = list(range(n+1))
        for i in range(4, n+1):
            j = square = 1
            while square <= i:
                if dp[i] > 1 + dp[i-square]:
                    dp[i] = 1 + dp[i-square]    
                j += 1
                square = j * j
        return dp[n]
    
