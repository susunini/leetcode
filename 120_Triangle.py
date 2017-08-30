class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        if not triangle:
            return 0
        dp = [li[:] for li in triangle] #
        n = len(dp)
        for i in range(1,n):
            m = len(dp[i])
            for j in range(m):
                if 0 < j < m-1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j])
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1]
                dp[i][j] += triangle[i][j]
        return min(dp[-1])
