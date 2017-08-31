class Solution:
    """DP. Hard. 75%. """
    def minCut(self, s):
        if not s:
            return 0
        is_palindrome = self.getPalindromes(s)
        n = len(s)
        dp = [i for i in range(n-1,-1,-1)]
        for i in range(n-2,-1,-1):
            if is_palindrome[i][n-1]:
                dp[i] = 0
                continue
            for j in range(i+1, n):
                if not is_palindrome[i][j-1]:
                    continue
                dp[i] = min(dp[i], dp[j]+1)
        return dp[0]
                
 
    def getPalindromes(self, s):
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1): # Wrong: for i in range(n)
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif j-i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
        return dp
    
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        matrix = self.getPalindromeMatrix(s)
        n = len(s)
        dp = [i for i in range(n)]
        for i in range(n):
            if matrix[0][i]:
                dp[i] = 0
                continue
            for j in range(0, i):
                if matrix[j+1][i]:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[n-1]

    def getPalindromeMatrix(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1): # Wrong: for i in range(n)
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        return dp
                    
        
        

        
