class Solution(object):
    """ Dynamic Programming.
    
    dp[i] - number of ways to step i
    dp[1] = 1; dp[2] = 2
    dp[i] = dp[i-1] + dp[i-2]
    return dp[n] 
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        dp = [1, 2]
        for i in range(3, n+1): # Wrong: for i in range(3, n)
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
        return dp[-1]
