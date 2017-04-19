class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] != '0':
                dp[i] += dp[i-1] if i > 0 else 1
            if i > 0 and s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2] if i > 1 else 1
        return dp[-1]
        
class Solution:
    # @param s, a string
    # @return an integer
        
    def numDecodings(self, s):
        n = len(s)
        
        if n == 0:
            return 0
            
        memo = [0] * (n + 1)
        memo[n] = 1
        if int(s[n-1]) == 0:
            memo[n-1] = 0
        else:
            memo[n-1] = 1

        for i in range(n-2, -1, -1):
            if int(s[i]) == 0:
                memo[i] = 0
            elif int(s[i:i+2]) > 26:
                memo[i] = memo[i+1]
            else:
                memo[i] = memo[i+1] + memo[i+2]
        return memo[0]
