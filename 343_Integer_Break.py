class Solution(object):
    """ Wrong. """
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = max([max(dp(j), j) * max(dp(i-j), i-j) for j in range(1, i)])
        return dp[-1]
        
class Solution(object):
    """ DP. 4%. 
    
    TODO: There is another O(lgn) math solution. I did not spend time on that. """
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = max([max(dp[j], j) * max(dp[i-j], i-j) for j in range(1, i)])
        return dp[-1]
        
class Solution(object):
    """ DP. Improvement. 24%. """
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = max([max(dp[j], j) * max(dp[i-j], i-j) for j in range(1, i/2+1)])
        return dp[-1]
