class Solution(object):      
    """ Dynamic Programming. beats 34%
    
    Only p may have wildcard characters.
    
    dp[i][j]: does s[:i] matches p[:j]
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s) + 1; m = len(p) + 1
        dp = [[False]*m for _ in range(n)]
        dp[0][0] = True
        for i in range(1, n):
            dp[i][0] = False
        for j in range(1, m):
            dp[0][j] = (p[j-1] == '*' and dp[0][j-1])
        for i in range(1, n):
            for j in range(1, m):
                if p[j-1] != '*':
                    dp[i][j] = (dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '?'))
                else:
                    dp[i][j] = (dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j])
        return dp[-1][-1]
