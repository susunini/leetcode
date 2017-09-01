class Solution(object):
    """ DP.
    dp[i][j] - number of t[:i+1] in s[:j+1]
    dp[i][j] = dp[i][j-1] => number of current t in previous s
               + dp[i-1][j-1] if s[i] == t[j] else 0 => number of previous t in previous s if s[i] == t[j]
    """
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t:
            return 0
        m = len(t); n = len(s)
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 if t[0] == s[0] else 0
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + (1 if t[0] == s[j] else 0)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1] if t[i] == s[j] else dp[i][j-1]
        return dp[m-1][n-1]
