class Solution(object):
    """ Dynamic Programming. Tree.
    
    dp[i] - number of unique binary search trees with i consecutive nodes
    dp[n]
    dp[i] = sum(max(dp[j], 1), max(dp[i-j-1], 1) for j from 0 to i-1)
    dp[0] = 0
    """
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = sum([max(dp[j], 1)*max(dp[i-j-1], 1) for j in range(0, i)])
        return dp[-1]
