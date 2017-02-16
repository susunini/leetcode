class Solution(object):
    """ Dynamic Programming.
    
    This problem is different from Wildcard matching in that * matches zero or more 
    PRECEEDING characters.
    
    dp[i][j]: does s[:i] matches p[:j]
    dp[i][j] = if p[j] != '*' or s[i-1] == p[j-1] and dp[i-1][j-1]
                                 p[j-1] == '.' and dp[i-1][j-1]
               else p[j] == '*' or x matches empty sequence => dp[i][j-2]
                                   x matches single charater => dp[i-1][j-2] and s[i-1] == p[j-2]
                                   x matches multiple characters => dp[i-1][j] and s[i-1] == p[j-2]
    dp[0][0] = True
    dp[i][0] = False for i in range(1,n)
    dp[0][1] = False
    dp[0][j] = dp[0][j-2] and p[j-1] == '*' for j in range(2, m)
    return dp[n-1][m-1]
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
        for j in range(2, m):
            dp[0][j] = (p[j-1] == '*' and dp[0][j-2])
        for i in range(1, n):
            for j in range(1, m):
                if p[j-1] != '*':
                    dp[i][j] = (dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.'))
                else:
                    dp[i][j] = any([
                        dp[i][j-2], 
                        (dp[i-1][j-2] or dp[i-1][j]) and (s[i-1] == p[j-2] or p[j-2] == '.')
                        ])
        return dp[-1][-1]
